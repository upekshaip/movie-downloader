
from PyQt5.QtWidgets import QTreeView, QAbstractItemView, QApplication, QTreeWidgetItem, QTableWidgetItem, QCheckBox
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon
from bin.API import Handle

class Process:
    def __init__(self):
        self.api = Handle("ok")

    def show_warning_popup(self, message, warn):
        # create a message box with the warning message and an "OK" button to dismiss the popup
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QIcon('logo.ico'))
        msg.setText(message)
        msg.setWindowTitle(f"Warning - {warn}")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def handle_search(self, app, search_txt):
        data = self.api.search_movie(search_txt)
        if data:
            current_page = data["page"]
            total_pages = data["total_pages"]
            total_results = data["total_results"]
            results = data["results"]
            app.movie_count.setText(f"Movie count: {total_results}\nMovie Pages: {total_pages}")

        else:
            print("data not availible")
            self.show_warning_popup()
