from PyQt5.QtWidgets import QTreeView, QAbstractItemView, QApplication, QTreeWidgetItem, QTableWidgetItem, QCheckBox
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QImage, QDesktopServices, QIcon
from PyQt5.QtCore import Qt, QUrl, pyqtSignal
from bin.API import Handle
from bin.Config import AppConfig as AC
import requests
import os
from bin.Downloader import DWN
import threading



class Process:
    SIGNAL = False
    def __init__(self):
        self.api = Handle("ok")
        self.download_thread = None

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
        data = self.api.search_movie(search_txt, 1)
        
        if data:
            current_page = data["page"]
            total_pages = data["total_pages"]
            total_results = data["total_results"]
            results = data["results"]
            
            app.movie_count.setText(f"Movie count: {total_results}\nMovie Pages: {total_pages}")
            app.load_pg_label.setText(f"1/{total_pages}")
            if total_pages > 1:
                app.load_next_btn.setEnabled(True)

            self.handle_table(app, results)
        
        else:
            print("data not availible")
            self.show_warning_popup()
    

    def get_img(self, s, poster):
        return s.get(poster).content
    
    def handle_load(self, app, search_txt, pg):
        pg = int(pg.split("/")[0]) + 1
        max_pg = int(app.movie_count.text().split(" ")[-1])
        if max_pg == pg:
            app.load_next_btn.setEnabled(False)

        print(pg)
        
        
        data = self.api.search_movie(search_txt, pg)
        if data:
            current_page = data["page"]
            total_pages = data["total_pages"]
            total_results = data["total_results"]
            results = data["results"]
            app.movie_count.setText(f"Movie count: {total_results}\nMovie Pages: {total_pages}")
            app.load_pg_label.setText(f"{current_page}/{total_pages}")

            self.insert_data_table(app, results)
        else:
            print("data not availible")
            self.show_warning_popup()

    def handle_table(self, app, data):
        row = 0
        app.tableWidget.setRowCount(len(data))
        s = requests.Session()
        for movie in data:
            if movie['poster_path'] != None:
                app.tableWidget.setRowHeight(row, 300)
                
                poster = f"{AC.POSTER_URL}{movie['poster_path']}"

                image = QImage()
                image.loadFromData(self.get_img(s, poster))

                image_label = QLabel()
                image_label.setPixmap(QPixmap(image).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                app.tableWidget.setCellWidget(row, 0, image_label)
            else:
                poster = "Image not available"
                app.tableWidget.setItem(row, 0, QTableWidgetItem(str(poster)))


            
            app.tableWidget.setItem(row, 1, QTableWidgetItem(str(movie["original_title"])))
            app.tableWidget.setItem(row, 5, QTableWidgetItem(str(movie["vote_average"])))
            app.tableWidget.setItem(row, 3, QTableWidgetItem(str(movie["release_date"])))
            app.tableWidget.setItem(row, 4, QTableWidgetItem(str(movie["overview"])))
            app.tableWidget.setItem(row, 6, QTableWidgetItem(str(movie["id"])))
           

            button = QPushButton("Watch")
            button.setStyleSheet("text-align: center;")

            button.setFixedSize(80, 40)
            button.clicked.connect(lambda _, r=movie: self.movie_clicked(app, r))
            
            container = QWidget()
            h_layout = QHBoxLayout(container)
            v_layout = QVBoxLayout()
            v_layout.addWidget(button)
            h_layout.addLayout(v_layout)
            container.setLayout(h_layout)
            
            app.tableWidget.setCellWidget(row, 2, container)

            row += 1

    def movie_clicked(self, app, movie):
        app.stackedWidget.setCurrentWidget(app.movie_pg)
        app.movie_name.setText(f'{movie["original_title"]} - {movie["release_date"].split("-")[0]}')
        # app.movie_year.setText(movie["release_date"].split("-")[0])
        # app.movie_poster
        details, pic = self.get_movie_info(movie)
        self.format_movie_info(app, movie, details)
   

        image = QImage()
        image.loadFromData(pic)
        app.movie_poster.setPixmap(QPixmap(image).scaled(400, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        # print(f'Button in row {movie["id"]} clicked!')


    def format_movie_info(self, app, movie, details):
        genres = ""
        for genre in details["genres"]:
            genres += f'{genre["name"]}, '
        
        app.m_name.setText(f"{movie['original_title']}")
        app.m_language.setText(f"{movie['original_language']}")
        app.m_date.setText(f"{movie['release_date']}")
        app.m_runtime.setText(f"{details['runtime']} min")
        app.m_popularity.setText(f"{movie['popularity']}")
        app.m_status.setText(f"{details['status']}")
        app.m_genres.setText(f"{genres}")
        app.m_imdb.setText(f"{details['imdb_id']}")
        app.m_budget.setText(f"{details['budget']}")
        app.m_overview.setText(f"{movie['overview']}")
    
        # buttons and inputs
        LINK1 = f"{AC.MOVIE_LINK1}{movie['id']}"
        LINK2 = f"{AC.MOVIE_LINK2}{details['imdb_id']}"
        LINK3 = f"{AC.MOVIE_LINK3}{movie['id']}"

        app.link1.setText(LINK1)
        app.link2.setText(LINK2)
        app.link3.setText(LINK3)

        app.link1_open.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(LINK1)))
        app.link2_open.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(LINK2)))
        app.link3_open.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(LINK3)))
        
        app.link1_copy.clicked.connect(lambda: QApplication.clipboard().setText(LINK1))
        app.link2_copy.clicked.connect(lambda: QApplication.clipboard().setText(LINK2))
        app.link3_copy.clicked.connect(lambda: QApplication.clipboard().setText(LINK3))

    
    
    def get_movie_info(self, movie):
        INFO_URL = f"{AC.MOVIE_INFO_URL}{movie['id']}"
        poster = f"{AC.POSTER_URL}{movie['poster_path']}"
        
        s = requests.Session()
        details = s.get(INFO_URL, headers=AC.TMD_HEADERS_DEFAULT).json()
        pic = self.get_img(s, poster)
        return details, pic
        

    
    def insert_data_table(self, app, data):
        row = app.tableWidget.rowCount()
        s = requests.Session()
        for movie in data:
            app.tableWidget.insertRow(row)
            if movie['poster_path'] != None:
                app.tableWidget.setRowHeight(row, 300)
                
                poster = f"{AC.POSTER_URL}{movie['poster_path']}"

                image = QImage()
                image.loadFromData(self.get_img(s, poster))

                image_label = QLabel()
                image_label.setPixmap(QPixmap(image).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                app.tableWidget.setCellWidget(row, 0, image_label)
            else:
                poster = "Image not available"
                app.tableWidget.setItem(row, 0, QTableWidgetItem(str(poster)))
            app.tableWidget.setItem(row, 1, QTableWidgetItem(str(movie["original_title"])))
            app.tableWidget.setItem(row, 5, QTableWidgetItem(str(movie["vote_average"])))
            app.tableWidget.setItem(row, 3, QTableWidgetItem(str(movie["release_date"])))
            app.tableWidget.setItem(row, 4, QTableWidgetItem(str(movie["overview"])))
            app.tableWidget.setItem(row, 6, QTableWidgetItem(str(movie["id"])))

            button = QPushButton("Watch")
            button.setStyleSheet("text-align: center;")

            button.setFixedSize(80, 40)
            button.clicked.connect(lambda _, r=movie: self.movie_clicked(app, r))
            
            container = QWidget()
            h_layout = QHBoxLayout(container)
            v_layout = QVBoxLayout()
            v_layout.addWidget(button)
            h_layout.addLayout(v_layout)
            container.setLayout(h_layout)
            
            app.tableWidget.setCellWidget(row, 2, container)

            row += 1

    def handle_download(self, app, url):
        if os.path.exists("./Movies"):
            pass
        else:
            os.mkdir("./Movies")

        if self.download_thread and self.download_thread.is_alive():
            print("Download is already in progress.")
            return
    
        self.download = DWN()
        self.download_thread = threading.Thread(target=self.download.download, args=(app, url))
        self.download_thread.start()

        # download(app, url)
    def closeEvent(self, event):
        if self.download_thread and self.download_thread.is_alive():
            print("Stopping download manually...")
            # Crash the app and threads
            print(1/0)