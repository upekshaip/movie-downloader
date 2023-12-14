import sys
from bin.Runtime import RunTiime as RT
# pyqt
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainUI(QMainWindow):

    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("ux.ui", self)
        self.setWindowTitle('Movie Downloader')
        self.setWindowIcon(QIcon('logo.ico'))
        rt = RT()
        rt.buttons(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()