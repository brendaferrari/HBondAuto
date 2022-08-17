🔴❗UNDER DEVELOPMENT❗🔴

# Hydrogen bond analysis automation (HBondAuto)

HBondAuto is a program developed to calculate and automate the hydrogen bond analysis in Molecular Dynamics Simulations.

<img src="images\example.png">

Up until now the program is able to:
* Calculate the hydrogen bonds in the system through simulation time
* Calculate the hydrogen bonds in specific residues of interest: Up until three.
* Plot the hydrogen bonds in specific residues of interest

In future updates:
* Plot all the hydrogen bonds

---
## Instalation

Download the code and unzip it on the desirable directory. To prepare the environment use the following command:

```
conda env create -f environment.yml
``` 

Be aware to uncomment the sections on the environment.yml file depending on which OS you are using.

---
## How to use

To calculate the hydrogen bonds this program needs the protein file (pdb), with only the protein, and the trajectory file (xtc) with only the protein atoms (please use *gmx make_ndx -f md_protein-only.pdb -o index.ndx* to create an index and *gmx trjconv -f md.xtc -o md_protein-only.xtc -n index.ndx* to get only the protein trajectory). **Do not use the noPBC file in this analysis**.

Modify line 47 to add the residues of interest:
```
# Modify here the residues of interest
residues = {'donor_residues':[["PHE"],["GLY"],["GLN"]],
            'donor_indexes':[["28"],["32"],["33"]],
            'acceptor_residues':[["ALA"],["ASN"],["ASN"]],
            'acceptor_indexes':[["23"],["30"],["30"]]}
```

Activate the environment using:

```
conda activate hbondanalysis
```

The program uses a shell script to automate the calculation of data in multiple folders. To use this feature go to the root directory and on the terminal use:

```
bash \hbondauto.sh
```

If you are interested only on running one folder, you may just add your files to the [HBondAuto directory](HBondAuto/) and use:

```
python analysis.py
```

---
## Observations

* This script was developed following some steps on the 
MDAnalysis tutorial for calculating hydrogen bonds. The tutorial can be found [here](https://userguide.mdanalysis.org/dev/examples/analysis/hydrogen_bonds/hbonds.html).

---
## Authorship

* Author: **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))

Social preview original photo by **Brenda Ferrari** ([brendaferrari](https://github.com/brendaferrari))
