import glob
import os
import re


class Options:

    def get_hydrogens(self):
        '''get Hydrogens from pdb file'''
        # try to gt only hydrogens after nitrogen/ only from specific residues

        hydrogens = []
        try:
            print(os.getcwd())
            os.chdir('../')
            for file in glob.glob('*.pdb'):
                fileName = re.sub('.pdb', '', file)

                with open(file, 'r', encoding='utf-8') as pdb_file:
                    data = pdb_file.readlines()
                    for i, line in enumerate(data):
                        values = line[12:16]
                        #print(values)

                        if bool(re.search(r'(?<!N|C|O)H', values)) == True:
                            hydrogen = values
                            if hydrogen not in hydrogens:
                                hydrogens.append(hydrogen)

            for i in range(0,(len(hydrogens))):
                x = str(hydrogens[i]).strip(' ')
                hydrogens[i] = x
            
            os.chdir('HBondAuto')

        except ValueError:
            raise ValueError("There is no files with pdb extension.")

        return hydrogens

    def get_acceptors(self, acceptor_selector):

        acceptors = []
        try:
            os.chdir('../')
            for file in glob.glob('*.pdb'):
                fileName = re.sub('.pdb', '', file)

                pdb_file = open(file, 'r', encoding='utf-8')
                for x, line in enumerate(pdb_file):
                    values = line[12:16]
                    #print(values)

                    if bool(re.search(acceptor_selector, values)) == True:
                        acceptor = values
                        if acceptor not in acceptors:
                            acceptors.append(acceptor)

            for i in range(0,(len(acceptors))):
                x = str(acceptors[i]).strip(' ')
                acceptors[i] = x

            os.chdir('HBondAuto')

        except ValueError:
            raise ValueError("There is no files with pdb extension.")        

        return acceptors

    def get_important_bonds():
        # get only interested bonds
        return
