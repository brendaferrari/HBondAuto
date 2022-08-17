import glob
import os
import re
import numpy as np


class Options:

    def get_hydrogens(self, filename):
        '''get Hydrogens from pdb file'''
        # try to get only hydrogens after nitrogen/ only from specific residues

        hydrogens = []
        try:
            with open(filename, 'r', encoding='utf-8') as pdb_file:
                data = pdb_file.readlines()
                for i, line in enumerate(data):
                    values = line[12:16]

                    if bool(re.search(r'(?<!N|C|O)H', values)) == True:
                        hydrogen = values
                        if hydrogen not in hydrogens:
                            hydrogens.append(hydrogen)

            for i in range(0,(len(hydrogens))):
                x = str(hydrogens[i]).strip(' ')
                hydrogens[i] = x

            hydrogens_to_str = " ".join(str(e) for e in hydrogens)
            hydrogens_code = 'name ' + hydrogens_to_str 
            
        except ValueError:
            raise ValueError("There is no files with pdb extension.")

        return hydrogens_code

    def get_acceptors(self, filename, acceptor_selector):
        '''get acceptors from pdb file'''

        acceptors = []
        try:
            pdb_file = open(filename, 'r', encoding='utf-8')
            for x, line in enumerate(pdb_file):
                values = line[12:16]

                if bool(re.search(acceptor_selector, values)) == True:
                    acceptor = values
                    if acceptor not in acceptors:
                        acceptors.append(acceptor)

            for i in range(0,(len(acceptors))):
                x = str(acceptors[i]).strip(' ')
                acceptors[i] = x

            acceptor_to_str = " ".join(str(e) for e in acceptors)
            acceptors_code = 'name ' + acceptor_to_str 

        except ValueError:
            raise ValueError("There is no files with pdb extension.")        

        return acceptors_code

    def get_important_bonds(self, filename, donor_residues, donor_indexes, acceptor_residues, acceptor_indexes, hbonds):
        '''get only interested bonds'''

        donor_atoms = []
        acceptor_atoms = []
        try:
            pdb_file = open(filename, 'r', encoding='utf-8')
            for x, line in enumerate(pdb_file):
                residues_pdb = line[17:20]
                indexes_pdb = line[24:26]
                atom_n_pdb = line[8:11]

                for donor_residue, donor_index in zip(donor_residues, donor_indexes):
                    if (donor_residue == residues_pdb) and (donor_index == indexes_pdb):
                        data = atom_n_pdb + ' ' + residues_pdb + ' ' + indexes_pdb
                        data_to_str = data.split(' ')
                        donor_atoms.append(data_to_str)
            
                for acceptor_residue, acceptor_index in zip(acceptor_residues, acceptor_indexes):
                    if (acceptor_residue == residues_pdb) and (acceptor_index == indexes_pdb):
                        data = atom_n_pdb + ' ' + residues_pdb + ' ' + indexes_pdb
                        data_to_str = data.split(' ')
                        acceptor_atoms.append(data_to_str)

            important_hbonds_donor = []
            for item in donor_atoms:
                atom_n = np.asarray(item[0], dtype=float) -1
                residues_n = item[1]
                indexes_n = item[2]

                for hb in hbonds: #HYDROGENS
                    donor = hb[1]
                    hydrogen = hb[2]
                    acceptor = hb[3]
                    distance = hb[4]
                    angle_dha = hb[5]
                    if donor == atom_n:
                        important_hbonds_donor.append(hb)

            important_hbonds_donor_arr = np.array(important_hbonds_donor)

            important_hbonds_acceptor = []
            for item in acceptor_atoms:
                atom_n = np.asarray(item[0], dtype=float) -1
                residues_n = item[1]
                indexes_n = item[2]

                for hb in important_hbonds_donor_arr: #HYDROGENS
                    donor = hb[1]
                    hydrogen = hb[2]
                    acceptor = hb[3]
                    distance = hb[4]
                    angle_dha = hb[5]
                    if acceptor == atom_n:
                        important_hbonds_acceptor.append(hb)

            important_hbonds_acceptor_arr = np.array(important_hbonds_acceptor)

        except ValueError:
            raise ValueError("There is no files with pdb extension.") 

        return important_hbonds_acceptor_arr
