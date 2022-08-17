import numpy as np
import matplotlib.pyplot as plt
from functools import reduce 



class Plot:

    def plot_hbonds(self):
        # plot all hbonds
        return

    def plot_important_hbonds(self, hbonds1, hbonds2, hbonds3, donor_residues, donor_indexes, acceptor_residues, acceptor_indexes, timeframe_beg, timeframe_end):
        # plot only interested hbonds

        if np.any(hbonds2) and np.any(hbonds3):
            print('a')
            times1 = hbonds1[:,0]
            times2 = hbonds2[:,0]
            times3 = hbonds3[:,0]
            t1 = times1[timeframe_beg:timeframe_end]
            t2 = times2[timeframe_beg:timeframe_end]
            t3 = times3[timeframe_beg:timeframe_end]
            fig, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(20,7))
            fig.suptitle("hydrogen bonds interaction between aminoacids", fontsize=14)
            ax1.set_title(f'Hydrogen bonds between {donor_residues[0], donor_indexes[0]} and {acceptor_residues[0], acceptor_indexes[0]}')
            ax1.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax1.tick_params(left=False)
            ax1.set_ylim([0, 2])
            ax1.set_xlim([timeframe_beg, timeframe_end])
            ax1.eventplot(t1, color="black")

            ax2.set_title(f'Hydrogen bonds between {donor_residues[1], donor_indexes[1]} and {acceptor_residues[1], acceptor_indexes[1]}')
            ax2.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax2.tick_params(left=False)
            ax2.set_ylim([0, 2])
            ax2.set_xlim([timeframe_beg, timeframe_end])
            ax2.eventplot(t2, color="black")

            ax3.set_title(f'Hydrogen bonds between {donor_residues[2], donor_indexes[2]} and {acceptor_residues[2], acceptor_indexes[2]}')
            ax3.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax3.tick_params(left=False)
            ax3.set_ylim([0, 2])
            ax3.set_xlim([timeframe_beg, timeframe_end])
            ax3.eventplot(t3, color="black")

            plt.savefig('hbond.png')

        if np.any(hbonds2) and not np.any(hbonds3):
            print('b')
            times1 = hbonds1[:,0]
            times2 = hbonds2[:,0]
            t1 = times1[timeframe_beg:timeframe_end]
            t2 = times2[timeframe_beg:timeframe_end]
            fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,7))
            ax1.set_title(f'Hydrogen bonds between {donor_residues[0], donor_indexes[0]} and {acceptor_residues[0], acceptor_indexes[0]}')
            ax1.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax1.tick_params(left=False)
            ax1.set_ylim([0, 2])
            ax1.set_xlim([timeframe_beg, timeframe_end])
            ax1.eventplot(t1, color="black")

            ax2.set_title(f'Hydrogen bonds between {donor_residues[1], donor_indexes[1]} and {acceptor_residues[1], acceptor_indexes[1]}')
            ax2.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax2.tick_params(left=False)
            ax2.set_ylim([0, 2])
            ax2.set_xlim([timeframe_beg, timeframe_end])
            ax2.eventplot(t2, color="black")

            plt.savefig('hbond.png')

        if not np.any(hbonds2):
            print('c')
            times1 = hbonds1[:,0]
            t1 = times1[timeframe_beg:timeframe_end]
            fig, ax1 = plt.subplots(1,1,figsize=(7,7))
            ax1.set_title(f'Hydrogen bonds between {donor_residues[0], donor_indexes[0]} and {acceptor_residues[0], acceptor_indexes[0]}')
            ax1.set(xlabel="Simulation time (ns)",ylabel=None, yticklabels=[])
            ax1.tick_params(left=False)
            ax1.set_ylim([0, 2])
            ax1.set_xlim([timeframe_beg, timeframe_end])
            ax1.eventplot(t1, color="black")

            plt.savefig('hbond.png')

        return
