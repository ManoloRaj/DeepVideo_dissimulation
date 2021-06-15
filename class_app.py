#Program fully write by Manolo RAJAONAH
import sys
from PyQt5 import QtWidgets, uic
import cv2
from PyQt5.QtWidgets import QApplication, QLabel
import os
from MainWindow import Ui_MainWindow
from ssim import *
from matplotlib import pyplot as plt
from pylab import *

#All libraries about video - audio
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import sounddevice as sd
import os

import threading
import time
import cv2

from PyQt5.QtCore import QThread, pyqtSignal

from record_cover import *
from record_secret import *

from plot_graph import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)

    def steganoDeep(self):
        sortie = os.popen("python3 video_hide.py --model models/hide.h5 --secret_video my_video/secret.avi --cover_video my_video/cover.avi ")
        print(sortie.read())


    def revealSecret(self):
        print("Revelons le secret")
        sortie = os.popen("python3 video_reveal.py --model models/reveal.h5 --container_video my_video/stego.avi ")
        print(sortie.read())

    def showStego(self):
        sortie = os.popen("")
        print(sortie.read())

    
    def coverLive(self):
        
        self.fen1 = Record_cover()
        self.fen1.show()
        
    def secretLive(self):
        self.fen2 = Record_secret()
        self.fen2.show()

    def merge_cover(self):
        os.system("ffmpeg -i my_video/cover.avi -i my_video/cover.wav -c:v copy -c:a aac my_video/finale_cover.avi")
        
    def merge_secret(self):
        os.system("ffmpeg -i my_video/secret.avi -i my_video/secret.wav -c:v copy -c:a aac my_video/finale_secret.avi")

    

    def fenetre1(self):
        self.player = VideoPlayer()
        self.player.setWindowTitle("COVER")
        self.player.resize(600, 400)
        self.player.setGeometry(350, 100, 700, 300)
        self.player.show()

        self.player2 = VideoPlayer()
        self.player2.setWindowTitle("SECRET")
        self.player2.resize(600, 400)
        self.player2.setGeometry(350, 450, 700, 300)
        self.player2.show()

    def compute_ssim(self):
        self.graph = MatPlotResult()
        self.graph.show()
        
