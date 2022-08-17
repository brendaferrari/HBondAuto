import pickle
import numpy as np
np.set_printoptions(linewidth=100)
import pandas as pd

import matplotlib.pyplot as plt

import MDAnalysis as mda
from MDAnalysis.analysis.hydrogenbonds import HydrogenBondAnalysis

from options import Options
from plot import Plot

protein = 'md_protein-only.pdb'
trajectory = 'md_protein-only.xtc'

u = mda.Universe(protein, trajectory, guess_bonds=True)

opt = Options()
hydrogens = opt.get_hydrogens(filename=protein)
print(hydrogens)

acceptors = opt.get_acceptors(filename=protein, acceptor_selector='O')
print(acceptors)

hbonds = HydrogenBondAnalysis(
    universe=u,
    donors_sel=None,
    hydrogens_sel=hydrogens,
    acceptors_sel=acceptors,
    d_a_cutoff=3.0,
    d_h_a_angle_cutoff=150,
    update_selections=False
)

hbonds.run(
    start=None,
    stop=None,
    step=None,
    verbose=True
)

results = hbonds.results.hbonds
print(hbonds.results.hbonds[20])

# Modify here the residues of interest
residues = {'donor_residues':[["PHE"],["GLY"],["GLN"]],
            'donor_indexes':[["28"],["32"],["33"]],
            'acceptor_residues':[["ALA"],["ASN"],["ASN"]],
            'acceptor_indexes':[["23"],["30"],["30"]]}

print(residues['donor_residues'])
try:
    bonds1 = opt.get_important_bonds(filename=protein, donor_residues=residues['donor_residues'][0], 
                                    donor_indexes=residues['donor_indexes'][0],
                                    acceptor_residues=residues['acceptor_residues'][0], 
                                    acceptor_indexes=residues['acceptor_indexes'][0], 
                                    hbonds=results)
except IndexError():
    print(f'No hydrogen bonds were found for residues in bonds1')

try:
    bonds2 = opt.get_important_bonds(filename=protein, donor_residues=residues['donor_residues'][1], 
                                    donor_indexes=residues['donor_indexes'][1],
                                    acceptor_residues=residues['acceptor_residues'][1], 
                                    acceptor_indexes=residues['acceptor_indexes'][1], 
                                    hbonds=results)
except IndexError():
    print(f'No hydrogen bonds were found for residues in bonds2')

try:
    bonds3 = opt.get_important_bonds(filename=protein, donor_residues=residues['donor_residues'][2], 
                                    donor_indexes=residues['donor_indexes'][2],
                                    acceptor_residues=residues['acceptor_residues'][2], 
                                    acceptor_indexes=residues['acceptor_indexes'][2], 
                                    hbonds=results)
except IndexError():
    print(f'No hydrogen bonds were found for residues in bonds2')

plot = Plot()

if bonds1.size > 0 and bonds2.size > 0 and bonds3.size > 0:
    plotbond = plot.plot_important_hbonds(bonds1, bonds2, bonds3, residues['donor_residues'], residues['donor_indexes'],
                                            residues['acceptor_residues'], residues['acceptor_indexes'],
                                            timeframe_beg=0, timeframe_end=10000)

elif bonds1.size > 0 and bonds2.size > 0 and bonds3.size == 0:
    plotbond = plot.plot_important_hbonds(bonds1, bonds2, None, residues['donor_residues'], residues['donor_indexes'],
                                            residues['acceptor_residues'], residues['acceptor_indexes'],
                                            timeframe_beg=0, timeframe_end=10000)

elif bonds1.size > 0 and bonds2.size == 0 and bonds3.size == 0:
    plotbond = plot.plot_important_hbonds(bonds1, None, None, residues['donor_residues'], residues['donor_indexes'],
                                            residues['acceptor_residues'], residues['acceptor_indexes'],
                                            timeframe_beg=0, timeframe_end=10000)

else:
    print(f'No hydrogen bonds observed for this residues.')