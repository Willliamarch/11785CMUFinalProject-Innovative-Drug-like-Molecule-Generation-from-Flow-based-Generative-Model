# 11785CMU_Final_Project_Innovative-Drug-like-Molecule-Generation-from-Flow-based-Generative-Model
 
1. Dataset downloaded
scPDB: http://bioinfo-pharma.u-strasbg.fr/scPDB/
CrossDocked2020: (datasets and related packages) https://github.com/gnina

2. Preprocessing
It is only for scPDB.
Firstly, make sure you have the following packages:
Biopython, prody, py3dmol
Biopython:
$ pip install biopython
$ pip install biopython --upgrade
prody:
$ pip install -U ProDy
or
$ tar -xzf ProDy-2.0.tar.gz
$ cd ProDy-2.0
$ python setup.py build
$ sudo python setup.py install
py3dmol:
pip install py3Dmol
In dataset, list of scPDB is in "scPDB.txt" file. Run GetPDB_info.py, you can download all information about scPDB.
Then, run class_readPDB.py, you can get final txt file including BindingSites_ID_basedLIgand.txt, and BindingStrength_affinity.txt
After downloaded all datasets, run Permutation_test/Protein_assembly_beta.py to rebuild structures based on B-factors and biological aseemblies.

3. Evaluate binding affinity
Using BindingStrength_affinity.txt, using prodigy server to predict binding affinity.
Downloaded in: https://github.com/haddocking/prodigy

4. Training model and molecule generation:
The tutorial for both models have been included in their GitHub Readme file.
GraphBP: https://github.com/divelab/GraphBP
liGAN: https://github.com/mattragoza/LiGAN
The best model we trained is in the "Model" directory. The training loss for each model is in "Results" directory

5. Validity
In "Validity_check" file. You need to use python2.7 as your environment and download rdkit package.
$ conda create -c conda-forge -n my-rdkit-env rdkit python=2.7
$ conda activate my-rdkit-env
$ cd [anaconda folder]/bin
$ source activate my-rdkit-env
$ conda install numpy matplotlib
$ conda install cmake cairo pillow eigen pkg-config
$ conda install boost-cpp boost py-boost
Then, use Check_Validity.py by using your generated small molecule SMILE string and it will return if the SMILE string is valid.

6. Generated small molecules
In the directory "Generated_molecules", there are 3 files including protein structures, binding pockets, and generated small molecules.
You can check the structure by using VMD or pymol.
To install VMD: https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD
To install pymol: https://pymol.org/2/

