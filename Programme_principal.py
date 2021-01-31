#!/usr/bin/python
from os import path
import wx
import csv
import numpy as np
from matplotlib import pyplot as plt
import wxmplot
from fonction_statistique import afficher_statistique
from fonction_graphes import tracer_graphes
from fonction_histogramme import afficher_histogramme

directory_path = ""

class MyFrame(wx.Frame):
    

    def __init__(self):
        super().__init__(parent=None, title='Kenny - Programme')
        self.installer_menu()
        panel = wx.Panel(self)
        panel.SetBackgroundColour((50, 51, 102, 100))
        vbox = wx.BoxSizer(wx.VERTICAL) 

        self.text_ctrl = wx.TextCtrl(panel)
        self.text_ctrl.SetLabel('Experience_')
        vbox.Add(self.text_ctrl, 0, wx.ALIGN_CENTER)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)          
        graph_btn = wx.Button(panel, label='Graphes')
        hbox.Add(graph_btn, 4, wx.ALL | wx.ALIGN_CENTER, 5)
        graph_btn.Bind(wx.EVT_BUTTON, self.on_press_graph)
        graph_btn.SetBackgroundColour((0, 210, 201, 100))

        histo_btn = wx.Button(panel, label='Histogramme')
        hbox.Add(histo_btn, 4, wx.ALL | wx.ALIGN_CENTER, 5)
        histo_btn.Bind(wx.EVT_BUTTON, self.on_press_histo)
        histo_btn.SetBackgroundColour((0, 230, 210, 100))

        stat_btn = wx.Button(panel, label='Statistiques')
        hbox.Add(stat_btn, 4, wx.ALL | wx.ALIGN_CENTER, 5)  
        stat_btn.Bind(wx.EVT_BUTTON, self.on_press_stat)
        stat_btn.SetBackgroundColour((0, 230, 210, 100))

        vbox.Add(hbox, 1, wx.ALIGN_CENTER)       
        panel.SetSizer(vbox)
        
        self.Show()
        self.Centre() 
        self.Fit()
    
    def installer_menu(self):
        barre_menu = wx.MenuBar()
        menu_fichier = wx.Menu()
        ouvrir_experience = menu_fichier.Append(wx.ID_ABOUT, 'Ouvrir une expérience', 'Ouvrir une expérience')
        barre_menu.Append(menu_fichier, '&Fichier')
        self.SetMenuBar(barre_menu)
        self.Bind(wx.EVT_MENU, self.Ouvrir_Fichier, ouvrir_experience)

    def Ouvrir_Fichier(self, e):
        global directory_path
        nom_fichier_csv = wx.FileSelector("Experience")
        directory_path, nom_fichier_csv = path.split(nom_fichier_csv)
        index_fin = nom_fichier_csv.find('.csv')
        nom_fichier = nom_fichier_csv[:index_fin]
        self.text_ctrl.SetValue(nom_fichier)
        print("Ouverture Expérience.csv path-- ", directory_path)
        print("Ouverture Expérience.csv nom_fichier-- ", nom_fichier)


    def on_press_graph(self, event):
        experience = self.text_ctrl.GetValue()
        global directory_path
        if experience not in ['Experience_' + str(i) for i in range(1, 11)] :
            wx.MessageBox('Veuillez entrer un nom correct pour afficher les graphes (Ex : Experience_1)', 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            if directory_path != "":
                thisdir = directory_path
            else:
                thisdir, file_name = path.split(__file__)
            tracer_graphes(thisdir + "/Experiences", experience + '.csv')
    
    def on_press_histo(self, event):
        experience = self.text_ctrl.GetValue()
        if experience not in ['Experience_' + str(i) for i in range(1, 11)] :
            wx.MessageBox('Veuillez entrer un nom correct pour afficher son histogramme (Ex : Experience_2)', 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            if directory_path != "":
                thisdir = directory_path
            else:
                thisdir, file_name = path.split(__file__)
            afficher_histogramme(thisdir + "/Experiences", experience + '.csv')
    
    def on_press_stat(self, event):
        experience = self.text_ctrl.GetValue()
        if experience not in ['Experience_' + str(i) for i in range(1, 11)] :
            wx.MessageBox('Veuillez entrer un nom correct pour afficher ses statistiques (Ex : Experience_3)', 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            if directory_path != "":
                thisdir = directory_path
            else:
                thisdir, file_name = path.split(__file__)
            afficher_statistique(thisdir + "/Experiences", experience + '.csv')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()