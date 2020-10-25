#!/usr/bin/env python3

import sys, os, argparse, datetime, requests
import xml.etree.ElementTree as ET




def get_btyper3_path():

	btyper3_path = os.path.realpath(__file__)
	btyper3_path = btyper3_path.rpartition("/")[0].strip()+"/"
	return(btyper3_path)




def download_pubmlst(btyper3_path):
	
	now = datetime.datetime.now()
	print("Downloading most recent PubMLST datbase at " + now.strftime("%Y-%m-%d %H:%M"))
	
	url = "https://pubmlst.org/data/dbases.xml"
	resp = requests.get(url)
	xml = btyper3_path + "seq_mlst_db/pubmlst.xml"
	with open(xml, "wb") as f:
		f.write(resp.content)
		tree=ET.parse(xml)
		root=tree.getroot()
		species={}
		for parent in root.iter("species"):
			species[parent.text.strip()]=[]
			for child in parent.iter("url"):
				species[parent.text.strip()].append(child.text)

		urlcol = species["Bacillus cereus"]

		for u in urlcol:
	

			if "alleles_fasta" in u:
				fname = u.split("/")[-2].strip()
				resp = requests.get(u)
				with open(btyper3_path + "seq_mlst_db/mlst.fas", "ab") as outfile:
					outfile.write(resp.content)

			elif "profiles_csv" in u:
				fname = "bcereus.txt"
				resp = requests.get(u)
				with open(btyper3_path + "seq_mlst_db/" + fname, "wb") as outfile:
					outfile.write(resp.content)

			
	print("Finished downloading most recent PubMLST datbase at " + now.strftime("%Y-%m-%d %H:%M"))




def main():

	parser = argparse.ArgumentParser(usage = "build_btyper3_ani_db.py")
	
	btyper3_path = get_btyper3_path()

	args = parser.parse_args()

	download_pubmlst(btyper3_path)

	



if __name__ == "__main__":
        main()
