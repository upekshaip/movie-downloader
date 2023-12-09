# from bin.Process.Tasks import refresh_local_process, refresh_nlearn, download_files, clear_all_logs, select_all_slots, log_out, log_in, show_log_table, search_logs, ignore_process
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QFileIconProvider, QDialog, QLineEdit, QTableWidgetItem, QLabel, QTreeWidgetItem
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from bin.Config import AppConfig as AC
import os
import json
from bin.API import Handle
from bin.Process import Process


class RunTiime():

    def __init__(self):
        self.process = Process()

    def buttons(self, app):
        # MENU

        app.btn_home.clicked.connect(lambda: app.stackedWidget.setCurrentWidget(app.home_pg))
        app.btn_movie.clicked.connect(lambda: app.stackedWidget.setCurrentWidget(app.movie_pg))
        app.btn_downloader.clicked.connect(lambda: app.stackedWidget.setCurrentWidget(app.downloader_pg))
        app.btn_instructions.clicked.connect(lambda: app.stackedWidget.setCurrentWidget(app.instructions_pg))
        app.btn_github.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl('https://github.com/upekshaip/movie-downloader')))

       
        # Search BTN
        app.btn_search.clicked.connect(lambda: self.process.handle_search(app, app.search_movie.text()))   

        # show search texts
        app.search_movie.setPlaceholderText("Search...")
        app.movie_count.setText("")
        
        
        # self.search_logs_box.textChanged.connect(
        #     lambda: search_logs(self, self.search_logs_box.text()))
        
        # ignore json file tasks
        # self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        # self.reload_course_button.clicked.connect(lambda: ignore_process(self))

    def run(self):
        # refresh_local_process(self)
        # show_log_table(self)
        # self.password_input.setEchoMode(QLineEdit.Password)
        # self.cookie_input.setPlaceholderText("Moodle Session")
        pass