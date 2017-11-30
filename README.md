# Data Analysis for &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo;

Authors:  
- C. O'Rourke ORCID:  0000-0002-0703-8234 
- B. J. Morgan ORCID: 0000-0002-3056-8233

[![CircleCI](https://circleci.com/gh/bjmorgan/data_NEB_spinel.svg?style=shield&circle-token=858a87f5298c9e6fc09a308ffa0d66652907dc82)](https://circleci.com/gh/bjmorgan/data_NEB_spinel)
[![DOI](https://zenodo.org/badge/112021402.svg)](https://zenodo.org/badge/latestdoi/112021402)

## Summary

This repository contains data analysis that supports the findings reported in 
C. O’Rourke and B. J. Morgan, &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo;,
and code for plotting figures in this paper.

The repository consists of
1. A series of .csv files, containing data extracted from VASP calculations. The inputs and outputs for the source VASP calculations, along with scripts for extracting the relevant data, are available at the [University of Bath Data Archive](https://dx.doi.org/10.15125/BATH-00438).
2. A Jupyter notebook that constructs the figures in the manuscript from the .csv data. The analysis notebook can be viewed [here](https://nbviewer.jupyter.org/github/bjmorgan/data_NEB_spinel/blob/master/analysis/spinel_paper_generating_figures.ipynb).

## Overview

This top level directory contains three sub-directories `data`, `analysis` and `figures`. 
 
* **`data/`**: This folder contains a series of `.csv` files, containing data extracted from VASP calculations. The inputs and outputs for the source VASP calculations, along with scripts for extracting the relevant data to generate these files, are available at the [University of Bath Data Archive](https://dx.doi.org/10.15125/BATH-00438).

* **`analysis/`**: In this folder the `.csv` files from the `data` folder are analysed and the figures in the main manuscript produced. A Jupyter notebook is included (`spinel_paper_generating_figures.ipynb`),  which performs the necessary analysis and produces the figures.

* **`figure/`**: This folder contains the manuscript figures produced by the analysis script.

To produce the figures in the manuscript, the Jupyter notebook in the `analysis` folder can be run to produce the files found in the `figures` folder.

## Dependencies

Python dependencies are listed in the [`requirements.txt`](requirements.txt) file.

## Testing

The repository contains tests that the analysis notebooks execute without errors. This happens [here](https://circleci.com/gh/bjmorgan/data_NEB_spinel).

To manually run the tests, run
```
python -m unittest discover
```

## References

1. C. O’Rourke and B. J. Morgan, &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo; [source](https://github.com/connorourke/Spinel-Paper).  
2. C. O'Rourke and B. J. Morgan, &ldquo;DFT Dataset for &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo; &rdquo; [University of Bath Research Data Archive](https://dx.doi.org/10.15125/BATH-00438).
