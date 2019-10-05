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
	else:
		print(ani_directory + " does not exist. You must select one of full (102M), species-only (91M), or subspecies-only (11M).")
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

	parser = argparse.ArgumentParser(usage = "build_btyper3_ani_db.py -db [full, species-only, subspecies-only]")

	parser.add_argument("-db", "--database", help = "Optional argument; Specify the ANI database to download for use with FastANI (--ani_species True and/or --ani_subspecies True options): full, species-only, subspecies-only; full for 102M database with medoid genomes of 18 Bacillus cereus group genospecies, plus 2 subspecies genomes (used with --ani_species True and --ani_subspecies True); species-only for 91M database with medoid genomes of 18 Bacillus cereus group genospecies (subspecies genomes are not downloaded; used with --ani_species True and --ani_subspecies False); subspecies-only for 11M database with 2 subspecies genomes (genospecies genomes are not downloaded; used with --ani_species False and --ani_subspecies True); default = full", nargs = "?", default = "full")
	
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

if __name__ == "__main__":
        main()

