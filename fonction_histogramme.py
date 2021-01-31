#!/usr/bin/python
from os import path
import wx
import csv
import numpy as np
from matplotlib import pyplot as plt
import wxmplot.interactive as wi


def afficher_histogramme(dossier, nom_fichier):
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
        x = donnees[:, 1]
        y = donnees[:, 2]
        z = donnees[:, 3]
        absolute = donnees[:, 4]

        # histogramme des valeurs réparties en 12 classes
        histo_donnees, position_classe = np.histogram(x, 100)
        histo_donnees, position_classe = np.histogram(y, 100)
        histo_donnees, position_classe = np.histogram(z, 100)
        histo_donnees, position_classe = np.histogram(absolute, 100)
        
        print ("Classe : ", position_classe)
        print ("Nombre de valeurs dans chaque classe : ", histo_donnees)
        for idx in range(len(histo_donnees)-1):
            print("Dans l'intervalle ",idx," = [",
                position_classe[idx],", ",position_classe[idx+1],"[",
                " il y a ", histo_donnees[idx]," valeurs")
        print("Intervalle ",len(histo_donnees)-1," = [",
            position_classe[len(histo_donnees)-1],", ",position_classe[len(histo_donnees)],"]",
            " il y a ", histo_donnees[len(histo_donnees)-1]," valeurs")
        fig, ax = plt.subplots(nrows=1, ncols=1)
        fig.suptitle('Histogramme du fichier ' + nom_fichier)

        # tracer de l'histogramme en appelant hist
        ax.hist(position_classe[:-1], position_classe, weights=histo_donnees,edgecolor='black')
        plt.show()
