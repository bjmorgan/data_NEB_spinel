# Dataset for &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo;

Authors:  
- C. O'Rourke ORCID:  0000-0002-0703-8234 
- B. J. Morgan ORCID: 0000-0002-3056-8233

## Summary

This repository contains the data analysis and plotting code that supports findings reported in 

C. O’Rourke and B. J. Morgan, &ldquo;Interfacial Strain Effects on Lithium Diffusion Pathways in the Spinel Solid Electrolyte Li-Doped MgAl<sub>2</sub>O<sub>4</sub>&rdquo;, T.B.D.

The repository consists of
1. Input and output files for a series of VASP calculations.
2. A series of Python command-line scripts for extracting relevant data from these DFT calculations, and collating them in .csv files.
3. A Jupyter notebook that constructs the figures in the manuscript from the .csv data.

## Overview

This top level directory contains three sub-directories `data`, `analysis` and `figures`. 
 
* **`data/`**: This folder contains the necessary input data to reproduce the VASP calculations that support this work, along with their outputs. Also included are several Python scripts that traverse the data folders, stripping out the data presented within the main manuscript into `.csv` format. A `README.md` file in this subfolder describes the layout of the data folder and files therein.

* **`analysis/`**: In this folder the `.csv` files from the `data` folder are analysed and the figures in the main manuscript produced. A Jupyter notebook is included (`spinel_paper_generating_figures.ipynb`),  which performs the necessary analysis and produces the figures.

* **`figure/`**: Folder containing the manuscript figures produced by the analysis script.

To produce the figures in the manuscript, the scripts in the `data` folder can be run to extract the relevant data from the VASP outputs into `.csv` format. Then the Jupyter notebook in the `analysis` folder can be run to produce the files found in the `figures` folder.

## Testing

The repository contains tests that the analysis notebooks execute without errors. This happend [here](TODO).
