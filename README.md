# BTyper3

*In silico* taxonomic classification of *Bacillus cereus* group isolates using assembled genomes

## Overview

BTyper3 is a command-line tool for taxonomically classifying *Bacillus cereus* group genomes using a standardized nomenclature.

The program, as well as the associated databases, can be downloaded from https://github.com/lmc297/BTyper3.

Post issues at https://github.com/lmc297/BTyper3/issues.

For more information, check out the BTyper3 wiki at https://github.com/lmc297/BTyper3/wiki.

------------------------------------------------------------------------

## Installation

For more information, check out the <a href="https://github.com/lmc297/BTyper3/wiki">BTyper3 wiki</a>

### conda (recommended)

To create a conda environment named `btyper3` and install BTyper3 and all of its dependencies:

1. Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), if necessary
2. Create a new environment named `btyper3` by running the following command from your terminal:
   ```console
   conda create -n btyper3
   ```
3. Activate your `btyper3` environment by running the following command from your terminal:
   ```console
   conda activate btyper3
   ```
4. Install [BTyper3](https://anaconda.org/bioconda/btyper3) by running the following command from your terminal:
   ```console
   conda install -c bioconda btyper3
   ```
5. You can now run `btyper3`! Run the following command from your terminal to view all `btyper3` options, or <a href="https://github.com/lmc297/BTyper3/wiki">check the BTyper3 wiki</a> for details:
   ```console
   btyper3 --help
   ```
6. When you're done with BTyper3, you can deactivate the `btyper3` environment by running the following:
   ```console
   conda deactivate
   ```

### pip

1. To run BTyper3, please download and install the following dependencies, if necessary:

   - [Python 3](https://www.python.org/downloads/)
   - [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download) v2.9.0+ and up
  <!-- - [Biopython](https://biopython.org/wiki/Download) v1.7.4 and up (for Python 3)
  - [Pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) (for Python 3)
  - [NumPy] (for Python 3)
  - [PyFastANI] version 0.3 and up</a> -->

2. [Add BLAST+ to your path](https://unix.stackexchange.com/questions/26047/how-to-correctly-add-a-path-to-path), if necessary (to check if BLAST+ is in your path, try running `makeblastdb -h` and `tblastn -h` from your command line; you should get a help message for each command, with no error messages)

3. Install via `pip` (this will download required Python dependencies as well):
   ```console
   pip install btyper3  
   ```

------------------------------------------------------------------------

## News: updates in BTyper3 v3.2.0, v3.3.0, and v3.4.0 -- new species just dropped!

The primary function of BTyper3 is to allow users to taxonomically classify *B. cereus* group genomes using a standardized nomenclature (see <a href="https://journals.asm.org/doi/10.1128/mBio.00034-20">here</a> and <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">here</a> for details regarding how the standardized nomenclature was constructed, and how it compares to historical typing methods, respectively). However, we understand that some users may also want to compare their *B. cereus* group genomes to the type strain genomes of published *B. cereus* group species. Thus, in BTyper3 v3.2.0, we have added the `--ani_typestrains` option, which calculates ANI values between a query genome and the genomes of all published *B. cereus* group species type strains and reports the type strain that produces the highest ANI value.

The type strain genomes used by BTyper3's `--ani_typestrains` option correspond to the species discussed in <a href="https://www.tandfonline.com/doi/full/10.1080/10408398.2021.1916735">Figure 2 of our taxonomy review</a>, plus species published after the review was published</a> (i.e., *Bacillus sanguinis*, *Bacillus paramobilis*, and *Bacillus hominis*, added in v3.2.0; "*B. arachidis*" and *B. rhizoplanae*, added in v3.3.0; "*B. pretiosus*", added in v3.4.0). Within the standardized taxonomy that BTyper3 uses for genomospecies assignment:

* All members of *Bacillus sanguinis* (type strain RefSeq Assembly Accession GCF_018332475.1) belong to *B. mosaicus* (i.e., *B. sanguinis* is not considered a novel species in the standardized taxonomy)

* All members of *Bacillus paramobilis* (type strain RefSeq Assembly Accession GCF_018332495.1) belong to *B. mosaicus* (i.e., *B. paramobilis* is not considered a novel species in the standardized taxonomy)

* All members of *Bacillus hominis* (type strain RefSeq Assembly Accession GCF_018332515.1) belong to *B. mycoides* (i.e., *B. hominis* is not considered a novel species in the standardized taxonomy)

* "*Bacillus arachidis*" (type strain RefSeq Assembly Accession GCF_017498775.1) replaces the putative genomospecies previously referred to as "Unknown Species 17" in the standardized taxonomy

* *Bacillus rhizoplanae* (type strain RefSeq Assembly Accession GCF_917563915.1) represents a novel genomospecies within the standardized taxonomy and has been added to the database

* All members of "*Bacillus pretiosus*" (type strain RefSeq Assembly Accession GCF_025916425.1) belong to *B. mosaicus* (i.e., "*B. pretiosus*" is not considered a novel species in the standardized taxonomy)

**Importantly, *B. cereus* group species are often proposed in the literature using unstandardized approaches** (e.g., varying genomospecies thresholds, which may produce overlapping genomospecies). We have added the type strain comparison method in BTyper3 v3.2.0, as users may still want to compare a query genome with the type strains of published *B. cereus* group species. However, interpret results with caution, as some *B. cereus* group genomes may belong to multiple species using type strain genomes.

For more information, check out our:

* <a href="https://www.tandfonline.com/doi/full/10.1080/10408398.2021.1916735">Review of *B. cereus* group taxonomy/nomenclature</a>

* <a href="https://journals.asm.org/doi/full/10.1128/mBio.00034-20">Standardized nomenclature for the *B. cereus* group</a>

* <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">Comparison of our standardized nomenclature to other *B. cereus* group typing methods (e.g., MLST, *panC*, ANI-based comparisons to species type strain genomes)</a>

------------------------------------------------------------------------

## Citation

### If you found the BTyper3 tool, its source code, and/or any of its associated databases useful, please cite:

Carroll, Laura M., Martin Wiedmann, Jasna Kovac. 2020. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7042689/">"Proposal of a Taxonomic Nomenclature for the *Bacillus cereus* Group Which Reconciles Genomic Definitions of Bacterial Species with Clinical and Industrial Phenotypes."</a> *mBio* 11(1): e00034-20; DOI: 10.1128/mBio.00034-20.

Carroll, Laura M., Rachel A. Cheng, Jasna Kovac. 2020. <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7536271/">"No Assembly Required: Using BTyper3 to Assess the Congruency of a Proposed Taxonomic Framework for the *Bacillus cereus* group with Historical Typing Methods."</a> *Frontiers in Microbiology* 11: 580691; DOI: 10.3389/fmicb.2020.580691.

------------------------------------------------------------------------


## Quick Start

For detailed information, check out the <a href="https://github.com/lmc297/BTyper3/wiki">BTyper3 wiki</a>

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
btyper3 -i /path/to/mlst.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --ani_typestrains False --virulence False --bt False --panC False --download_mlst_latest True
```

#### Perform *panC* group assignment only, using a user-supplied *panC* gene sequence in FASTA format:

```
btyper3 -i /path/to/panC.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --ani_typestrains False --virulence False --bt False --mlst False
```

#### Perform virulence factor and Bt toxin-encoding gene detection in a plasmid sequence in FASTA format:

```
btyper3 -i /path/to/plasmid.fasta -o /path/to/desired/output_directory --ani_species False --ani_subspecies False --ani_typestrains False --mlst False --panC False
```


------------------------------------------------------------------------


Disclaimer: BTyper3 is pretty neat! However, no tool is perfect, and BTyper3 cannot definitively prove whether an isolate is pathogenic or not. As always, interpret your results with caution. We are not responsible for taxonomic misclassifications, misclassifications of an isolate's pathogenic potential or industrial utility, and/or misinterpretations (biological, statistical, or otherwise) of BTyper3 results.
