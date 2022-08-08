🔴❗UNDER DEVELOPMENT❗🔴

# Hydrogen bond analysis automation (HBondAuto)


---
## Instalation

Download the code and unzip it on the desirable directory. To prepare the environment use the following command:

```
conda env create -f environment.yml
``` 

Be aware to uncomment the sections on the environment.yml file depending on which OS you are using.

---
## How to use

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
