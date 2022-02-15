import os
import contextlib
import importlib.resources
import subprocess
import tempfile

import pandas as pd
import numpy as np
from pandas.errors import EmptyDataError

class Ani:
	"""
	Use ANI to assign genome to genospecies and/or subspecies

	run_fastani
	purpose: runs fastANI for species/subspecies assignment and selects match with highest ANI
	input:
		taxon = "species", "subspecies", or "geneflow"; corresponds to directory of genomes to use
		fastani_path = path to fastANI executable
		fasta = query genome for fastANI
		final_results_directory = path to BTyper3 final results directory
		prefix = genome prefix to use for output files
	output:
		species or subspecies producing highest ANI value

	"""

	def __init__(self, taxon, fastani_path, fasta, final_results_directory, prefix):

		self.taxon = taxon
		self.fastani_path = fastani_path
		self.fasta = fasta
		self.final_results_directory = final_results_directory
		self.prefix = prefix

	def run_fastani(self, taxon, fastani_path, fasta, final_results_directory, prefix):
		# create output folder if it doesn't exist
		ani_results_dir = os.path.join(final_results_directory, taxon)
		os.makedirs(ani_results_dir, exist_ok=True)

		# get the ANI database using `importlib.resources`: note that since
		# files may not be available on the local filesystem (e.g. they could
		# be zipped), we use `importlib.resources.path` to get a system path
		# for each of them than can be passed to `fastANI`.
		with contextlib.ExitStack() as ctx:
			# create a temporary file to list the reference genomes
			ref_file = ctx.enter_context(tempfile.NamedTemporaryFile(suffix="txt", mode="w"))
			# extract the list of reference genomes
			data_module = "btyper3.seq_ani_db.{}".format(taxon)
			with importlib.resources.open_text(data_module, "{}.txt".format(taxon)) as list:
				genomes = [line.split()[0] for line in list if line.strip() and not line.startswith("#")]
			# extract all the reference genomes
			for genome in genomes:
				fna_path = ctx.enter_context(importlib.resources.path(data_module, genome))
				ref_file.write("{}\n".format(fna_path))
			ref_file.flush()
			# run fastANI
			fastani_results = os.path.join(ani_results_dir, "{}_{}_fastani.txt".format(prefix, taxon))
			proc = subprocess.run([fastani_path, "-q", fasta, "--rl", ref_file.name, "-o", fastani_results])
			proc.check_returncode()

		try:
			# extract results into a `pandas.DataFrame` object
			ani_results_file = pd.read_csv(fastani_results, sep = "\s+", header = None)
			ani_results_file.sort_values(by = [2], ascending = False, inplace = True)
			maxtax = ani_results_file.iloc[0,1]
			maxtax = maxtax.split("/")[-1].strip()
			maxani = ani_results_file.iloc[0,2]

			if taxon == "species":
				species = maxtax.split("_")[1].strip()
				if species == "cereus":
					species = "cereus s.s."
				if maxani < 92.5:
					species = species + "*"
				final_species = species + "(" + str(maxani) + ")"
				return(final_species)

			elif taxon == "subspecies":
				if maxtax == "B_mosaicus_subsp_anthracis_Ames_GCF_000007845.fna" and maxani >= 99.9:
					final_subspecies = "anthracis(" + str(maxani) + ")"
				elif maxtax == "B_mosaicus_subsp_cereus_AH187_GCF_000021225.fna" and maxani >= 97.5:
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
						testtax = ani_results_file.iloc[tt,1]
						testtax = testtax.split("/")[-1].strip()
						testani = ani_results_file.iloc[tt,2]
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

		except EmptyDataError:
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
