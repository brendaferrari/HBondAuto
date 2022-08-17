#!/bin/bash

echo starting HBondAuto;

for dir in input/*; 

do cp HBondAuto/{analysis.py,options.py,plot.py} "$dir";

cd "$dir";

shopt -s extglob;

if ls -l *.{pdb,xtc};

then echo Starting "${dir##*/}" HBondAuto;

python analysis.py; 

rm -f {analysis.py,options.py,plot.py,*.xtc_offsets.lock,*xtc_offsets.npz};

cd ../..;

echo "${dir##*/}" HBondAuto ended;

else echo No .pdb or .xtc files on directory. Please verify; 

cd ../..; fi; done