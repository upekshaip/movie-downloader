import sys
from bin.Runtime import RunTiime as rt
# pyqt
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileIconProvider, QDialog, QLineEdit, QTableWidgetItem, QLabel, QTreeWidgetItem
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from bin.Config.config import FDB
# idk btw


class MainUI(QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("ux.ui", self)
        self.setWindowTitle('Movie Downloader')
        self.setWindowIcon(QIcon('logo.ico'))
        rt.buttons(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()