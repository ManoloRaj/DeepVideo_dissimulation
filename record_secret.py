from PyQt5.QtCore import QThread, pyqtSignal
import sys
from PyQt5 import QtWidgets, uic
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtWidgets import QMainWindow, QLabel, QSizePolicy, QApplication 
from PyQt5.QtGui import QPixmap, QImage                                
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

import time

import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import sounddevice as sd
import os

sd.default.samplerate = 44100
sd.default.device = 6

import threading
import time
import cv2

class Thread1 (QThread):
    def run(self):
        self.record_audio()

    def record_audio(self):  
        print(sd.query_devices())

        fs = 44100  # Sample rate
        seconds = 5 # Duration of recording


        myrecording = sd.rec( int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        write('my_video/secret.wav', fs, myrecording)  # Save as WAV file
        


class Thread2(QThread):
    changePixmap = pyqtSignal(QImage)

    def run(self):
        capture_duration = 5

        cap = cv2.VideoCapture(0)

        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        out = cv2.VideoWriter('my_video/secret.avi', fourcc, 15, (640,480))

        start_time = time.time()

        while ((time.time() - start_time < capture_duration)):
            ret, frame = cap.read()
            if ret:
                # https://stackoverflow.com/a/55468544/6622587
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)
                #Save video file
                out.write(frame)

            cv2.waitKey(10)

        cap.release()
        out.release()
        
        
                


class Record_secret(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        self.setWindowTitle("cv2")
        self.setGeometry(450, 10, 700, 300)
        self.resize(800, 480)
        self.move(364,0)
        # create a label
        self.label = QLabel(self)
        self.label.move(80, 0)
        self.label.resize(800, 480)

        Audio_signal = Thread1(self)

        Video_signal = Thread2(self)
        Video_signal.changePixmap.connect(self.setImage)

        Audio_signal.start()
        Video_signal.start()
