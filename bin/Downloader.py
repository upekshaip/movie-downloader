import yt_dlp
import time
import re
import math

from PyQt5.QtCore import Qt, QMetaObject, Q_ARG


def remove_color_codes(text_with_colors):
    color_pattern = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    text_without_colors = color_pattern.sub('', text_with_colors)
    return text_without_colors

def extract(text_with_ansi):
    percentage_pattern = re.compile(r'(\d+(\.\d+)?)%')
    match = percentage_pattern.search(text_with_ansi)
    if match:
        percentage = match.group(1)
        return int(math.floor(float(percentage)))
    else:
        print("No percentage found in the text.")
        return None


class DWN:
    def __init__(self):
        self.signal = False

    def download(self, app, URL, name):
        def my_hook(d):
            value = extract(d['_percent_str'])
            QMetaObject.invokeMethod(app.progressBar, "setValue", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(int, value))

            if d['status'] == 'finished':
                QMetaObject.invokeMethod(app.progress_text, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"Done downloading, now post-processing ..."))
        

        if name:
            out_name = name
            QMetaObject.invokeMethod(app.info_label, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"File name saved as: {out_name}"))
        else:
            out_name = "%(title)s"
            QMetaObject.invokeMethod(app.info_label, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"File name saved as: Defaul name"))
        

        class MyLogger:
            def debug(self, msg):
                if msg.startswith('[debug] '):
                    pass
                else:
                    self.info(msg)

            def info(self, msg):
                QMetaObject.invokeMethod(app.progress_text, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"{remove_color_codes(msg)}"))

            def warning(self, msg):
                QMetaObject.invokeMethod(app.progress_text, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"{remove_color_codes(msg)}"))

            def error(self, msg):
                QMetaObject.invokeMethod(app.progress_text, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"{remove_color_codes(msg)}"))

        ydl_opts = {
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'outtmpl': "Movies" + f"/{out_name}.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([URL])

            QMetaObject.invokeMethod(app.progress_text, "setText", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(str, f"Task finished"))
            QMetaObject.invokeMethod(app.download_btn, "setEnabled", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(bool, True))

