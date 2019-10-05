import os
import pandas as pd
from pandas.errors import EmptyDataError

class Blast:
	"""
	Detect genes with blast

	run_blast
	purpose:
		blast a query against a reference and save results to a text file
	input:
		task = blast algorithm to use (e.g., tblastn)
		dbseqs = blast database fasta file
		fasta = blast query fasta file
		final_results_directory = BTyper3 final results directory
		prefix = genome prefix for output files
		suffix = suffix for output files corresponding to BTyper3 task (e.g., bt, virulence)
		pthresh = minimum percent identity threshold for blast hits
		qthresh = minimum percent query coverage for blast hits
		overlap = maximum proportion of overlap for overlapping blast hits to be considered separate (hits overlapping below this threshold will be considered separate hits)
		evalue = maximum blast e-value for blast hits

	output:
		path to blast output file of results

	parse_virulence
	purpose:
		assign query genome to virulence-associated biovars, using blast results from run_blast
	input:
		virfile = path to run_blast results file containing virulence gene hits
		pthresh = minimum percent identity threshold for blast hits
		qthresh = minimum percent query coverage for blast hits
	output:
		lists of virulence genes detected for each virulence-associated biovar

	parse_bt
	purpose:
		assign query genome to biovar Thuringiensis or not, using blast results from run_blast
	input:
		btfile = path to blast results file containing Bt toxin gene hits
		pthresh = minimum percent identity threshold for blast hits
		qthresh = minimum percent query coverage for blast hits
		overlap = maximum proportion of overlap for overlapping Bt toxin genes to be considered separate genes
			Bt toxin genes below this threshold will be considered separate, while those above it will be considered overlapping, and only the top hit will be reported
	output:
		a sorted list of Bt genes detected in a sequence
	"""

	def __init__(self, task, dbseqs, fasta, final_results_directory, prefix, suffix, pthresh, qthresh, overlap, evalue):

		self.task = task
		self.dbseqs = dbseqs
		self.fasta = fasta
		self.final_results_directory = final_results_directory
		self.prefix = prefix
		self.suffix = suffix
		self.pthresh = pthresh
		self.qthresh = qthresh
		self.overlap = overlap
		self.evalue = evalue

	def run_blast(self, task, dbseqs, fasta, final_results_directory, prefix, suffix, evalue):

		blast_results_dir = final_results_directory + suffix
		if not os.path.isdir(blast_results_dir):
			os.mkdir(blast_results_dir)

		if not os.path.exists(dbseqs + ".nsq"):
			os.system("makeblastdb -in " + dbseqs + " -dbtype nucl")
	
		cmd = '{3} -query {0} -db {1} -out {2} -max_target_seqs 1000000000 -evalue {4} -outfmt "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen slen qcovs qcovhsp"'.format(fasta, dbseqs, blast_results_dir + "/" + prefix + "_" + suffix + ".txt", task, evalue) # genome as query and mlst db as db	
		os.system(cmd)

		return(blast_results_dir + "/" + prefix + "_" + suffix + ".txt")

	def parse_virulence(self, virfile, pthresh, qthresh):

		try:

			blast_results_file = pd.read_csv(virfile, sep = "\s+", header = None)
			blast_results_file = blast_results_file.sort_values(by = [0], ascending = True) # genome as query and mlst db as db
			genes = blast_results_file.iloc[:,0] # genome as db and mlst db as query

			emetic = []
			anthracis = []
			genes = genes.unique()
			for gene in genes:
				gene_subset = blast_results_file[blast_results_file[0].str.contains(gene)] # genome as query and mlst db as db
				gene_subset = gene_subset.sort_values(by = [11], ascending = False)
				max_gene = gene_subset.iloc[0,0]
				pid = float(gene_subset.iloc[0,2])
				qid = float(gene_subset.iloc[0,14])	
				#qid = 100*(float(gene_subset.iloc[0,3])/float(gene_subset.iloc[0,12])) # original BTyper query coverage value; genome as db and mlst db as query
				if pid >= pthresh and qid >= qthresh:
					if max_gene == "cesA" or max_gene == "cesB" or max_gene == "cesC" or max_gene == "cesD":
						emetic.append(max_gene)
					if max_gene == "cya" or max_gene == "lef" or max_gene == "pagA":
						anthracis.append(max_gene)

		except EmptyDataError:

			anthracis = []
			emetic = []	

		return(anthracis, emetic)				


	
	def parse_bt(self, btfile, pthresh, qthresh, overlap):

		try:

			blast_results_file = pd.read_csv(btfile, sep = "\s+", header = None)
			blast_results_file = blast_results_file.sort_values(by = [0], ascending = True) # genome as query and mlst db as db
			genes = blast_results_file.iloc[:,0] # genome as db and mlst db as query
	
			rangedict = {}
			bitdict = {}
			genes = genes.unique()
			for gene in genes:
				gene_subset = blast_results_file[blast_results_file[0].str.contains(gene)] # genome as query and mlst db as db
				gene_subset = gene_subset.sort_values(by = [11], ascending = False)
				max_gene = gene_subset.iloc[0,0]
				pid = float(gene_subset.iloc[0,2])
				qid = float(gene_subset.iloc[0,14])	
				#qid = 100*(float(gene_subset.iloc[0,3])/float(gene_subset.iloc[0,12])) # original BTyper query coverage value; genome as db and mlst db as query
				glen = float(gene_subset.iloc[0,3])
				gstart = int(gene_subset.iloc[0,8])
				gend = int(gene_subset.iloc[0,9])
				if gstart < gend:
					grange = list(range(gstart, gend + 1))
				elif gend < gstart:
					grange = list(range(gend, gstart + 1))
				if pid >= pthresh and qid >= qthresh:
					rangedict[max_gene] = grange
					bitdict[max_gene] = float(gene_subset.iloc[0,11])
		

			bt = []
			#comparisons = []
			for key, val in rangedict.items():
				overlap_dict = {}	
				test_bits = bitdict[key]
				grange = val
				for key2, val2 in rangedict.items():
					if key != key2: #and key + "VS" + key2 not in comparisons and key2 + "VS" + key not in comparisons:
						#comparisons.append(key + "VS" + key2)
						#comparisons.append(key2 + "VS" + key)
						test_overlap = float(len(list(set(grange) & set(val2))))/float(len(val2))
						og_bits = bitdict[key2]
						if test_overlap > overlap: #and test_bits  > og_bits:
							if key not in overlap_dict.keys():
								overlap_dict[key] = test_bits
							overlap_dict[key2] = og_bits
				if len(overlap_dict.keys()) > 0:	
					maxbits = 0
					max_gene = []
					for okey in overlap_dict.keys():
						oval = overlap_dict[okey]
						if oval > maxbits:
							maxbits = oval
							max_gene = [okey]
						elif oval == maxbits:
							max_gene.append(okey)
				else:
					max_gene = [key]
				max_gene = sorted(max_gene)
				if len(max_gene) > 1:
					max_gene = "/".join(max_gene)
				else:
					max_gene = max_gene[0]
				if max_gene not in bt:
					bt.append(max_gene)

		except EmptyDataError:
			bt = []	
		return(sorted(bt))				
