import csv
import io
import os
import gzip
import contextlib
import importlib.resources
import itertools
import subprocess
import tempfile
import warnings

import Bio.SeqIO
import pandas
import pyfastani
from pandas.errors import EmptyDataError

class Ani:
	"""
	Use ANI to assign genome to genospecies and/or subspecies

	run_fastani
	purpose: runs fastANI for species/subspecies assignment and selects match with highest ANI
	input:
		taxon = "species", "subspecies", or "geneflow"; corresponds to directory of genomes to use
		fasta = query genome for fastANI
		final_results_directory = path to BTyper3 final results directory
		prefix = genome prefix to use for output files
	output:
		species or subspecies producing highest ANI value

	"""

	def __init__(self, taxon, fasta, final_results_directory, prefix):
		self.taxon = taxon
		self.fasta = fasta
		self.final_results_directory = final_results_directory
		self.prefix = prefix

	def run_fastani(self, taxon, fasta, final_results_directory, prefix):
		# create output folder if it doesn't exist
		ani_results_dir = os.path.join(final_results_directory, taxon)
		os.makedirs(ani_results_dir, exist_ok=True)

		# create the FastANI sketch
		sketch = pyfastani.Sketch()

		# get the ANI database using `importlib.resources`: note that since
		# files may not be available on the local filesystem (e.g. they could
		# be zipped), we use `importlib.resources.path` to get a system path
		# for each of them than can be passed to `fastANI`.
		data_module = "btyper3.seq_ani_db.{}".format(taxon)
		with importlib.resources.open_text(data_module, "{}.tsv".format(taxon)) as f:
			database = pandas.read_table(f, comment="#")
		# extract all the reference genomes
		for genome_id in database["id"]:
			with importlib.resources.open_binary(data_module, genome_id) as handle:
				reader = io.TextIOWrapper(gzip.GzipFile(fileobj=handle, mode="rb"))
				records = Bio.SeqIO.parse(reader, "fasta")
				sketch.add_draft(genome_id, (str(record.seq) for record in records))

		# index the references
		mapper = sketch.index()

		# query mapper with the input file
		with open(fasta) as handle:
			records = Bio.SeqIO.parse(handle, "fasta")
			sequences = [str(record.seq) for record in records]
			self.check_fragmentation(sequences, mapper.fragment_length)
			hits = mapper.query_draft(sequences)

		# make a table from the hits
		results = pandas.DataFrame(
			data=[
				[fasta, hit.name, hit.identity, hit.matches, hit.fragments]
				for hit in hits
			],
			columns=[
				"query",
				"hit",
				"ani",
				"matches",
				"fragments",
			],
		)

		# write raw FastANI results
		result_file = os.path.join(ani_results_dir, "{}_{}_fastani.txt".format(prefix, taxon))
		results.to_csv(result_file, index=False, header=False, sep="\t")

		# left join with database to get associated metadata for each hit
		results = pandas.merge( results, database, how="left", left_on="hit", right_on="id")

		if not results.empty:
			# sort values by decreasing ANI and get best hit
			results.sort_values("ani", ascending = False, inplace = True)
			best = results.iloc[0]

			if taxon == "species":
				if best.ani < best.threshold:
					return f"{best.species}*({best.ani})"
				else:
					return f"{best.species}({best.ani})"

			elif taxon == "subspecies":
				if best.ani < best.threshold:
					return "No subspecies"
				else:
					return f"{best.subspecies}({best.ani})"

			elif taxon == "geneflow":
				if best.ani < best.threshold:
					# if the ANI value doesn't fall within the pseudo-gene flow 
					# unit ANI boundary, try the 2nd to 5th most similar genomes
					for candidate in itertools.islice(results.itertuples(), 1, 5):
						if candidate.ani >= candidate.threshold:
							return f"{candidate.psub}({candidate.ani})"
					return f"{best.psub}*({best.ani})"
				else:
					return f"{best.psub}({best.ani})"

			elif taxon == "typestrains":
				return f"{best.typestrain}({best.ani})"

		else:
			if taxon == "species":
				return "(Species unknown)"
			elif taxon == "subspecies":
				return "No subspecies"
			elif taxon == "geneflow":
				return "(Pseudo-gene flow unit unknown)"
			elif taxon == "typestrains":
				return "(Type strain unknown)"

	def check_fragmentation(self, sequences, fragment_length):
		length_total = 0
		length_in_fragment = 0
		for sequence in sequences:
			length_total += len(sequence)
			length_in_fragment += len(sequence) % fragment_length
		if length_in_fragment * 2 > length_total:
			warnings.warn("Genome is heavily fragmented, ANI results will not be reliable.")
