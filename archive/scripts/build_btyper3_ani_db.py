#!/usr/bin/env python3

import sys, os, argparse
from urllib.request import urlopen

def get_args(args):

	ani_directory = args.database
	ani_directory = ani_directory.strip()
	if ani_directory == "subspecies-only":
		ani_size = "11M"
	elif ani_directory == "species-only":
		ani_size = "91M"
	elif ani_directory == "full":
		ani_size = "102M"
	elif ani_directory == "geneflow-only":
		ani_size = "198M"
	elif ani_directory == "typestrains-only":
		ani_size = "138M"
	else:
		print(ani_directory + " does not exist. You must select one of full (102M), species-only (91M), subspecies-only (11M), geneflow-only (198M), or typestrains-only (138M).")
		print("Exiting...")
		sys.exit()
	print("You specified the '" + ani_directory + "' ANI database. This database will take up " + ani_size + " of space on your computer. Do you want to continue? Type 'yes' and press ENTER to download the " + ani_directory + " database, or type any other key and press ENTER to exit without downloading the database.")
	newmm = input("Do you want to download the " + ani_directory + " ANI database (" + ani_size + ")?: ")
	if newmm.replace("'","").replace('"',"").strip()!="yes":
		print("Exiting...")
		sys.exit()
	else:
		return(ani_directory)
				

def get_btyper_path():

	btyper_path = os.path.realpath(__file__)
	btyper_path = btyper_path.rpartition("/")[0].strip()+"/"
	return(btyper_path)


def download_genomes(btyper_path, genome_list, ani_directory):

	glist = open(genome_list, "r")
	for line in glist:
		if not line.startswith("#"):
			gname = line.split("\t")[0].strip()
			gpath = line.split("\t")[1].strip()
			if not os.path.isfile(btyper_path + "seq_ani_db/" + ani_directory + "/" +  gname):
				# read file in chunks
				# courtesy of Alex Martelli: https://stackoverflow.com/questions/1517616/stream-large-binary-files-with-urllib2-to-file
				response = urlopen(gpath)
				chunk_size = 16 * 1024
				print("Downloading " + gname + "...")
				with open(btyper_path + "seq_ani_db/" + ani_directory + "/" + gname + ".gz", "wb") as f:
					while True:
						chunk = response.read(chunk_size)
						if not chunk:
							break
						f.write(chunk)
				os.system("gunzip " + btyper_path + "seq_ani_db/" + ani_directory + "/" + gname)
				with open(btyper_path + "seq_ani_db/" + ani_directory + "/fastani_references_" + ani_directory + ".txt", "a") as outfile:
					print(btyper_path + "seq_ani_db/" + ani_directory + "/" + gname, file = outfile)	

def main():

	parser = argparse.ArgumentParser(usage = "build_btyper3_ani_db.py -db [full, species-only, subspecies-only, geneflow-only, typestrains-only]")

	parser.add_argument("-db", "--database", help = "Optional argument; Specify the ANI database to download for use with FastANI (--ani_species True and/or --ani_subspecies True and/or --ani_geneflow True and/or --ani_typestrains True options): full, species-only, subspecies-only, geneflow-only, typestrains-only; full for 102M database with medoid genomes of 18 Bacillus cereus group genomospecies, plus 2 subspecies genomes (used with --ani_species True and --ani_subspecies True); species-only for 91M database with medoid genomes of 18 Bacillus cereus group genomospecies (subspecies genomes are not downloaded; used with --ani_species True and --ani_subspecies False); subspecies-only for 11M database with 2 subspecies genomes (genomospecies genomes are not downloaded; used with --ani_species False and --ani_subspecies True); geneflow-only for the 198M database with 37 genomes (used for pseudo-gene flow unit assignment with --ani_geneflow True); typestrains-only for the 138M database with 26 genomes (used for ANI-based type strain comparison via --ani_typestrains True); default = full", nargs = "?", default = "full")
	
	btyper_path = get_btyper_path()

	args = parser.parse_args()
	
	ani_directory = get_args(args)	
	
	if ani_directory == "full":
		genome_list = btyper_path + "seq_ani_db/species/species.txt"
		download_genomes(btyper_path, genome_list, "species")
		genome_list = btyper_path + "seq_ani_db/subspecies/subspecies.txt"
		download_genomes(btyper_path, genome_list, "subspecies")
	elif ani_directory == "species-only":
		genome_list = btyper_path + "seq_ani_db/species/species.txt"
		download_genomes(btyper_path, genome_list, "species")
	elif ani_directory == "subspecies-only":
		genome_list = btyper_path + "seq_ani_db/subspecies/subspecies.txt"
		download_genomes(btyper_path, genome_list, "subspecies")
	elif ani_directory == "geneflow-only":
		genome_list = btyper_path + "seq_ani_db/geneflow/geneflow.txt"
		download_genomes(btyper_path, genome_list, "geneflow")
	elif ani_directory == "typestrains-only":
		genome_list = btyper_path + "seq_ani_db/typestrains/typestrains.txt"
		download_genomes(btyper_path, genome_list, "typestrains")

if __name__ == "__main__":
        main()

