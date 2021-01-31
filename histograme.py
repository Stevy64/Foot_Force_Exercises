"""
Exemple de calcul d'histogramme
et de tracé
"""
import doctest
import csv
import numpy as np
from matplotlib import pyplot as plt
import csv
import numpy as np
from matplotlib import pyplot as plt
import wx

my_app = wx.App()
nom_fichier_csv = wx.FileSelector("Fichier de données")# pylint: disable=maybe-no-member
with open(nom_fichier_csv,'r') as fichier:
    tableur = csv.DictReader(fichier, delimiter=';')
    tableau =[]
    for ligne in tableur:
        print(ligne)
        tableau.append([float(ligne['Time (s)']), float(ligne['Linear Acceleration x (m/s^2)']), 
        float(ligne['Linear Acceleration y (m/s^2)']), float(ligne['Linear Acceleration y (m/s^2)']), 
        float(ligne['Linear Acceleration z (m/s^2)']),float(ligne['Absolute acceleration (m/s^2)'])])
    mes_donnees1 = np.array(tableau)[:,1]
    mes_donnees2 = np.array(tableau)[:,2]
    mes_donnees3 = np.array(tableau)[:,3]
    mes_donnees4 = np.array(tableau)[:,4]
   
    # histogramme des valeurs réparties en 5 classes
    histo_donnees, position_classe = np.histogram(mes_donnees1, 12)
    histo_donnees, position_classe = np.histogram(mes_donnees2, 12)
    histo_donnees, position_classe = np.histogram(mes_donnees3, 12)
    histo_donnees, position_classe = np.histogram(mes_donnees4, 12)
    
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
    # tracer de l'histogramme en appelant hist
    ax.hist(position_classe[:-1], position_classe, weights=histo_donnees,edgecolor='black')
    plt.show()
