#Program fully write by Manolo RAJAONAH
import sys
from PyQt5 import QtCore, QtWidgets, uic
import cv2
from PyQt5.QtWidgets import QApplication, QLabel
import os
from AcceuilWindow import Ui_AcceuilWindow

from ssim import *
from matplotlib import pyplot as plt
import class_app
from class_app import *

from record_cover import *
from record_secret import *

from gi.repository import Gdk
from afficher_dossier import *


class AcceuilWindow(QtWidgets.QMainWindow, Ui_AcceuilWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(AcceuilWindow, self).__init__(*args, **kwargs)
        
        # this will hide the title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        

    def acceuilBtn(self) :
        self.acceuil = MainWindow()
        self.acceuil.move(0,0)
        self.acceuil.show()
        

        self.s = Gdk.Screen.get_default()
        self.move(self.s.get_width(),0)
        self.resize(200,self.s.get_height())

        self.afficher_dossier = NavigFichiers("my_video/")
        self.afficher_dossier.show()
    def quitterBtn(self) :
        print("dsd")
        
app = QtWidgets.QApplication(sys.argv)

window = AcceuilWindow()
window.show()
app.exec()