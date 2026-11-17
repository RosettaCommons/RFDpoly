# RFDpoly tutorials

Interactive Colab notebooks that walk through RFDpoly inference. Each one installs the
apptainer container and downloads model weights into the Colab session, so no local
install is needed — but the container is large, and the setup cell takes a while.

A GPU runtime is recommended (**Runtime → Change runtime type → GPU**).

| Notebook | What it covers |
| --- | --- |
| [**Demo 1: general design**](https://colab.research.google.com/github/RosettaCommons/RFDpoly/blob/main/tutorials/demo01_general_design.ipynb) | Polymer-class contigs, sequence–structure codesign, nucleic acid secondary structure conditioning (dot-bracket strings, paired-region lists, symmetry, strand orientation, multi-base contacts), and motif scaffolding of DNA-binding proteins. |
| [**Demo 2: ensemble modeling**](https://colab.research.google.com/github/RosettaCommons/RFDpoly/blob/main/tutorials/demo02_ensemble_modeling.ipynb) | Motif scaffolding around a nucleotide ligand, conformational ensemble generation by partial diffusion, and multi-state sequence design with tied NA-MPNN. |

Demo 2 assumes you have worked through demo 1, which covers installation and the basic
inference syntax.

For a text reference covering the same arguments in more depth, see
[`RFDpoly_tutorial.pdf`](../RFDpoly_tutorial.pdf) and the
[online documentation](https://rosettacommons.github.io/RFDpoly/).

To save your work, save a copy of the notebook into your own Google Drive before editing it.
