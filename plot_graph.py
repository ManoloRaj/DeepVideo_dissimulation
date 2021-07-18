import cv2
from ssim import *
from matplotlib import pyplot as plt

import sys
import matplotlib

#matplotlib.use('Qt5Agg')

from math import log10, sqrt
import cv2
import numpy as np

import gi
#gi.require_version('Gtk', '3.0')
#from gi.repository import Gtk
 
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MatPlotResult(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MatPlotResult, self).__init__(*args, **kwargs)
        self.resize(800, 800)
        self.move(364,0)

        
        x1, y1 = self.get_ssim()
        x2, y2 = self.get_psnr()

        sc = MplCanvas(self)
        sc.axes.plot(x1, y1)
        sc.axes.set_title('SSIM 4x4')
        sc.axes.set_ylabel("SSIM")

        sc1 = MplCanvas(self)
        sc1.axes.plot(x2, y2)
        sc1.axes.set_title('PSNR')
        sc1.axes.set_ylabel("PSNR en Decibel (dB)")


        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)
        layout.addWidget(sc1)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def get_ssim(self):
        x = []
        result =[]
        print("Compute SSIM")
        i = 1

        secretCap = cv2.VideoCapture("my_video/secret.avi")
        revealCap = cv2.VideoCapture("my_video/reveal.avi")
        print(secretCap.get(cv2.CAP_PROP_FRAME_COUNT))
        while (i < (secretCap.get(cv2.CAP_PROP_FRAME_COUNT)/1.5)):
            success1,secretIm = secretCap.read()
            success2,revealIm = revealCap.read()

            secretIm = cv2.resize(secretIm, (200,200))
            #cv2.imwrite(folder+'secret'+str(i)+'.jpg', secretIm)
            revealIm = cv2.resize(revealIm, (200,200))
            #cv2.imwrite(folder+'reveal'+str(i)+'.jpg', revealIm)

            result.append(ssim(secretIm, revealIm))
            x.append(i)
            print("image "+str(i))
            print(" SSIM "+str(ssim(secretIm, revealIm)))
            i=i+1
        return x, result

    def get_psnr(self):  

        x = []
        result =[]
        print("Compute PSNR")
        i = 1

        secretCap = cv2.VideoCapture("my_video/secret.avi")
        revealCap = cv2.VideoCapture("my_video/reveal.avi")

        while (i < (secretCap.get(cv2.CAP_PROP_FRAME_COUNT)/1.5)):

            success1,secretIm = secretCap.read()
            success2,revealIm = revealCap.read()

            secretIm = cv2.resize(secretIm, (200,200))
            #cv2.imwrite(folder+'secret'+str(i)+'.jpg', secretIm)
            revealIm = cv2.resize(revealIm, (200,200))
            #cv2.imwrite(folder+'reveal'+str(i)+'.jpg', revealIm)

            result.append(self.compute_psnr(secretIm, revealIm))
            x.append(i)
            print("Image "+str(i))
            print(" PSNR " +str(self.compute_psnr(secretIm, revealIm)))
            i=i+1
        return x, result

    def compute_psnr(self, original, compressed):
        mse = np.mean((original - compressed) ** 2)
        if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
            return 100
        max_pixel = 255.0
        psnr = 20 * log10(max_pixel / sqrt(mse))

        return psnr
  
       
