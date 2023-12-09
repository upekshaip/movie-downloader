
from PyQt5.QtWidgets import QTreeView, QAbstractItemView, QApplication, QTreeWidgetItem, QTableWidgetItem, QCheckBox
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from bin.API import Handle
from bin.Config import AppConfig as AC
import requests
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
            
            self.handle_table(app, results)
        
        else:
            print("data not availible")
            self.show_warning_popup()
    

    
    def handle_table(self, app, data):
        row = 0
        app.tableWidget.setRowCount(len(data))
        for movie in data:
            if movie['poster_path'] != None:
                app.tableWidget.setRowHeight(row, 300)
                
                poster = f"{AC.POSTER_URL}{movie['poster_path']}"

                image = QImage()
                image.loadFromData(requests.get(poster).content)

                image_label = QLabel()
                image_label.setPixmap(QPixmap(image).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                app.tableWidget.setCellWidget(row, 0, image_label)
            else:
                poster = "Image not available"
                app.tableWidget.setItem(row, 0, QTableWidgetItem(str(poster)))


            
            app.tableWidget.setItem(row, 1, QTableWidgetItem(str(movie["original_title"])))
            app.tableWidget.setItem(row, 2, QTableWidgetItem(str(movie["vote_average"])))
            app.tableWidget.setItem(row, 3, QTableWidgetItem(str(movie["release_date"])))
            app.tableWidget.setItem(row, 4, QTableWidgetItem(str(movie["overview"])))
            row += 1
