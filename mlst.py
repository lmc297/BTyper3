import os
import pandas as pd
import numpy as np
from pandas.errors import EmptyDataError
import itertools

class Mlst:
	"""
	Use multi-locus sequence typing (MLST) to assign genome to sequence type (ST)

	at2st
	purpose: selects most likely ST from a list of allelic types (ATs)
	input:
		alleles = list of detected best-matching alleles, ordered alphabetically
		profiles = file containing profiles for each gene and the resulting ST
		perfect_matches = number of alleles which perfectly matched database (produced by parse_mlst in blast.py)
		final_results_directory = path to BTyper3 final results directory
		prefix = genome prefix to use for output files
	output:
		predicted ST corresponding to best-matching alleles
	
	"""


	def __init__(self, alleles, profiles, perfect_matches, final_results_directory, prefix):

		self.alleles = alleles
		self.profiles = profiles
		self.perfect_matches = perfect_matches
		self.final_results_directory = final_results_directory
		self.prefix = prefix


	def at2st(self, alleles, profiles, perfect_matches, final_results_directory, prefix):

		if len(alleles) == 7:
			final = []	
			profiles = pd.read_csv(profiles, sep = "\t", header = 0)	
			alleles = list(itertools.product(*alleles))
			for allele in alleles:
				st_rows = profiles[(profiles.glp == int(allele[0])) & (profiles.gmk == int(allele[1])) & (profiles.ilv == int(allele[2])) & (profiles.pta == int(allele[3])) & (profiles.pur == int(allele[4])) & (profiles.pyc == int(allele[5])) & (profiles.tpi == int(allele[6]))]	
				if st_rows.shape[0] > 0:
					if str(st_rows["clonal_complex"].iloc[0]) == "nan":
						cc = "No clonal complex"
					else:
						cc = str(st_rows["clonal_complex"].iloc[0])
					final.append(str(st_rows["ST"].iloc[0]) + "[" + cc + "](" + str(perfect_matches) + "/7)")
			if len(final) > 0:
				final = final
			else:
				final = ["Unknown(unknown ST)"]
		else:
			final = ["Unknown(missing alleles)"]

		return(";".join(final))
