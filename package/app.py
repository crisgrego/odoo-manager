from PyQt5 import QtWidgets
from .ui.mainwindow import MainWindow
import sys

def run():
    app = QtWidgets.QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())