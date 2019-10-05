class FinalResults:
	"""
	Print final results file

	print_final_results
	purpose: print a final results file containing final species, subspecies, and biovar names
	input:
		final_results_directory = BTyper3 final results directory
		infile = path to file used as input
		prefix = prefix used for output files associated with a particular genome
		species = final_species string output by run_fastani in ani.py 
		subspecies = final_subspecies string output by run_fastani in ani.py
		anthracis = list of anthrax toxin genes detected in genome (anthracis produced by parse_virulence)
		emetic = list of emetic toxin genes detected in genome (emetic produced by parse_virulence)
		bt_final = list of Bt toxin genes detected in genome (bt produced by parse_bt)
	output: 
		prints final results file for query genome
		
	"""

	def __init__(self, final_results_directory, infile, prefix, species, subspecies, anthracis, emetic, bt_final):

		self.final_results_directory = final_results_directory
		self.infile = infile,
		self.prefix = prefix
		self.species = species
		self.subspecies = subspecies
		self.anthracis = anthracis
		self.emetic = emetic
		self.bt_final = bt_final

	def print_final_results(self, final_results_directory, infile, prefix, species, subspecies, anthracis, emetic, bt_final):

		header = ["#filename", "prefix", "species(ANI)", "subspecies(ANI)", "cereulide(genes)", "anthrax_toxin(genes)", "Bt(genes)", "final_taxon_names"]

		biovars = []
		if anthracis != "(Virulence factor detection not performed)" and emetic != "(Virulence factor detection not performed)":
			Anthracis = str(len(anthracis)) + "/3(" + ";".join(anthracis) + ")"
			Emeticus = str(len(emetic)) + "/4(" + ";".join(emetic) + ")"
		else:
			Anthracis = "(Virulence factor detection not performed)"
			Emeticus = "(Virulence factor detection not performed)"
		if bt_final != "(Bt toxin gene detection not performed)": 
			Thuringiensis = str(len(bt_final)) + "(" + ";".join(bt_final) + ")"
		else:
			Thuringiensis = "(Bt toxin gene detection not performed)" 
		if len(anthracis) >= 2 and anthracis != "(Virulence factor detection not performed)":
			if len(anthracis) == 3:
				biovars.append("Anthracis")
			else:
				biovars.append("Anthracis*")
		if len(emetic) >= 2 and emetic != "(Virulence factor detection not performed)":
			if len(emetic) == 4:
				biovars.append("Emeticus")
			else:
				biovars.append("Emeticus*")
		if len(bt_final) >= 1 and bt_final != "(Bt toxin gene detection not performed)":
			biovars.append("Thuringiensis")

		final_taxon = ""
		final_species = species.split("(")[0].strip()	
		final_subspecies = subspecies.split("(")[0].strip()
		final_biovars = ",".join(biovars)
		if final_subspecies == "anthracis":
			final_taxon = "B. mosaicus subsp. anthracis"
		elif final_subspecies == "cereus":
			final_taxon = "B. mosaicus subsp. cereus"
		else:
			if "*" not in final_species and len(final_species) > 0:
				final_taxon = "B. " + final_species
			else:
				final_taxon = "(Species unknown)"
		if len(biovars) > 0:
			if len(biovars) == 1:
				final_taxon = final_taxon + " biovar "
			else:
				final_taxon = final_taxon + " biovars "
			final_taxon = final_taxon + final_biovars
		if final_subspecies == "anthracis" or final_subspecies == "cereus":
			if final_subspecies == "anthracis":
				final_taxon = final_taxon + "; B. anthracis"
			elif final_subspecies == "cereus":
				final_taxon = final_taxon + "; B. cereus"
			if len(biovars) > 0:
				if len(biovars) == 1:
					final_taxon = final_taxon + " biovar "
				else:
					final_taxon = final_taxon + " biovars "
				final_taxon = final_taxon + final_biovars
		if len(biovars) > 0:
			final_taxon = final_taxon + "; B. " + final_biovars
			

		final_line = [infile, prefix, species, subspecies, Anthracis, Emeticus, Thuringiensis, final_taxon]

		with open(final_results_directory + prefix + "_final_results.txt", "a") as outfile:
			print("\t".join(header), file = outfile)
			print("\t".join(final_line), file = outfile)
