import sys
from PyQt5 import QtWidgets, uic

qpp = QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("gui.ui")
window.show()
app.exec()