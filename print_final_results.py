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
		geneflow = final_geneflow string output by run_fastani in ani.py
		typestrains = final_typestrains string output by run_fastani in ani.py
		anthracis = list of anthrax toxin genes detected in genome (anthracis produced by parse_virulence)
		emetic = list of emetic toxin genes detected in genome (emetic produced by parse_virulence)
		nhe = list of Nhe-encoding genes detected in genome (nhe produced by parse_virulence)
		hbl = list of Hbl-encoding genes detected in genome (hbl produced by parse_virulence)
		cytK = list containing top hit of either cytK-1 or cytK-2, if detected (cytK produced by parse_virulence)
		sph = list containing Sph encoding gene, if detected (sph produced by parse_virulence)
		cap = list containing Cap capsular genes detected in genome (cap produced by parse_virulence)
		has = list containing Has-encoding genes detected in genome (has produced by parse_virulence)
		bps = list containing Bps-encoding genes detected in genome (bps produced by parse_virulence)
		bt_final = list of Bt toxin genes detected in genome (bt produced by parse_bt)
		mlst_final = list of prediced STs/clonal complexes (mlst_final produced by at2st)
		panC_final = predicted panC group (panC_final produced by parse_panC)
	output: 
		prints final results file for query genome
		
	"""

	def __init__(self, final_results_directory, infile, prefix, species, subspecies, geneflow, typestrains, anthracis, emetic, nhe, hbl, cytK, sph, cap, has, bps, bt_final, mlst_final, panC_final):

		self.final_results_directory = final_results_directory
		self.infile = infile,
		self.prefix = prefix
		self.species = species
		self.subspecies = subspecies
		self.geneflow = geneflow
		self.typestrains = typestrains
		self.anthracis = anthracis
		self.emetic = emetic
		self.nhe = nhe
		self.hbl = hbl
		self.cytK = cytK
		self.sph = sph
		self.cap = cap
		self.has = has
		self.bps = bps
		self.bt_final = bt_final
		self.mlst_final = mlst_final
		self.panC_final = panC_final

	def print_final_results(self, final_results_directory, infile, prefix, species, subspecies, geneflow, typestrains, anthracis, emetic, nhe, hbl, cytK, sph, cap, has, bps, bt_final, mlst_final, panC_final):

		header = ["#filename", "prefix", "species(ANI)", "subspecies(ANI)", "Pseudo_Gene_Flow_Unit(ANI)", "Closest_Type_Strain(ANI)", "anthrax_toxin(genes)", "emetic_toxin_cereulide(genes)", "diarrheal_toxin_Nhe(genes)", "diarrheal_toxin_Hbl(genes)", "diarrheal_toxin_CytK(top_hit)", "sphingomyelinase_Sph(gene)", "capsule_Cap(genes)", "capsule_Has(genes)", "capsule_Bps(genes)", "Bt(genes)", "PubMLST_ST[clonal_complex](perfect_matches)", "Adjusted_panC_Group(predicted_species)", "final_taxon_names"]

		biovars = []
		if anthracis != "(Virulence factor detection not performed)" and emetic != "(Virulence factor detection not performed)":
			Anthracis = str(len(anthracis)) + "/3(" + ";".join(sorted(anthracis)) + ")"
			Emeticus = str(len(emetic)) + "/4(" + ";".join(sorted(emetic)) + ")"
			Nhe = str(len(nhe)) + "/3(" + ";".join(sorted(nhe)) + ")"
			Hbl = str(len(hbl)) + "/4(" + ";".join(sorted(hbl)) + ")"
			CytK = str(len(cytK)) + "/1(" + ";".join(cytK) + ")"
			Sph = str(len(sph)) + "/1(" + ";".join(sph) + ")"
			Cap = str(len(cap)) + "/5(" + ";".join(sorted(cap)) + ")"
			Has = str(len(has)) + "/3(" + ";".join(sorted(has)) + ")"
			Bps = str(len(bps)) + "/9(" + ";".join(sorted(bps)) + ")"

		else:
			Anthracis = "(Virulence factor detection not performed)"
			Emeticus = "(Virulence factor detection not performed)"
			Nhe = "(Virulence factor detection not performed)"
			Hbl = "(Virulence factor detection not performed)"
			CytK = "(Virulence factor detection not performed)"
			Sph = "(Virulence factor detection not performed)"
			Cap = "(Virulence factor detection not performed)"
			Has = "(Virulence factor detection not performed)"
			Bps = "(Virulence factor detection not performed)"

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
			

		final_line = [infile, prefix, species, subspecies, geneflow, typestrains, Anthracis, Emeticus, Nhe, Hbl, CytK, Sph, Cap, Has, Bps, Thuringiensis, mlst_final, panC_final, final_taxon]

		with open(final_results_directory + prefix + "_final_results.txt", "a") as outfile:
			print("\t".join(header), file = outfile)
			print("\t".join(final_line), file = outfile)
