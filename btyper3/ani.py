import csv
import io
import os
import gzip
import contextlib
import importlib.resources
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
		with importlib.resources.open_text(data_module, "{}.txt".format(taxon)) as list:
			genomes = [line.split()[0] for line in list if line.strip() and not line.startswith("#")]
		# extract all the reference genomes
		for genome in genomes:
			with importlib.resources.open_binary(data_module, genome) as handle:
				reader = io.TextIOWrapper(gzip.GzipFile(fileobj=handle, mode="rb"))
				records = Bio.SeqIO.parse(reader, "fasta")
				sketch.add_draft(genome, (str(record.seq) for record in records))

		# index the references
		mapper = sketch.index()

		# query mapper with the input file
		with open(fasta) as handle:
			records = Bio.SeqIO.parse(handle, "fasta")
			sequences = [str(record.seq) for record in records]
			self.check_fragmentation(sequences, mapper.fragment_length)
			hits = mapper.query_draft(str(record.seq) for record in records)

		# make a table from the hits
		ani_results = pandas.DataFrame([
			[fasta, hit.name, hit.identity, hit.matches, hit.fragments]
			for hit in hits
		])

		# write results
		fastani_results = os.path.join(ani_results_dir, "{}_{}_fastani.txt".format(prefix, taxon))
		ani_results.to_csv(fastani_results, index=False, header=False, sep="\t")

		if not ani_results.empty:
			# extract results into a `pandas.DataFrame` object
			ani_results.sort_values(by = [2], ascending = False, inplace = True)
			maxtax = ani_results.iloc[0,1]
			maxtax = maxtax.split("/")[-1].strip()
			maxani = ani_results.iloc[0,2]

			if taxon == "species":
				species = maxtax.split("_")[1].strip()
				if species == "cereus":
					species = "cereus s.s."
				if maxani < 92.5:
					species = species + "*"
				final_species = species + "(" + str(maxani) + ")"
				return(final_species)

			elif taxon == "subspecies":
				if maxtax == "B_mosaicus_subsp_anthracis_Ames_GCF_000007845.fna.gz" and maxani >= 99.9:
					final_subspecies = "anthracis(" + str(maxani) + ")"
				elif maxtax == "B_mosaicus_subsp_cereus_AH187_GCF_000021225.fna.gz" and maxani >= 97.5:
					final_subspecies = "cereus(" + str(maxani) + ")"
				else:
					final_subspecies = "No subspecies"
				return(final_subspecies)

			elif taxon == "geneflow":
				psub = maxtax.split("_")[1].strip()
				minani = maxtax.split("_")[3].strip()
				minani = float(minani.split("-")[0].strip())
				# if the ANI value doesn't fall within the pseudo-gene flow unit ANI boundary
				if maxani < minani:
					# try the 2nd, 3rd, 4th, and 5th most similar genomes
					found_alternate = 0
					test_top5 = [1, 2, 3, 4]
					for tt in test_top5:
						testtax = ani_results.iloc[tt,1]
						testtax = testtax.split("/")[-1].strip()
						testani = ani_results.iloc[tt,2]
						test_minani = testtax.split("_")[3].strip()
						test_minani = float(test_minani.split("-")[0].strip())
						if testani >= test_minani:
							psub = testtax.split("_")[1].strip()
							found_alternate = 1
					if found_alternate == 0:
						psub = psub + "*"

				final_geneflow = psub + "(" + str(maxani) + ")"
				return(final_geneflow)

			elif taxon == "typestrains":
				maxtype = maxtax.split("_")[1].strip()
				final_typestrains = maxtype + "(" + str(maxani) + ")"
				return(final_typestrains)

		else:
			if taxon == "species":
				final_species = "(Species unknown)"
				return(final_species)
			elif taxon == "subspecies":
				final_subspecies = "No subspecies"
				return(final_subspecies)
			elif taxon == "geneflow":
				final_geneflow = "(Pseudo-gene flow unit unknown)"
				return(final_geneflow)
			elif taxon == "typestrains":
				final_typestrains = "(Type strain unknown)"
				return(final_typestrains)

	def check_fragmentation(self, sequences, fragment_length):
		length_total = 0
		length_in_fragment = 0
		for sequence in sequences:
			length_total += len(sequence)
			length_in_fragment += len(sequence) % fragment_length
		if length_in_fragment * 2 > length_total:
			warnings.warn("Genome is heavily fragmented, ANI results will not be reliable.")
