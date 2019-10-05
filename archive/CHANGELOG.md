# BTyper3 CHANGELOG

All noteable changes to BTyper3 will be documented in this file

## [3.0.1] 2019-10-05
### Changed
- Changed default percent amino acid identity for virulence gene detection and Bt toxin gene detection from 70% to 50% to be compatible with what was reported in the <a href="https://www.biorxiv.org/content/10.1101/779199v1">preprint</a>
- Fixed pandas.read_csv error which would occur when no fastANI and/or BLAST output file would be produced, or when a file was empty
- Fixed error which would occur when printing final output files when ```--virulence False``` or ```--bt False```; when these typing methods were not performed, the final output file would treat the string which designated that these typing methods were not performed as a list

## [3.0.0] 2019-09-22
### Added
- Initial commit of BTyper3

