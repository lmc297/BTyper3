# BTyper3

*In silico* taxonomic classification of *Bacillus cereus* group isolates using assembled genomes

## Overview

BTyper3 is a command-line tool for taxonomically classifying *Bacillus cereus* group genomes using a novel, standardized nomenclature

The program, as well as the associated databases, can be downloaded from https://github.com/lmc297/BTyper3.

Post issues at https://github.com/lmc297/BTyper3/issues

### Citation

#### If you found the BTyper3 tool, its source code, and/or any of its associated databases useful, please cite:
  
Carroll, Laura M., Martin Wiedmann, Jasna Kovac. 2020. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7042689/">"Proposal of a Taxonomic Nomenclature for the *Bacillus cereus* Group Which Reconciles Genomic Definitions of Bacterial Species with Clinical and Industrial Phenotypes."</a> *mBio* 11(1): e00034-20; DOI: 10.1128/mBio.00034-20.

Carroll, Laura M., Rachel A. Cheng, Jasna Kovac. 2020. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7536271/">"No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the *Bacillus cereus* group with Historical Typing Methods."</a> *Frontiers in Microbiology* 11: 580691; DOI: 10.3389/fmicb.2020.580691.

#### If you used BTyper3 to perform species and/or subspecies and/or pseudo-gene flow unit assignment, please additionally cite:

Jain, Chirag, Luis M. Rodriguez-R, Adam M. Phillippy, Konstantinos T. Konstantinidis, Srinivas Aluru. 2018. High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries. *Nature Communications* 9(1):5114. doi: 10.1038/s41467-018-07641-9.

#### If you used BTyper3 to perform biovar assignment and/or to identify virulence factors and/or to identify Bt toxin-encoding genes and/or to perform *in silico* MLST and/or *panC* group assignment, please additionally cite:

Camacho, Christiam, George Coulouris, Vahram Avagyan, Ning Ma, Jason Papadopoulos, Kevin Bealer, Thomas L Madden. 2009. BLAST+: architecture and applications. *BMC Bioinformatics* 10:421. doi: 10.1186/1471-2105-10-421.

Cock, Peter J. A., Tiago Antao, Jeffrey T. Chang, Brad A. Chapman, Cymon J. Cox, Andrew Dalke, Iddo Friedberg, Thomas Hamelryck, Frank Kauff, Bartek Wilczynski, Michiel J. L. de Hoon. 2009. Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics* 25(11): 1422–1423. doi: 10.1093/bioinformatics/btp163.

#### If you used BTyper3 to perform seven-gene MLST, please additionally cite:

Jolley, Keith A., James E. Bray, Martin C.J. Maiden. 2018. Open-access bacterial population genomics: BIGSdb software, the PubMLST.org website and their applications. *Wellcome Open Research* 3: 124. doi: doi:10.12688/wellcomeopenres.14826.1


------------------------------------------------------------------------
  
  
## Quick Start
  
### Command Structure
  
```
btyper3 -i [fasta] -o [output directory] [options...]
```

For help, type `btyper3 -h` or `btyper3 --help`

For your current version, type `btyper3 --version`

### Sample Commands

#### Perform all default analyses, using an assembled genome (complete or draft) in (multi-)FASTA format as input (assumes fastANI is in the user's path):

```
btyper3 -i /path/to/genome.fasta -o /path/to/desired/output_directory
```

#### Perform all default analyses, using an assembled genome (complete or draft) in (multi-)FASTA format as input (fastANI is not in the user's path):

```
btyper3 -i /path/to/genome.fasta -o /path/to/desired/output_directory --fastani_path /path/to/FastANI_executable/fastANI
```

#### Perform all default analyses, plus pseudo-gene flow unit assignment, using an assembled genome (complete or draft) in (multi-)FASTA format as input (assumes fastANI is in the user's path):

```
btyper3 -i /path/to/genome.fasta -o /path/to/desired/output_directory --ani_geneflow True
```

#### Perform seven-gene MLST only, using user-supplied MLST gene sequences and the latest version of the PubMLST *B. cereus s.l.* database (sequences can be in multi-FASTA format, or concatenated into a single sequence in FASTA format):

```
btyper3 -i /path/to/mlst.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --virulence False --bt False --panC False --download_mlst_latest True
```

#### Perform *panC* group assignment only, using a user-supplied *panC* gene sequence in FASTA format:

```
btyper3 -i /path/to/panC.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --virulence False --bt False --mlst False
```

#### Perform virulence factor and Bt toxin-encoding gene detection in a plasmid sequence in FASTA format:

```
btyper3 -i /path/to/plasmid.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --mlst False --panC False
```


------------------------------------------------------------------------
  
  
## Installation
### Install BTyper3 using Homebrew (macOS users)
  
BTyper3 and its dependencies can be installed using <a href="https://brew.sh/">Homebrew</a>.

1. First, install Homebrew, if necessary, by running the following command from your terminal:
  
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Install python3, if necessary, by running the following command from your terminal:

```
brew install python3
```

3. Install Biopython, if necessary, by running the following command from your terminal:

```
pip3 install biopython
```
Note: if you don't have permissions, you may need to use --user:

```
pip3 install --user biopython
```

4. Install pandas, if necessary, by running the following command from your terminal:

```
pip3 install pandas
```

5. Install numpy, if necessary, by running the following command from your terminal:

```
pip3 install numpy
```

6. Install BLAST, if necessary, by running the following command from your terminal (you can alternatively install BLAST from <a href="https://anaconda.org/bioconda/blast">bioconda</a> or <a href="ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/">from NCBI</a>):

```
brew install blast
```

<a href="https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path">Additionally, make sure BLAST+ is in your path</a>, if necessary (to check if BLAST+ is in your path, try running ```makeblastdb -h``` and ```tblastn -h``` from your command line; you should get a help message for each command, with no error messages)

7. Follow the instructions to install <a href="https://github.com/ParBLiSS/FastANI">fastANI</a>, if necessary.

8. Tap brewsci/bio, if necessary, by running the following command from your terminal:

```
brew tap brewsci/bio
```

9. Tap BTyper3 by running the following command from your terminal:
  
```
brew tap lmc297/homebrew-btyper3
```

10. Install BTyper3 and its dependencies by running the following command from your terminal:
  
```
brew install btyper3
```

11. Download the "species-only", "subspecies-only", "full" (i.e., both "species-only" and "subspecies-only"), or "geneflow-only" database(s) by running one or more of the following commands from your terminal; note that users who want to perform all ANI-based assignment methods implemented in BTyper3 (i.e., species, subspecies, and pseudo-gene flow unit assignment) should download both the "full" and "geneflow-only" databases (i.e., run both command "A" and command "D" below):

A. For the full database, which can be used to perform both species and subspecies assignment, but not pseudo-gene flow unit assignment (needs about 102M disk space):

```
build_btyper3_anib_db.py -db full
```

B. For species-only database, which can be used to perform species assignment (but not subspecies or pseudo-gene flow unit assignment; needs about 91M disk space):
```
build_btyper3_anib_db.py -db species-only
```

C. For subspecies-only database, which can be used to perform subspecies assignment (but not species or pseudo-gene flow unit assignment; needs about 11M disk space):
```
build_btyper3_anib_db.py -db subspecies-only
```

D. For geneflow-only database, which can be used to perform pseudo-gene flow unit assignment (but not species or subspecies assignment; needs about 198M disk space):

```
build_btyper3_anib_db.py -db geneflow-only
```

After running any command, follow the instructions in your terminal.

12. Download the latest PubMLST database by running the following command from your terminal:

```
download_pubmlst_latest.py
```


### Download and run BTyper3 using source file (macOS and Ubuntu)

1. To run BTyper3, please download and install the following dependencies, if necessary:
  
  <a href="https://www.python.org/downloads/">python3</a>
  
  <a href="https://biopython.org/wiki/Download">Biopython v. 1.7.4 and up (for python3)</a>
  
  <a href="https://pandas.pydata.org/pandas-docs/stable/install.html">Pandas (for python3)</a>
  
  <a href="https://numpy.org/">NumPy (for python3)</a>
  
  BLAST v. 2.9.0+ and up (ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/)
  
  <a href="https://github.com/ParBLiSS/FastANI">FastANI version 1.0 and up</a>
  
2. <a href="https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path">Add BLAST+ to your path</a>, if necessary (to check if BLAST+ is in your path, try running ```makeblastdb -h``` and ```tblastn -h``` from your command line; you should get a help message for each command, with no error messages)

3. Optional: <a href="https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path">Add fastANI to your path</a>, if necessary (to check if fastANI is in your path, try running ```fastANI -h``` from your command line; you should get a help message, with no error messages). Note that this step is optional; if you want to perform species and/or subspecies and/or pseudo-gene flow unit assignment using BTyper3, you can just use the ```--fastani_path``` argument and supply the path to the fastANI executable (```--fastani_path /path/to/fastANI```)
    
4. Download the BTyper3 source file, and store it in your directory of choice:

To download manually, click the following URL, and then click the "Download" button: "https://github.com/lmc297/BTyper3/blob/master/archive/btyper-3.1.2.tar.gz

Or with `wget`:
```
wget https://github.com/lmc297/BTyper3/raw/master/archive/btyper-3.1.2.tar.gz
```

5. Extract BTyper3 program/databases

```
tar -xzvf btyper-3.1.2.tar.gz
```

Note: to ensure that BTyper3 works correctly, make sure database directories (beginning with "seq_") remain in the same directory as the BTyper3 executable (stored as "btyper3").

6. To run BTyper, call python3 and supply the full path to the btyper3 executable:

```
python3 /path/to/executable/btyper3 [options...]
```

Note: In the examples below, BTyper3 commands are shown as ```btyper3 [options...]```. If you are calling BTyper3 from the source file (i.e. you didn't install BTyper3 using Homebrew), keep in mind that you may have to call python3 and supply the path to btyper3 to execute the program or related scripts: ```python3 btyper3 [options...]```.

7. Download the "species-only", "subspecies-only", "full" (i.e., both "species-only" and "subspecies-only"), or "geneflow-only" database(s) by running one or more of the following commands from your terminal; note that users who want to perform all ANI-based assignment methods implemented in BTyper3 (i.e., species, subspecies, and pseudo-gene flow unit assignment) should download both the "full" and "geneflow-only" databases (i.e., run both command "A" and command "D" below):

A. For the full database, which can be used to perform both species and subspecies assignment, but not pseudo-gene flow unit assignment (needs about 102M disk space):

```
python3 build_btyper3_anib_db.py -db full
```

B. For species-only database, which can be used to perform species assignment (but not subspecies or pseudo-gene flow unit assignment; needs about 91M disk space):
```
python3 build_btyper3_anib_db.py -db species-only
```

C. For subspecies-only database, which can be used to perform subspecies assignment (but not species or pseudo-gene flow unit assignment; needs about 11M disk space):
```
python3 build_btyper3_anib_db.py -db subspecies-only
```

D. For geneflow-only database, which can be used to perform pseudo-gene flow unit assignment (but not species or subspecies assignment; needs about 198M disk space):

```
python3 build_btyper3_anib_db.py -db geneflow-only
```

After running any command, follow the instructions in your terminal.

8. Download the latest PubMLST database by running the following command from your terminal:

```
python3 download_pubmlst_latest.py
```

Note: In the examples below, BTyper3 commands are shown as ```btyper3 [options...]```. If you are calling BTyper3 from the source file (i.e. you didn't install BTyper3 using Homebrew), keep in mind that you may have to call python3 and supply the path to btyper3 to execute the program or related scripts: ```python3 btyper3 [options...]```.


------------------------------------------------------------------------
  
  
## Usage and Options
  
### Input File Formats
  
BTyper3 requires an assembled genome in FASTA format, with one FASTA file containing a single *B. cereus* group genome (this can be a closed genome, or a draft genome containing multiple contigs or scaffolds)
  
### Required Arguments

BTyper3 can be run from your terminal with the following command line:
  
```
usage: btyper3 -i </path/to/genome.fasta> -o </path/to/output/directory/> [other options]
```

Required arguments are:

```
  -i INPUT, --input INPUT
                        Path to input genome in fasta format
  -o OUTPUT, --output OUTPUT
                        Path to desired output directory
```

Optional arguments are:

```
  --ani_species [ANI_SPECIES]
                        Optional argument; True or False; assign genome to a
                        species using FastANI; default = True
  --ani_subspecies [ANI_SUBSPECIES]
                        Optional argument; True or False; assign genome to a
                        subspecies, if relevant, using FastANI; default = True
  --ani_geneflow [ANI_GENEFLOW]
                        Optional argument; True or False; assign genome to a
                        pseudo-gene flow unit using the method described by
                        Carroll, et al. using FastANI; default = False
  --fastani_path [FASTANI_PATH]
                        Optional argument for use with --ani_species True
                        and/or --ani_subspecies True and/or --ani_geneflow
                        True; fastANI, unless path to fastANI executable is
                        supplied; path to fastANI; default = fastANI <fastANI
                        is in the user's path>
  --virulence [VIRULENCE]
                        Optional argument; True or False; perform virulence
                        gene detection (required if one wants to assign
                        genomes to biovars Anthracis or Emeticus); default =
                        True
  --bt [BT]             Optional argument; True or False; perform Bt toxin
                        gene detection for cry, cyt, and vip genes (required
                        if one wants to assign genomes to biovar
                        Thuringiensis); default = True
  --mlst [MLST]         Optional argument; True or False; assign genome to a
                        sequence type (ST) using the seven-gene multi-locus
                        sequence typing (MLST) scheme available in PubMLST;
                        default = True
  --panC [PANC]         Optional argument; True or False; assign genome to a
                        phylogenetic group (Group I-VIII) using an adjusted,
                        eight-group panC group assignment scheme; default =
                        True
  --virulence_db [VIRULENCE_DB]
                        Optional argument for use with --virulence True; aa or
                        nuc; database to use for virulence factor detection:
                        aa for the amino acid sequence database, or nuc for
                        the nucleotide sequence database; option aa uses
                        translated nucleotide blast and allows for the
                        detection of more remote homologs, but is slower than
                        nuc, which uses blastn; default = aa
  --virulence_identity [VIRULENCE_IDENTITY]
                        Optional argument for use with --virulence True;
                        integer from 0 to 100; minimum percent amino
                        acid/nucleotide identity threshold for a virulence
                        gene to be considered present, depending on choice of
                        --virulence_db aa or nuc, respectively; default = 70
  --virulence_coverage [VIRULENCE_COVERAGE]
                        Optional argument for use with --virulence True;
                        integer from 0 to 100; minimum percent coverage
                        threshold for a virulence gene to be considered
                        present; default = 80
  --bt_identity [BT_IDENTITY]
                        Optional argument for use with --bt True; integer from
                        0 to 100; minimum percent amino acid identity
                        threshold for a Bt toxin gene to be considered
                        present; default = 50
  --bt_coverage [BT_COVERAGE]
                        Optional argument for use with --bt True; integer from
                        0 to 100; minimum percent coverage threshold for a Bt
                        toxin gene to be considered present; default = 70
  --bt_overlap [BT_OVERLAP]
                        Optional argument for use with --bt True; float from 0
                        to 1; specify maximum proportion of overlap for
                        overlapping Bt toxin genes to be considered separate
                        genes; Bt toxin genes below this threshold will be
                        considered separate, while those above it will be
                        considered overlapping, and only the top hit will be
                        reported; default=0.7
  --evalue [EVALUE]     Optional argument for use with --virulence True and/or
                        --bt True; float >= 0; maximum blast e-value for a hit
                        to be saved; note that if both --virulence True and
                        --bt True, this e-value threshold will be applied to
                        both analyses; default = 1e-5
  --download_mlst_latest [DOWNLOAD_MLST_LATEST]
                        Optional argument for use with --mlst True; True or
                        False; download the latest version of the seven-gene
                        multi-locus sequence typing (MLST) scheme available in
                        PubMLST; if this is False, BTyper3 will search for the
                        appropriate files in the seq_mlst_db directory;
                        default = False
```

For help:
```
btyper3 -h
```

For the version:
```
btyper3 --version
```
------------------------------------------------------------------------
  
  
## Output Directories and Files
  
A single BTyper3 run will deposit the following in your specified output directory (```--output```):
  
```btyper3_final_results``` (*directory*): Final results directory in which BTyper3 deposits all of its output files. BTyper3 creates this directory in your specified output directory (```--output```) 

```your_genome_final_results.txt``` (*file*): Final tab-separated text file, 1 per input genome. BTyper3 creates this file, which has a header (denoted with "#"), followed by a single row containing results for the input genome, where columns contain the following:

* **Column 1: #filename**
The path to the fasta file supplied as input.

* **Column 2: prefix**
The file name prefix used by BTyper3 for all results files

* **Column 3: species(ANI)**
The *B. cereus* group genomospecies producing the highest average nucleotide identity (ANI) value, with the corresponding ANI value in parentheses. If the input genome does not share >= 92.5 ANI with any known *B. cereus* group species medoid genome, an asterisk is appended to the species name. If species assignment is not performed (```--ani_species False```), a designation of "(Species assignment not performed)" is given.

* **Column 4: subspecies(ANI)**
Assigned *B. cereus* group subspecies, with the corresponding ANI value in parentheses, if applicable. If the input genome does not meet any subspecies thresholds, a subspecies designation of "No subspecies" is given. If subspecies assignment is not performed (```--ani_subspecies False```), a designation of "(Subspecies assignment not performed)" is given.

* **Column 5: Pseudo_Gene_Flow_Unit(ANI)**
Assigned *B. cereus* group pseudo-gene flow unit, with the corresponding ANI value relative to the pseudo-gene flow unit medoid genome in parentheses. If the input genome does not fall within the observed ANI boundary for any previously delineated "true" gene flow unit, an asterisk is appended to the pseudo-gene flow unit name.

* **Column 6: anthrax_toxin(genes)**
Number of anthrax toxin-encoding genes detected in the input genome, out of the total number of anthrax toxin genes required for a genome to be assigned to biovar Anthracis (i.e., 3 genes; *cya, lef, pagA*). Anthrax toxin genes detected in the input genome are listed in parentheses.

* **Column 7: emetic_toxin_cereulide(genes)**
Number of cereulide synthetase-encoding genes detected in the input genome, out of the total number of cereulide synthetase genes required for a genome to be assigned to biovar Emeticus (i.e., 4 genes; *cesABCD*). Cereulide synthetase genes detected in the input genome are listed in parentheses.

* **Column 8: diarrheal_toxin_Nhe(genes)**
Number of non-hemolytic enterotoxin (Nhe)-encoding genes detected in the input genome, out of three (*nheABC*). Nhe-encoding genes detected in the input genome are listed in parentheses.

* **Column 9: diarrheal_toxin_Hbl(genes)**
Number of hemolysin BL (Hbl)-encoding genes detected in the input genome, out of four (*hblABCD*). Hbl-encoding genes detected in the input genome are listed in parentheses.

* **Column 10: diarrheal_toxin_CytK(top_hit)**
Highest-scoring Cytotoxin K (CytK)-encoding gene detected in the input genome (either *cytK-1* or *cytK-2*). The highest-scoring CytK-encoding gene detected in the input genome is listed in parentheses.

* **Column 11: sphingomyelinase_Sph(gene)**
Sphingomyelinase (Sph)-encoding gene detected in the input genome (*sph*). The Sph-encoding gene detected in the input genome is listed in parentheses.

* **Column 12: capsule_Cap(genes)**
Number of *B. anthracis*-associated poly-γ-D-glutamic acid capsule (Cap)-encoding genes detected in the input genome, out of five (*capABCDE*). Cap-encoding genes detected in the input genome are listed in parentheses.

* **Column 13: capsule_Has(genes)**
Number of hyaluronic acid capsule (Has)-encoding genes detected in the input genome, out of three (*hasABC*). Has-encoding genes detected in the input genome are listed in parentheses.

* **Column 14: capsule_Bps(genes)**
Number of *"B. cereus"* exo-polysaccharide capsule (Bps)-encoding genes detected in the input genome, out of nine (*bpsXABCDEFGH*). Bps-encoding genes detected in the input genome are listed in parentheses.

* **Column 15: Bt(genes)**
Total number of *Bacillus thuringiensis* toxin (Bt toxin) genes detected in the input genome. Bt toxin genes detected in the input genome are listed in parentheses. **Note: BTyper3 currently detects known Bt toxin genes (i.e., those present in the <a href="http://www.btnomenclature.info/">Bt toxin nomenclature database</a>; accessed September 19, 2019)  using translated nucleotide blast (tblastn). This approach is conservative to reflect the analyses conducted in the manuscript (i.e., to limit false positives).**

* **Column 16: PubMLST_ST\[clonal_complex](perfect_matches)**
Sequence type (ST) assigned using PubMLST's seven-gene multi-locus sequence typing (MLST) scheme for *B. cereus s.l.* Square brackets contain the name of the PubMLST clonal complex associated with the ST, if available/applicable. Parentheses contain the number of perfect allele matches (i.e., with 100% nucleotide identity and coverage) out of seven possible.

* **Column 17: Adjusted_panC_Group(predicted_species)**
*panC* group assigned using the adjusted, eight-group *panC* group assignment scheme proposed by Carroll, et al. *panC* sequences of effective and proposed *B. cereus s.l.* species are also included in the database but are assigned a species name (e.g., “Group_manliponensis”) rather than a number (i.e., Group_I to Group_VIII). Species associated with a *panC* group are listed in parentheses. If the query genome does not share >= 99% nucleotide identity and/or >= 80% coverage with one or more *panC* alleles in the database, the closest-matching *panC* group is reported with an asterisk.

* **Column 18: final_taxon_names**
Taxonomic assignment of the isolate, written from longest (species, subspecies [if applicable], and biovars [if applicable]) to shortest (biovars, if applicable) form. If the input genome does not share >= 92.5 ANI with any known *B. cereus* group species medoid genome (i.e., there is an asterisk appended to the species name in the "species(ANI)" column), a species designation of "(Species unknown)" is given (this designation is also used if species assignment is not performed, i.e., ```--ani_species False```). If 2 or more anthrax toxin genes and/or cereulide synthetaste genes are detected in the input genome, but one or more anthrax toxin genes and cereulide synthetase genes are missing, respectively, an asterisk is appended to the biovar (i.e., "Anthracis\*" and "Emeticus\*", respectively)

```species``` (*directory*): Directory in which BTyper3 deposits raw fastANI output files during species assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/species```).

```subspecies``` (*directory*): Directory in which BTyper3 deposits raw fastANI output files during subspecies assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/subspecies```).

```geneflow``` (*directory*): Directory in which BTyper3 deposits raw fastANI output files during pseudo-gene flow unit assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/geneflow```).

```virulence``` (*directory*): Directory in which BTyper3 deposits raw blast output files during virulence gene detection. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/virulence```).

```bt``` (*directory*): Directory in which BTyper3 deposits raw blast output files during Bt gene detection. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/bt```).

```mlst``` (*directory*): Directory in which BTyper3 deposits raw blast output files during seven-gene MLST. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/mlst```).

```panC``` (*directory*): Directory in which BTyper3 deposits raw blast output files during *panC* group assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/panC```).

```logs``` (*directory*): Directory in which BTyper3 deposits its log files for a run. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/logs```).


------------------------------------------------------------------------

## Additional BTyper3 Scripts

### build_btyper3_anib_db.py

* **Purpose:** download database(s) to be used for species and/or subspecies and/or pseudo-gene flow unit assignment (```--ani_species True``` and/or ```--ani_subspecies True``` and/or `--ani_geneflow True`); must be run before performing species and/or subspecies and/or pseudo-gene flow unit assignment

```
usage: build_btyper3_ani_db.py -db [full, species-only, subspecies-only, geneflow-only]

optional arguments:
  -h, --help            show this help message and exit
  -db [DATABASE], --database [DATABASE]
                        Optional argument; Specify the ANI database to
                        download for use with FastANI (--ani_species True
                        and/or --ani_subspecies True and/or --ani_geneflow
                        True options): full, species-only, subspecies-only,
                        geneflow-only; full for 102M database with medoid
                        genomes of 18 Bacillus cereus group genomospecies,
                        plus 2 subspecies genomes (used with --ani_species
                        True and --ani_subspecies True); species-only for 91M
                        database with medoid genomes of 18 Bacillus cereus
                        group genomospecies (subspecies genomes are not
                        downloaded; used with --ani_species True and
                        --ani_subspecies False); subspecies-only for 11M
                        database with 2 subspecies genomes (genomospecies
                        genomes are not downloaded; used with --ani_species
                        False and --ani_subspecies True); geneflow-only for
                        the 198M database with 37 genomes (used for pseudo-
                        gene flow unit assignment with --ani_geneflow True);
                        default = full
```
Users will then be prompted in the terminal to type "yes" and press ENTER to confirm the download.

For help, type ```build_btyper3_anib_db.py -h``` or ```build_btyper3_anib_db.py --help```

### download_pubmlst_latest.py

* **Purpose:** download latest PubMLST database for *Bacillus cereus* to be used for *in silico* seven-gene MLST (```--mlst True```); must be run before performing MLST (or, alternatively, set ```--download_mlst_latest True``` when running ```btyper3```)

```
usage: build_btyper3_ani_db.py

optional arguments:
  -h, --help  show this help message and exit
```

------------------------------------------------------------------------
  
  
## Frequently Asked Questions

* **What's the difference between BTyper3 and the original BTyper?**

BTyper3 is a completely novel tool for determining the identity of *B. cereus* group isolates using WGS data and a standardized taxonomic nomenclature. Unlike its predecessor, which focused on gene detection and required a signifcant amount of user knowledge/interpretation, BTyper3 aims to provide taxonomic classifications at a whole-genome scale which require minimal user interpretation/prior domain-specific knowledge of the *B. cereus* group.
  
* **Why is it named BTyper3?**

BTyper3 uses python3; python2, which the original BTyper relied on, <a href="https://pythonclock.org/">will not be maintained in the future.</a> Additionally (and conveniently!), the most recent version of the original BTyper was version 2, making BTyper3 a logical next step.

* **Why doesn't BTyper3 perform *rpoB* allelic typing like the original BTyper?**

When developing BTyper3, we found that <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">the resolution *rpoB* provided was lower than that of MLST and *panC*</a>. We thus opted to not currently include it in BTyper3 (this may change in the future, but for now, see the <a href="https://github.com/lmc297/BTyper">original BTyper</a> if you'd like to perform *rpoB* allelic typing).

* **Why doesn't BTyper3 perform antimicrobial resistance (AMR) determinant detection like the original BTyper?**

The AMR determinant detection method implemented in the original BTyper was difficult to maintain and wasn't *B. cereus* group-specific; we thus considered it to fall outside of the scope of BTyper3, and we opted to not include it. In addition to the <a href="https://github.com/lmc297/BTyper">original BTyper</a>, there are many AMR determinant detection methods available now, including some that do <a href="https://github.com/tseemann/abricate">effectively the same thing as the original BTyper</a>.

* **Can I analyze BTyper3 output files with <a href="https://github.com/lmc297/BMiner">BMiner</a>?**

Sadly, BMiner currently does not support BTyper3 files as input, as BTyper3 and the <a href="https://github.com/lmc297/BTyper">original BTyper (version 2.X.X and earlier)</a> produce files in different output formats. BTyper3 was developed to produce output files in a standard tabular format, which we anticipate will be easier for users to work with. 

To aggregate all BTyper3 results from a single run into a single tab-separated table which can then be loaded into R, Excel, etc., simply:

1. Move to your BTyper3 output directory: `cd < name of the directory you supplied to btyper3 -o >`
2. Concatenate BTyper3 final results files into a single file, here named `btyper3_all_results.txt` (the `-v` option excludes the file headers): `cat btyper3_final_results/*_final_results.txt | grep -v "#filename" > btyper3_all_results.txt`

* **Can I use sequencing reads (e.g., Illumina reads) as input for BTyper3?**

No; BTyper3 requires an assemlbed genome in FASTA format. While the original BTyper had the option to use SPAdes for genome assembly, we opted to not include it in BTyper3, as it became time-consuming to maintain, without adding significant value to users.

* **Can I use multiple *B. cereus* group genomes in a single FASTA file (e.g., an assembled metagenome) as input for BTyper3?**

No; BTyper3 requires whole genomes of single *B. cereus* group isolates, as it relies on ANI-based methods.

* **Can I use partial nucleotide sequences (e.g., plasmid sequences, MLST genes, *panC* alleles, etc.) as input for BTyper3?**
  
Yes, but only if you set all ANI-based methods to False (i.e., make sure to include `--ani_species False --ani_subspecies False` in your command), as ANI-based methods require whole genomes. 

To perform seven-gene MLST only, using the latest version of the PubMLST *B. cereus* database, use the following command:

```
btyper3 -i [fasta] -o [output directory] --ani_species False --ani_subspecies False --virulence False --bt False --panC False --download_mlst_latest True
```

To perform *panC* group assignment only, use the following command:

```
btyper3 -i [fasta] -o [output directory] --ani_species False --ani_subspecies False --virulence False --bt False --mlst False
```

To detect virulence factors and Bt toxin-encoding genes in a nucleotide sequence (e.g., a plasmid sequence), use the following command:

```
btyper3 -i [fasta] -o [output directory] --ani_species False --ani_subspecies False --mlst False --panC False
```

* **Can I use WGS data from organisms that don't belong to the *Bacillus cereus* group?**
  
No; BTyper3 is a taxonomic tool which relies on ANI-based methods relative to *B. cereus* group genomes. Results for distant species won't be interpretable.

------------------------------------------------------------------------
  
  
## BTyper3 Tutorial #1: Characterizing a *B. cereus* isolate using its draft genome
  
1. First, let's download our isolate's draft genome from NCBI by clicking the follwoing link:
  
https://www.ncbi.nlm.nih.gov/Traces/wgs/JHQN01

If not already selected, click the "Download" tab. Click on the link for the FASTA file to download the contigs in fasta format: JHQN01.1.fsa_nt.gz. This should download the file into your "Downloads" directory.

2. If you haven't done so already, open your terminal. For Mac users, type **command-space** to open your search bar, type **terminal** in your search bar, and press **Enter**. For Ubuntu users, type **Ctrl-Alt-t** (assuming you haven't changed your default shortcuts).

3. From the command line in your terminal, move to your "Downloads directory" by typing the following, and then hitting **Enter**:
  
```
cd ~/Downloads
```

4. Now that we're in our Downloads directory, let's unzip our contigs file by typing the following command, and hitting **Enter**:
  
```
gunzip JHQN01.1.fsa_nt.gz
```

5. Let's create an output directory in which we can store our BTyper3 results. That way, once we're done with this tutorial, we can easily delete everything. To create a directory called "btyper3_tutorial_1" in our Downloads directory, type the following command and hit **Enter**:
  
```
mkdir ~/Downloads/btyper3_tutorial_1
```

6. Now, let's run BTyper3 on our genome, directly from our Downloads directory, by typing the following command into our terminal, and pressing **Enter**:

```
btyper3 -i ~/Downloads/JHQN01.1.fsa_nt -o ~/Downloads/btyper3_tutorial_1
```

Here are the options we selected, explained:

* **-i ~/Downloads/JHQN01.1.fsa_nt**
We're directing BTyper3 to our input file (JHQN01.1.fsa_nt)

* **-o ~/Downloads/btyper3_tutorial_1**
We're telling BTyper3 where to store the output files it produces (our directory, btyper3_tutorial_1)

7. Once the program is finished running, we can take a look at our final results file to get detailed results about our isolate. Open the "JHQN01.1_final_results.txt" file in any text editor, either by searching for it or opening it in your "~/Downloads/btyper3_tutorial_1/btyper3_final_results" directory.

8. Now that we've opened the final results file for our isolate, we can see all taxonomic classifications for our isolate in the column "final_taxon_names". According to BTyper3, our genome's full taxonomic classification is *B. mosaicus* biovar Anthracis. This can also be written as *B.* Anthracis, meaning that our genome possesses anthrax toxin-encoding genes! We can see that all three toxin genes, *cya, lef,* and *pagA*, were detected in our genome (column "anthrax_toxin(genes)"). No cereulide synthetase genes were detected (column name "cereulide(genes)").
  
Sure enough, this genome is actually that of strain BcFL2013, an isolate previously classified as "anthrax-causing *B. cereus* which was isolated from a patient with an anthrax-like skin lesion in Florida (Gee, et al., 2014, *Genome Announcements*).

9. If you want to delete the results from this tutorial, just go to your Downloads folder and delete the "btyper3_tutorial_1" directory there.


## References

#### Dependencies

Camacho, Christiam, et al. BLAST+: architecture and applications. *BMC Bioinformatics* 2009 10:421.

Cock, Peter J., et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. *Bioinformatics* 2009 June 1; 25(11): 1422-1423.

Jain, Chirag, et al. High-throughput ANI Analysis of 90K Prokaryotic Genomes Reveals Clear Species Boundaries. *Nature Communications* 9(1):5114. doi: 10.1038/s41467-018-07641-9.

#### Tutorial Genomes

Gee, JE, et al. Draft Genome Sequence of *Bacillus cereus* Strain BcFL2013, a Clinical Isolate Similar to G9241. *Genome Announcements* 2014 May 29;2(3).


------------------------------------------------------------------------


Disclaimer: BTyper3 is pretty neat! However, no tool is perfect, and BTyper3 cannot definitively prove whether an isolate is pathogenic or not. As always, interpret your results with caution. We are not responsible for taxonomic misclassifications, misclassifications of an isolate's pathogenic potential or industrial utility, and/or misinterpretations (biological, statistical, or otherwise) of BTyper3 results.
