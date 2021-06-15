import sys
import os
 
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QFileSystemModel, QTreeView, 
                             QFrame, QGridLayout, QMainWindow)
 
##############################################################################
class NavigFichiers(QMainWindow):
 
    #=========================================================================
    def __init__(self, repertoire, parent=None):
        super().__init__(parent)
 
        self.resize(800, 200)
        self.move(364,500)
        self.setWindowTitle("Navigateur de fichiers")
 
        # crée le modèle
        model = QFileSystemModel()
        model.setRootPath(repertoire)
 
        #Crée le QTreeView et intégre le modèle
        self.view = QTreeView()
        self.view.setModel(model)
        self.view.setRootIndex(model.index(repertoire))
 
        # Police de caractères à utiliser
        font = QFont()
        font.setStyleHint(QFont.Monospace)
        self.view.setFont(font)
 
        # largeur de la colonne 0
        self.view.setColumnWidth(0, 350)
 
        # place le QTreeView dans la fenêtre
        self.setCentralWidget(QFrame())
        layout = QGridLayout()
        layout.addWidget(self.view, 0, 0)
        self.centralWidget().setLayout(layout)
 
        # Etablissement lien entre signal et méthode
        self.view.doubleClicked.connect(self.clicligne)
 
    #=========================================================================
    def clicligne(self, qindex):
 
        nom = self.view.model().fileName(qindex)
        chemin =  self.view.model().filePath(qindex)
        if os.path.isdir(chemin):
            print("Répertoire:", nom, "===> avec chemin:", chemin)
        else:
            print("fichier:", nom, "===> avec chemin:", chemin)
            os.popen("vlc '"+chemin+"'")
 
