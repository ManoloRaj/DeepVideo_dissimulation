# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Acceuil.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AcceuilWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AcceuilWindow")
        MainWindow.resize(943, 535)
        MainWindow.move(200,100)
        MainWindow.setStyleSheet("#AcceuilWindow{background-image : url(\"me.png\"); background-position : center; background-repeat : no-repeat;background-size: contain;}\n"
"\n"
"QPushButton#acceuilBut{\n"
"                background : #45e78e;\n"
"                color : rgb(255,255,255);\n"
"                border : 1px solid rgb(255,255,255);\n"
"                border-radius: 1px;\n"
"                font-size : 16px; \n"
"                width : 10px;\n"
"            }\n"
"QPushButton#acceuilBut:hover{\n"
"                background : rgb(255,255,255);\n"
"                color : #45e78e;\n"
"                border : 1px solid #45e78e;\n"
"                border-radius: 1px;\n"
"   } \n"
"QPushButton#quitterBut{\n"
"                background : red;\n"
"                color : rgb(255,255,255);\n"
"                border : 1px solid rgb(255,255,255);\n"
"                border-radius: 1px;\n"
"                font-size : 16px; \n"
"                width : 10px;\n"
"            }\n"
"QPushButton#quitterBut:hover{\n"
"                background : rgb(255,255,255);\n"
"                color : red;\n"
"                border : 1px solid red;\n"
"                border-radius: 1px;\n"
"   }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.acceuilBut = QtWidgets.QPushButton(self.centralwidget)
        self.acceuilBut.setGeometry(QtCore.QRect(340, 380, 231, 51))
        self.acceuilBut.setObjectName("acceuilBut")
        self.quitterBut = QtWidgets.QPushButton(self.centralwidget)
        self.quitterBut.setGeometry(QtCore.QRect(340, 440, 231, 51))
        self.quitterBut.setStyleSheet("background-color :red\n"
"\n"
"QPushButton:hover{\n"
"                background : rgb(255,255,255);\n"
"                color : red;\n"
"                border : 1px solid red;\n"
"                border-radius: 2px;\n"
"   }")
        self.quitterBut.setObjectName("quitterBut")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 0, 571, 61))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 42, 381, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.acceuilBut.clicked.connect(MainWindow.acceuilBtn)
        self.quitterBut.clicked.connect(MainWindow.quitterBtn)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.acceuilBut.setText(_translate("MainWindow", "ACCEUIL"))
        self.quitterBut.setText(_translate("MainWindow", "Quitter"))
        self.label.setText(_translate("MainWindow", "DEEP STEGANOGRAPHIE VIDEO "))
        self.label_2.setText(_translate("MainWindow", "By Manolo RAJAONAH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

