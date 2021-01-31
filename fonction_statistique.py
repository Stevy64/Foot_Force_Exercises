#!/usr/bin/python
from os import path
import wx
import csv
import numpy as np
from matplotlib import pyplot as plt


def afficher_statistique(dossier, nom_fichier):
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
        temps = donnees[:, 0]
        x = donnees[:, 1]
        y = donnees[:, 2]
        z = donnees[:, 3]
        absolute = donnees[:, 4]

        # Traçage des figures
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle('Statistiques du fichier ' + nom_fichier)

        ax1.plot(temps, x, color='blue')
        ax1.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[1])
        # ax1.grid(True)
        ax2.plot(temps, y, color='blue')
        ax2.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[2])
        # ax1.grid(True)
        ax3.plot(temps, z, color='blue')
        ax3.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[3])

        ax4.plot(temps, absolute, color='blue')
        ax4.set(xlabel=tableur.fieldnames[0], ylabel=tableur.fieldnames[4])

        for ax in fig.get_axes():
            ax.label_outer()

        moyenne_x = np.mean(x)
        moyenne_y = np.mean(y)
        moyenne_z = np.mean(z)
        moyenne_abs = np.mean(absolute)

        ecart_type_x = np.std(x)
        ecart_type_y = np.std(y)
        ecart_type_z = np.std(z)
        ecart_type_abs = np.std(absolute)
        
        ax1.hlines(moyenne_x, np.min(temps), np.max(temps),
                colors='red', linestyles='dashed')
        ax1.hlines(moyenne_x - ecart_type_x, np.min(temps), np.max(temps),
                colors='yellow', linestyles='dotted')
        ax1.hlines(moyenne_x + ecart_type_x, np.min(temps), np.max(temps),
                colors='green', linestyles='dotted',)
        ax1.legend(['accélération en x(t)', 'moyenne(m)', 'm-s', 'm+s'])
        
        ax2.hlines(moyenne_y, np.min(temps), np.max(temps),
                colors='red', linestyles='dashed')
        ax2.hlines(moyenne_y - ecart_type_y, np.min(temps), np.max(temps),
                colors='yellow', linestyles='dotted')
        ax2.hlines(moyenne_y + ecart_type_y, np.min(temps), np.max(temps),
                colors='green', linestyles='dotted',)
        ax2.legend(['accélération en y(t)', 'moyenne(m)', 'm-s', 'm+s'])
        
        ax3.hlines(moyenne_z, np.min(temps), np.max(temps),
                colors='red', linestyles='dashed')
        ax3.hlines(moyenne_z - ecart_type_z, np.min(temps), np.max(temps),
                colors='yellow', linestyles='dotted')
        ax3.hlines(moyenne_z + ecart_type_z, np.min(temps), np.max(temps),
                colors='green', linestyles='dotted',)  
        ax3.legend(['accélération en z(t)', 'moyenne(m)', 'm-s', 'm+s'])        
                
        ax4.hlines(moyenne_abs, np.min(temps), np.max(temps),
                colors='red', linestyles='dashed')
        ax4.hlines(moyenne_abs - ecart_type_abs, np.min(temps), np.max(temps),
                colors='yellow', linestyles='dotted')
        ax4.hlines(moyenne_abs + ecart_type_abs, np.min(temps), np.max(temps),
                colors='green', linestyles='dotted',)
        ax4.legend(['accélération absolue(t)', 'moyenne(m)', 'm-s', 'm+s'])

        plt.autoscale(enable=True, axis=u'both', tight=False)
        plt.show()