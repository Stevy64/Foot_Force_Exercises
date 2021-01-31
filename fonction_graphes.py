#!/usr/bin/python
from os import path
import wx
import csv
import numpy as np
from matplotlib import pyplot as plt
import wxmplot.interactive as wi

def tracer_graphes(dossier, nom_fichier):
    with open(path.join(dossier, nom_fichier),'r') as fichier:
        tableur = csv.DictReader(fichier, delimiter=';')
        tableau =[]
        for ligne in tableur:
            tableau.append([float(ligne['Time (s)']), float(ligne['Linear Acceleration x (m/s^2)']), 
            float(ligne['Linear Acceleration y (m/s^2)']), 
            float(ligne['Linear Acceleration z (m/s^2)']), 
            float(ligne['Absolute acceleration (m/s^2)'])])
            
        for ligne in tableau:
            print(ligne)
        
        donnees = np.array(tableau)
        time = donnees[:, 0]
        x = donnees[:, 1]
        y = donnees[:, 2]
        z = donnees[:, 3]
        absolute = donnees[:, 4]

        # Traçage des figures
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle('Graphe du fichier ' + nom_fichier)

        ax1.plot(time, x, color='red')
        ax1.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[1])
        # ax1.grid(True)
        ax2.plot(time, y, color='blue')
        ax2.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[2])
        # ax1.grid(True)
        ax3.plot(time, z, color='green')
        ax3.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[3])

        ax4.plot(time, absolute, color='yellow')
        ax4.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[4])
        
        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.show()

        for ax in fig.get_axes():
            ax.label_outer()
       
