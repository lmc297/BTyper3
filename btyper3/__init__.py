#!/usr/bin/env python3

import argparse
import contextlib
import datetime
import importlib.resources
import logging
import os
import sys
import shutil
import tempfile
import urllib.request
import xml.etree.ElementTree as etree

from Bio import SeqIO

from .ani import Ani
from .blast import Blast
from .mlst import Mlst
from .print_final_results import FinalResults


def run_pipeline(args):
	"""
	run btyper3
	"""

	# get path to btyper3 executable
	btyper3_path = os.path.realpath(__file__)
	btyper3_path = btyper3_path.rpartition("/")[0].strip() + "/"

	# get input and output arguments and prefix to use for output files
	infile = args.input[0]
	prefix = infile.split("/")[-1].strip()
	prefix = ".".join(prefix.split(".")[0:-1])
	output = args.output[0]

	# add a / to output directory name, if one is not already supplied
	if not output.endswith("/"):
		output = output.strip() + "/"

	# if the output directory doesn't yet exist, make it
	if not os.path.isdir(output):
		os.mkdir(output)

	# if a btyper3_final_results directory does not exist
	# in the output directory, make it
	if not os.path.isdir(output + "btyper3_final_results"):
		os.mkdir(output + "btyper3_final_results/")

	# make a logs directory for log files
	if not os.path.isdir(output + "btyper3_final_results/logs"):
		os.mkdir(output + "btyper3_final_results/logs")

	# save path to final results directory
	final_results_directory = output + "btyper3_final_results/"

	# initialize log file
	logging.basicConfig(level = logging.DEBUG, filename = final_results_directory + "logs/" + prefix + ".log", filemode = "a+", format = "%(message)s")
	logging.getLogger().addHandler(logging.StreamHandler())


	# get arguments
	# evalue is stored as a string because it gets passed to blast command as a string
	ani_species = args.ani_species
	ani_subspecies = args.ani_subspecies
	ani_geneflow = args.ani_geneflow
	ani_typestrains = args.ani_typestrains
	fastani_path = args.fastani_path
	virulence = args.virulence
	bt = args.bt
	mlst = args.mlst
	panC = args.panC
	vdb = args.virulence_db
	vpthresh = int(args.virulence_identity)
	vqthresh = int(args.virulence_coverage)
	bpthresh = int(args.bt_identity)
	bqthresh = int(args.bt_coverage)
	overlap = float(args.bt_overlap)
	evalue = str(args.evalue)
	download_mlst_latest = args.download_mlst_latest

	# log to file
	now = datetime.datetime.now
	logging.info("Welcome to BTyper3!")
	logging.info("You are initializing this run at " + now().strftime("%Y-%m-%d %H:%M"))
	logging.info("You ran the following command: ")
	logging.info(" ".join([str(sa) for sa in sys.argv]))
	logging.info("Report bugs/concerns to Laura M. Carroll, laura.carroll@embl.de")


	# perform species and/or supspecies assignment
	if ani_species == "True" or ani_subspecies == "True" or ani_geneflow == "True" or ani_typestrains == "True":

		if ani_species == "True":

			get_species = Ani(
				taxon = "species",
				fastani_path = fastani_path,
				fasta = infile,
				final_results_directory = final_results_directory,
				prefix = prefix)

			logging.info("Using FastANI to assign " + prefix + " to a species at " + now().strftime("%Y-%m-%d %H:%M"))
			final_species = get_species.run_fastani("species", fastani_path, infile, final_results_directory, prefix)
			logging.info("Finished species assignment of " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

		else:

			final_species = "(Species assignment not performed)"

		if ani_subspecies == "True":

			get_subspecies = Ani(
				taxon = "subspecies",
				fastani_path = fastani_path,
				fasta = infile,
				final_results_directory = final_results_directory,
				prefix = prefix)

			logging.info("Using FastANI to assign " + prefix + " to a subspecies (if applicable) at " + now().strftime("%Y-%m-%d %H:%M"))
			final_subspecies = get_subspecies.run_fastani("subspecies", fastani_path, infile, final_results_directory, prefix)
			logging.info("Finished subspecies assignment of " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

		else:

			final_subspecies = "(Subspecies assignment not performed)"

		if ani_geneflow == "True":

			get_geneflow = Ani(
				taxon = "geneflow",
				fastani_path = fastani_path,
				fasta = infile,
				final_results_directory = final_results_directory,
				prefix = prefix)

			logging.info("Using FastANI to assign " + prefix + " to a pseudo-gene flow unit at " + now().strftime("%Y-%m-%d %H:%M"))
			final_geneflow = get_geneflow.run_fastani("geneflow", fastani_path, infile, final_results_directory, prefix)
			logging.info("Finished pseudo-gene flow unit assignment of " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

		else:

			final_geneflow = "(Pseudo-gene flow unit assignment not performed)"

		if ani_typestrains == "True":

			get_typestrains = Ani(
				taxon = "typestrains",
				fastani_path = fastani_path,
				fasta = infile,
				final_results_directory = final_results_directory,
				prefix = prefix)

			logging.info("Using FastANI to compare " + prefix + " to B. cereus s.l. species type strain genomes at " + now().strftime("%Y-%m-%d %H:%M"))
			final_typestrains = get_typestrains.run_fastani("typestrains", fastani_path, infile, final_results_directory, prefix)
			logging.info("Finished B. cereus s.l. species type strain comparison of " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

		else:

			final_typestrains = "(Type strain-based taxonomic assignment not performed)"

	else:

		final_species = "(Species assignment not performed)"
		final_subspecies = "(Subspecies assignment not performed)"
		final_geneflow = "(Pseudo-gene flow unit assignment not performed)"
		final_typestrains = "(Type strain-based taxonomic assignment not performed)"



	# perform virulence-associated biovar assignment
	if virulence == "True":

		if vdb == "aa":
			vdb_name = "btyper3_virulence_sequences.faa"
			vdb_task = "tblastn"

		elif vdb == "nuc":
			vdb_name = "btyper3_virulence_sequences.ffn"
			vdb_task = "blastn"


		with importlib.resources.path("btyper3.seq_virulence_db", vdb_name) as vdb_path:

			get_virulence = Blast(
				task = vdb_task,
				dbseqs = infile,
				fasta = vdb_path,
				final_results_directory = final_results_directory,
				prefix = prefix,
				suffix = "virulence",
				pthresh = vpthresh,
				qthresh = vqthresh,
				overlap = overlap,
				evalue = evalue)

			logging.info("Using " + vdb_task + " to identify potential virulence factors in " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

			vir = get_virulence.run_blast(vdb_task, infile, vdb_path, final_results_directory, prefix, "virulence", evalue)
			anthracis, emetic, nhe, hbl, cytK, sph, cap, has, bps = get_virulence.parse_virulence(vir, vpthresh, vqthresh)

			logging.info("Finished virulence factor detection in " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))


	else:

		anthracis = "(Virulence factor detection not performed)"
		emetic = "(Virulence factor detection not performed)"
		nhe = "(Virulence factor detection not performed)"
		hbl = "(Virulence factor detection not performed)"
		cytK = "(Virulence factor detection not performed)"
		sph = "(Virulence factor detection not performed)"
		cap = "(Virulence factor detection not performed)"
		has = "(Virulence factor detection not performed)"
		bps = "(Virulence factor detection not performed)"



	# perform Thuringiensis biovar assignment
	if bt == "True":

		with importlib.resources.path("btyper3.seq_bt_db", "btyper3_bt_sequences.faa") as bt_path:

			get_bt = Blast(
				task = "tblastn",
				dbseqs = infile,
				fasta = bt_path,
				final_results_directory = final_results_directory,
				prefix = prefix,
				suffix = "bt",
				pthresh = bpthresh,
				qthresh = bqthresh,
				overlap = overlap,
				evalue = evalue)

			logging.info("Using tblastn to identify potential Bt genes in " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

			bt_results = get_bt.run_blast("tblastn", infile, bt_path, final_results_directory, prefix, "bt", evalue)
			bt_final = get_bt.parse_bt(bt_results, bpthresh, bqthresh, overlap)

			logging.info("Finished Bt toxin gene detection for " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))


	else:

		bt_final = "(Bt toxin gene detection not performed)"




	# perform multi-locus sequence typing (MLST) using PubMLST's seven-gene scheme for Bacillus cereus
	if mlst == "True":

		with contextlib.ExitStack() as ctx:

			if download_mlst_latest == "True":

				logging.info("Downloading most recent PubMLST datbase at " + now().strftime("%Y-%m-%d %H:%M"))
				with urllib.request.urlopen("https://pubmlst.org/data/dbases.xml") as req:
					tree = etree.parse(req)
					parent = next(e for e in tree.iter("species") if e.text.strip() == "Bacillus cereus")
					urls = (e.text for e in parent.iter("url"))

				mlst_file = ctx.enter_context(tempfile.NamedTemporaryFile(suffix=".fas", mode="wb", buffering=0))
				bcereus_file = ctx.enter_context(tempfile.NamedTemporaryFile(suffix=".txt", mode="wb", buffering=0))
				mlst_path = mlst_file.name
				bcereus_path = bcereus_file.name

				for url in urls:
					if "alleles_fasta" in url:
						with urllib.request.urlopen(url) as req:
							shutil.copyfileobj(req, mlst_file)
					elif "profiles_csv" in url:
						with urllib.request.urlopen(url) as req:
							shutil.copyfileobj(req, bcereus_file)

				logging.info("Finished downloading most recent PubMLST datbase at " + now().strftime("%Y-%m-%d %H:%M"))

			else:

				db_time = importlib.resources.read_text("btyper3.seq_mlst_db", "timestamp.txt").strip()
				logging.info("Using local PubMLST database (downloaded at {})".format(db_time))

				mlst_path = ctx.enter_context(importlib.resources.path("btyper3.seq_mlst_db", "mlst.fas"))
				bcereus_path = ctx.enter_context(importlib.resources.path("btyper3.seq_mlst_db", "bcereus.txt"))


			get_mlst = Blast(
				task = "blastn",
				dbseqs = infile,
				fasta = mlst_path,
				final_results_directory = final_results_directory,
				prefix = prefix,
				suffix = "mlst",
				pthresh = 0,
				qthresh = 0,
				overlap = overlap,
				evalue = evalue)

			logging.info("Using blastn to identify potential seven-gene MLST genes in " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

			mlst_results = get_mlst.run_blast("blastn", infile, mlst_path, final_results_directory, prefix, "mlst", evalue)
			mlst_alleles, perfect_matches = get_mlst.parse_mlst(mlst_results)

			logging.info("Finished seven-gene MLST gene detection for " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

			get_st = Mlst(
				alleles = mlst_alleles,
				profiles = bcereus_path,
				perfect_matches = perfect_matches,
				final_results_directory = final_results_directory,
				prefix = prefix)


			mlst_final = get_st.at2st(mlst_alleles, bcereus_path, perfect_matches, final_results_directory, prefix)


	else:

		mlst_final = "(Seven-gene MLST not performed)"



	# perform panC phylogenetic group assignment using the adjusted, eight-group panC group assignment scheme
	if panC == "True":

		with importlib.resources.path("btyper3.seq_panC_db", "panC.fna") as panC_path:

			get_panC = Blast(
				task = "blastn",
				dbseqs = infile,
				fasta = panC_path,
				final_results_directory = final_results_directory,
				prefix = prefix,
				suffix = "panC",
				pthresh = 0,
				qthresh = 0,
				overlap = overlap,
				evalue = evalue)

			logging.info("Using blastn to identify panC in " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))

			panC_results = get_panC.run_blast("blastn", infile, panC_path, final_results_directory, prefix, "panC", evalue)
			panC_final = get_panC.parse_panC(panC_results)
			logging.info("Finished panC gene detection for " + prefix + " at " + now().strftime("%Y-%m-%d %H:%M"))


	else:

		panC_final = "(panC group assignment not performed)"



	# print results to a final results file
	get_final_results = FinalResults(
		final_results_directory = final_results_directory,
		infile = infile,
		prefix = prefix,
		species = final_species,
		subspecies = final_subspecies,
		geneflow = final_geneflow,
		typestrains = final_typestrains,
		anthracis = anthracis,
		emetic = emetic,
		nhe = nhe,
		hbl = hbl,
		cytK = cytK,
		sph = sph,
		cap = cap,
		has = has,
		bps = bps,
		bt_final = bt_final,
		mlst_final = mlst_final,
		panC_final = panC_final)

	get_final_results.print_final_results(final_results_directory, infile, prefix, final_species, final_subspecies, final_geneflow, final_typestrains, anthracis, emetic, nhe, hbl, cytK, sph, cap, has, bps, bt_final, mlst_final, panC_final)

	for blastdb_ext in ("nsq", "nin", "nhr"):
		blastdb_file = "{}.{}".format(infile, blastdb_ext)
		if os.path.isfile(blastdb_file):
			os.remove(blastdb_file)

	logging.info("")
	logging.info("")
	logging.info("")
	logging.info("BTyper3 finished at " + now().strftime("%Y-%m-%d %H:%M"))
	logging.info("Report bugs/concerns to Laura M. Carroll, laura.carroll@embl.de\n")
	logging.info("Have a nice day!")



def main():

	# BTyper3 arguments

	parser = argparse.ArgumentParser(usage = "btyper3 -i </path/to/genome.fasta> -o </path/to/output/directory/> [other options]")

	parser.add_argument("-i", "--input", help = "Path to input genome in fasta format", nargs = 1, required = True)

	parser.add_argument("-o", "--output", help = "Path to desired output directory", nargs = 1, required = True)

	parser.add_argument("--ani_species", help = "Optional argument; True or False; assign genome to a species using FastANI; default = True", nargs = "?", default = "True")

	parser.add_argument("--ani_subspecies", help = "Optional argument; True or False; assign genome to a subspecies, if relevant, using FastANI; default = True", nargs = "?", default = "True")

	parser.add_argument("--ani_geneflow", help = "Optional argument; True or False; assign genome to a pseudo-gene flow unit using the method described by Carroll, et al. using FastANI; default = False", nargs = "?", default = "False")

	parser.add_argument("--ani_typestrains", help = "Optional argument; True or False; calculate ANI values between the query genome relative to all B. cereus s.l. species type strain genomes using FastANI, and report the closest species type strain/highest ANI value; default = False", nargs = "?", default = "False")

	parser.add_argument("--fastani_path", help = "Optional argument for use with --ani_species True and/or --ani_subspecies True and/or --ani_geneflow True; fastANI, unless path to fastANI executable is supplied; path to fastANI; default = fastANI <fastANI is in the user's path>", nargs = "?", default = "fastANI")

	parser.add_argument("--virulence", help = "Optional argument; True or False; perform virulence gene detection (required if one wants to assign genomes to biovars Anthracis or Emeticus); default = True", nargs = "?", default = "True")

	parser.add_argument("--bt", help = "Optional argument; True or False; perform Bt toxin gene detection for cry, cyt, and vip genes (required if one wants to assign genomes to biovar Thuringiensis); default = True", nargs = "?", default = "True")

	parser.add_argument("--mlst", help = "Optional argument; True or False; assign genome to a sequence type (ST) using the seven-gene multi-locus sequence typing (MLST) scheme available in PubMLST; default = True", nargs = "?", default = "True")

	parser.add_argument("--panC", help = "Optional argument; True or False; assign genome to a phylogenetic group (Group I-VIII) using an adjusted, eight-group panC group assignment scheme; default = True", nargs = "?", default = "True")

	parser.add_argument("--virulence_db", help = "Optional argument for use with --virulence True; aa or nuc; database to use for virulence factor detection: aa for the amino acid sequence database, or nuc for the nucleotide sequence database; option aa uses translated nucleotide blast and allows for the detection of more remote homologs, but is slower than nuc, which uses blastn; default = aa", nargs = "?", default = "aa")

	parser.add_argument("--virulence_identity", help = "Optional argument for use with --virulence True; integer from 0 to 100; minimum percent amino acid/nucleotide identity threshold for a virulence gene to be considered present, depending on choice of --virulence_db aa or nuc, respectively; default = 70", nargs = "?", default = 70)

	parser.add_argument("--virulence_coverage", help = "Optional argument for use with --virulence True; integer from 0 to 100; minimum percent coverage threshold for a virulence gene to be considered present; default = 80", nargs = "?", default = 80)

	parser.add_argument("--bt_identity", help = "Optional argument for use with --bt True; integer from 0 to 100; minimum percent amino acid identity threshold for a Bt toxin gene to be considered present; default = 50", nargs = "?", default = 50)

	parser.add_argument("--bt_coverage", help = "Optional argument for use with --bt True; integer from 0 to 100; minimum percent coverage threshold for a Bt toxin gene to be considered present; default = 70", nargs = "?", default = 70)

	parser.add_argument("--bt_overlap", help = "Optional argument for use with --bt True; float from 0 to 1; specify maximum proportion of overlap for overlapping Bt toxin genes to be considered separate genes; Bt toxin genes below this threshold will be considered separate, while those above it will be considered overlapping, and only the top hit will be reported; default=0.7", nargs = "?", default = 0.7)

	parser.add_argument("--evalue", help = "Optional argument for use with --virulence True and/or --bt True; float >= 0; maximum blast e-value for a hit to be saved; note that if both --virulence True and --bt True, this e-value threshold will be applied to both analyses; default = 1e-5", nargs = "?", default = 1e-5)

	parser.add_argument("--download_mlst_latest", help = "Optional argument for use with --mlst True; True or False; download the latest version of the seven-gene multi-locus sequence typing (MLST) scheme available in PubMLST; if this is False, BTyper3 will search for the appropriate files in the seq_mlst_db directory; default = False", nargs = "?", default = "False")

	parser.add_argument("--version", action="version", version='%(prog)s 3.2.0', help="Print version")

	args = parser.parse_args()

	run_pipeline(args)

if __name__ == "__main__":

	# run BTyper3

	main()
