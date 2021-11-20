# BTyper3 CHANGELOG

All noteable changes to BTyper3 will be documented in this file

## [3.2.0] 2021-04-12
### Added
- Added `--ani_typestrains` option to `btyper3`, which allows users to compare a query *B. cereus* group genome to the type strain genomes of all published *B. cereus* group species in the literature; this options calculates ANI values between the query genome and the genomes of all published *B. cereus* group species type strains and reports the type strain that produces the highest ANI value. 
- Added `typestrains-only` database to `build_btyper3_ani_db.py`, which allows users to download the type strain genomes of all published *B. cereus* group species; this database is used with the `--ani_typestrains` in `btyper3`. Type strain genomes correspond to the <a href="https://www.tandfonline.com/doi/full/10.1080/10408398.2021.1916735">species discussed in Figure 2 of our taxonomy review</a>, plus <a href="https://pubmed.ncbi.nlm.nih.gov/34494947/">three species</a> published after the review was published.

## [3.1.2] 2021-04-12
### Changed
- Fixed an indentation typo in `download_pubmlst_latest.py` so that `xml` could properly parse the PubMLST xml

## [3.1.1] 2020-10-25
### Added
- Added `download_pubmlst_latest.py` script, which users can run to download latest PubMLST database for *Bacillus cereus*, independently of executing the `btyper3` program

### Changed
- Updated `--download_mlst_latest` portion of `btyper3` code to be compatible with changes to <a href="https://pubmlst.org/data/dbases.xml">PubMLST's XML</a> format; recent changes made by PubMLST to the filenames in the XML caused previous versions of BTyper3 to produce an error and not download the database

### Removed
- Removed <a href="https://mbio.asm.org/content/11/1/e00034-20">Unknown Species 14</a> from the species reference genomes used for genomospecies assignment; using recent genomes submitted to NCBI (accessed 2020-05-14), Unknown Species 14 was found to overlap with *B. luti* at a 92.5 ANI threshold (see genomes with NCBI RefSeq Assembly Accessions GCF_008764075.1, GCF_007667455.1, and GCF_007673665.1, which were assigned to both *B. luti* and Unknown Species 14 at a 92.5 ANI threshold); Unknown Species 14 was therefore merged into *B. luti* in BTyper3 v. 3.1.1

## [3.1.0] 2020-06-28
### Added
- Added <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">*in silico* seven-gene multi-locus sequence typing (MLST)</a>, using PubMLST's scheme for *Bacillus cereus*
- Added <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">*panC* group assignment</a> using an eight-group *panC* group assignment framework
- Added <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">virulence factor detection</a> for additional virulence factors (i.e., toxin genes associated with diarrheal *Bacillus cereus* illness, and genes associated with capsule production)
- Added <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">average-nucleotide identity (ANI)-based pseudo-gene flow unit assignment method</a>

### Changed
- Changed <a href="https://www.frontiersin.org/articles/10.3389/fmicb.2020.580691/full">default virulence factor detection thresholds to 70 and 80% amino acid identity and coverage, respectively</a>

## [3.0.2] 2019-11-18
### Changed
- Swapped anthrax and cereulide column names in final results file (previously, the column header for anthrax genes was above cereulide synthetase genes in the final results file, and vice versa; the typo was thus fixed)
- Edited the README to convey that BLAST+ version 2.10.0 is not compatible with BTyper3

## [3.0.1] 2019-10-05
### Changed
- Changed default percent amino acid identity for virulence gene detection and Bt toxin gene detection from 70% to 50% to be compatible with what was reported in the <a href="https://www.biorxiv.org/content/10.1101/779199v1">preprint</a>
- Fixed pandas.read_csv error which would occur when no fastANI and/or BLAST output file would be produced, or when a file was empty
- Fixed error which would occur when printing final output files when ```--virulence False``` or ```--bt False```; when these typing methods were not performed, the final output file would treat the string which designated that these typing methods were not performed as a list

## [3.0.0] 2019-09-22
### Added
- Initial commit of BTyper3

