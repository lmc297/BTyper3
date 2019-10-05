# BTyper3

*In silico* taxonomic classification of *Bacillus cereus* group isolates using assembled genomes

## Overview

BTyper3 is a command-line tool for taxonomically classifying *Bacillus cereus* group genomes using a novel, standardized nomenclature

The program, as well as the associated databases, can be downloaded from https://github.com/lmc297/BTyper3.

Post issues at https://github.com/lmc297/BTyper3/issues

### Citation

#### If you found the BTyper3 tool, its source code, and/or any of its associated databases useful, please cite:
  
Carroll, Laura M., Martin Wiedmann, Jasna Kovac. 2019. "Proposal of a taxonomic nomenclature for the *Bacillus cereus* group which reconciles genomic definitions of bacterial species with clinical and industrial phenotypes." *bioRxiv* 779199; doi: https://doi.org/10.1101/779199.


------------------------------------------------------------------------
  
  
## Quick Start
  
#### Command structure:
  
```
btyper3 -i [fasta] -o [output directory] [options...]
```

For help, type `btyper3 -h` or `btyper3 --help`

For your current version, type `btyper3 --version`


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

5. Install numpy, if necessary, bu running the following command from your terminal:

```
pip3 install numpy
```

6. Follow the instructions to install <a href="https://github.com/ParBLiSS/FastANI">fastANI</a>, if necessary.

7. Tap brewsci/bio, if necessary, by running the following command from your terminal:

```
brew tap brewsci/bio
```

8. Tap BTyper3 by running the following command from your terminal:
  
```
brew tap lmc297/homebrew-btyper3
```

9. Install BTyper3 and its dependencies by running the following command from your terminal:
  
```
brew install btyper3
```

10. Download the "species-only", "subspecies-only", or "full" (i.e., both "species-only" and "subspecies-only") database by running one of the following commands from your terminal:

For the full database, which can be used to perform both species and subspecies assignment (recommended; needs about 98M disk space):

```
build_btyper3_anib_db.py -db full
```

For species-only database, which can be used to perform species assignment (but not subspecies assignment; needs about 87M disk space):
```
build_btyper_anib_db.py -db species-only
```

For subspecies-only database, which can be used to perform subspecies assignment (but not species assignment; needs about 11M disk space):
```
build_btyper_anib_db.py -db subspecies-only
```

After running any command, follow the instructions in your terminal.


### Download and run BTyper3 using source file (macOS and Ubuntu)

1. To run BTyper3, please download and install the following dependencies, if necessary:
  
  <a href="https://www.python.org/downloads/">python3</a>
  
  <a href="https://biopython.org/wiki/Download">Biopython v. 1.7.4 (for python3)</a>
  
  <a href="https://pandas.pydata.org/pandas-docs/stable/install.html">Pandas (for python3)</a>
  
  <a href="https://numpy.org/">NumPy (for python3)</a>
  
  <a href="https://github.com/Homebrew/homebrew-core/blob/master/Formula/blast.rb">BLAST+ v. 2.9.0 or higher</a>
  
  <a href="https://github.com/ParBLiSS/FastANI">FastANI version 1.0 or higher</a>
  
2. <a href="https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path">Add BLAST+ to your path</a>, if necessary (to check if BLAST+ is in your path, try running ```makeblastdb -h``` and ```tblastn -h``` from your command line; you should get a help message for each command, with no error messages)

3. Optional: <a href="https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path">Add fastANI to your path</a>, if necessary (to check if fastANI is in your path, try running ```fastANI -h``` from your command line; you should get a help message, with no error messages). Note that this step is optional; if you want to perform species and/or subspecies assignment using BTyper3, you can just use the ```--fastani_path``` argument and supply the path to the fastANI executable (```--fastani_path /path/to/fastANI```)
    
4. Download the BTyper3 source file, and store it in your directory of choice:

https://github.com/lmc297/BTyper3/blob/master/archive/btyper-3.0.1.tar.gz

5. Extract BTyper3 program/databases

```
tar -xzvf btyper-3.0.1.tar.gz
```

Note: to ensure that BTyper3 works correctly, make sure database directories (beginning with "seq_") remain in the same directory as the BTyper3 executable (stored as "btyper3").

6. To run BTyper, call python3 and supply the full path to the btyper3 executable:

```
python3 /path/to/executable/btyper3 [options...]
```

Note: In the examples below, BTyper3 commands are shown as ```btyper3 [options...]```. If you are calling BTyper3 from the source file (i.e. you didn't install BTyper3 using Homebrew), keep in mind that you may have to call python3 and supply the path to btyper3 to execute the program or related scripts: ```python3 btyper3 [options...]```.

7. Download the "species-only", "subspecies-only", or "full" (i.e., both "species-only" and "subspecies-only") database by running one of the following commands from your terminal:

For the full database, which can be used to perform both species and subspecies assignment (recommended; needs about 98M disk space):

```
build_btyper3_anib_db.py -db full
```

For species-only database, which can be used to perform species assignment (but not subspecies assignment; needs about 87M disk space):
```
build_btyper3_anib_db.py -db species-only
```

For subspecies-only database, which can be used to perform subspecies assignment (but not species assignment; needs about 11M disk space):
```
build_btyper3_anib_db.py -db subspecies-only
```

After running any command, follow the instructions in your terminal.

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
  --fastani_path [FASTANI_PATH]
                        Optional argument for use with --ani_species True or
                        --ani_subspecies True; fastANI, unless path to fastANI
                        executable is supplied; path to fastANI; default =
                        fastANI <fastANI is in the user's path>
  --virulence [VIRULENCE]
                        Optional argument; True or False; perform virulence
                        gene detection to assign genomes to biovars Anthracis
                        or Emeticus; default = True
  --bt [BT]             Optional argument; True or False; perform Bt toxin
                        gene detection for cry, cyt, and vip genes to assign
                        genomes to biovar Thuringiensis; default = True
  --virulence_identity [VIRULENCE_IDENTITY]
                        Optional argument for use with --virulence True;
                        integer from 0 to 100; minimum percent amino acid
                        identity threshold for a virulence gene to be
                        considered present; default = 70
  --virulence_coverage [VIRULENCE_COVERAGE]
                        Optional argument for use with --virulence True;
                        integer from 0 to 100; minimum percent coverage
                        threshold for a virulence gene to be considered
                        present; default = 70
  --bt_identity [BT_IDENTITY]
                        Optional argument for use with --bt True; integer from
                        0 to 100; minimum percent amino acid identity
                        threshold for a Bt toxin gene to be considered
                        present; default = 70
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

```your_genome_final_results.txt``` (*file*): Final tab-separated text file, 1 per input genome. BTyper3 creates this file, which has a header (denoted with "#"), followed by a single row containing results for the input genome, where where columns contain the following:

* **Column 1: #filename**
The path to the fasta file supplied as input.

* **Column 2: prefix**
The file name prefix used by BTyper3 for all results files

* **Column 3: species(ANI)**
The *B. cereus* group genomospecies producing the highest average nucleotide identity (ANI) value, with the corresponding ANI value in parentheses. If the input genome does not share >= 92.5 ANI with any known *B. cereus* group species medoid genome, an asterisk is appended to the species name. If species assignment is not performed (```--ani_species False```), a designation of "(Species assignment not performed)" is given.

* **Column 4: subspecies(ANI)**
Assigned *B. cereus* group subspecies, with the corresponding ANI value in parentheses, if applicable. If the input genome does not meet any subspecies thresholds, a subspecies designation of "No subspecies" is given. If subspecies assignment is not performed (```--ani_subspecies False```), a designation of "(Subspecies assignment not performed)" is given.

* **Column 5: cereulide(genes)**
Number of cereulide synthetase-encoding genes detected in the input genome, out of the total number of cereulide synthetase genes required for a genome to be assigned to biovar Emeticus. Cereulide synthetase genes detected in the input genome are listed in parentheses.

* **Column 6: anthrax_toxin(genes)**
Number of anthrax toxin-encoding genes detected in the input genome, out of the total number of anthrax toxin genes required for a genome to be assigned to biovar Anthracis. Anthrax toxin genes detected in the input genome are listed in parentheses.

* **Column 7: Bt(genes)**
Total number of *Bacillus thuringiensis* toxin (Bt toxin) genes detected in the input genome. Bt toxin genes detected in the input genome are listed in parentheses. **Note: BTyper3 currently detects known Bt toxin genes (i.e., those present in the <a href="http://www.btnomenclature.info/">Bt toxin nomenclature database</a>; accessed September 19, 2019)  using translated nucleotide blast (tblastn). This approach is conservative to reflect the analyses conducted in the manuscript (i.e., to limit false positives).**

* **Column 8: final_taxon_names**
Taxonomic assignment of the isolate, written from longest (species, subspecies [if applicable], and biovars [if applicable]) to shortest (biovars, if applicable) form. If the input genome does not share >= 92.5 ANI with any known *B. cereus* group species medoid genome (i.e., there is an asterisk appended to the species name in the "species(ANI)" column), a species designation of "(Species unknown)" is given (this designation is also used if species assignment is not performed, i.e., ```--ani_species False```). If 2 or more anthrax toxin genes and/or cereulide synthetaste genes are detected in the input genome, but one or more anthrax toxin genes and cereulide synthetase genes are missing, respectively, an asterisk is appended to the biovar (i.e., "Anthracis\*" and "Emeticus\*", respectively)

```species``` (*directory*): Directory in which BTyper3 deposits raw fastANI output files during species assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/species```).

```subspecies``` (*directory*): Directory in which BTyper3 deposits raw fastANI output files during subspecies assignment. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/subspecies```).

```virulence``` (*directory*): Directory in which BTyper3 deposits raw blast output files during virulence gene detection. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/virulence```).

```bt``` (*directory*): Directory in which BTyper3 deposits raw blast output files during Bt gene detection. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/bt```).

```logs``` (*directory*): Directory in which BTyper3 deposits its log files for a run. BTyper3 creates this directory within the ```btyper3_final_results directory``` within your specified output directory (```output_directory/btyper3_final_results/logs```).


------------------------------------------------------------------------

## Additional BTyper3 Scripts

### build_btyper3_anib_db.py

* **Purpose:** download database(s) to be used for species and subspecies assignment (```--ani_species True``` and/or ```--ani_subspecies True```); must be run before performing species and subspecies assignment

```
usage: build_btyper3_ani_db.py -db [full, species-only, subspecies-only]

optional arguments:
  -h, --help            show this help message and exit
  -db [DATABASE], --database [DATABASE]
                        Optional argument; Specify the ANI database to
                        download for use with FastANI (--ani_species True
                        and/or --ani_subspecies True options): full, species-
                        only, subspecies-only; full for 98M database with
                        medoid genomes of 18 Bacillus cereus group
                        genospecies, plus 2 subspecies genomes (used with
                        --ani_species True and --ani_subspecies True);
                        species-only for 87M database with medoid genomes of
                        18 Bacillus cereus group genospecies (subspecies
                        genomes are not downloaded; used with --ani_species
                        True and --ani_subspecies False); subspecies-only for
                        11M database with 2 subspecies genomes (genospecies
                        genomes are not downloaded; used with --ani_species
                        False and --ani_subspecies True); default = full
```
Users will then be prompted in the terminal to type "yes" and press ENTER to confirm the download.

For help, type ```build_btyper3_anib_db.py -h``` or ```build_btyper3_anib_db.py --help```

------------------------------------------------------------------------
  
  
## Frequently Asked Questions

* **What's the difference between BTyper3 and the original BTyper?**

BTyper3 is a completely novel tool for determining the identity of *B. cereus* group isolates using WGS data and a standardized taxonomic nomenclature. Unlike its predecessor, which focused on gene detection and required a signifcant amount of user knowledge/interpretation, BTyper3 aims to provide taxonomic classifications at a whole-genome scale which require minimal user interpretation/prior domain-specific knowledge of the *B. cereus* group.
  
* **Why is it named BTyper3?**

BTyper3 uses python3; python2, which the original BTyper relied on, <a href="https://pythonclock.org/">will not be maintained in the future.</a> Additionally (and conveniently!), the most recent version of the original BTyper was version 2, making BTyper3 a logical next step.

* **Can I use sequencing reads (e.g., Illumina reads) as input for BTyper3?**

No; BTyper3 requires an assemlbed genome in FASTA format. While the original BTyper had the option to use SPAdes for genome assembly, we opted to not include it in BTyper3, as it became time-consuming to maintain, without adding significant value to users.

* **Can I use multiple *B. cereus* group genomes in a single FASTA file (e.g., an assembled metagenome) as input for BTyper3?**

No; BTyper3 requires whole genomes of single *B. cereus* group isolates, as it relies on ANI-based methods.

* **Can I use partial nucleotide sequences (e.g., plasmid sequences, MLST genes, *rpoB* alleles, etc.) as input for BTyper3?**
  
No; unlike its predecessor, BTyper3 requires whole genomes, as it relies on average-nucleotide identity (ANI)-based methods for species/subspecies assignment.

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

Jain, Chirag, et al. High-throughput ANI Analysis of 90K Prokaryotic Genomes Reveals Clear Species Boundaries. bioRxiv 225342; doi: https://doi.org/10.1101/225342.

#### Tutorial Genomes

Gee, JE, et al. Draft Genome Sequence of *Bacillus cereus* Strain BcFL2013, a Clinical Isolate Similar to G9241. *Genome Announcements* 2014 May 29;2(3).


------------------------------------------------------------------------


Disclaimer: BTyper3 is pretty neat! However, no tool is perfect, and BTyper3 cannot definitively prove whether an isolate is pathogenic or not. As always, interpret your results with caution. We are not responsible for taxonomic misclassifications, misclassifications of an isolate's pathogenic potential or industrial utility, and/or misinterpretations (biological, statistical, or otherwise) of BTyper3 results.











