import yt_dlp
import time
import re
import math

from PyQt5.QtCore import Qt, QMetaObject, Q_ARG

# URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def extract(text_with_ansi):
    percentage_pattern = re.compile(r'(\d+(\.\d+)?)%')
    match = percentage_pattern.search(text_with_ansi)
    if match:
        percentage = match.group(1)
        return int(math.floor(float(percentage)))
    else:
        print("No percentage found in the text.")
        return None

# ℹ️ See "progress_hooks" in help(yt_dlp.YoutubeDL)

class DWN:
    def __init__(self):
        self.signal = False

    def download(self, app, URL):
        def my_hook(d):
            value = extract(d['_percent_str'])
            app.progressBar.setValue(value)
            # print(d['_percent_str'])
            QMetaObject.invokeMethod(app.progressBar, "setValue", Qt.QueuedConnection | Qt.UniqueConnection, Q_ARG(int, value))

            # QMetaObject.invokeMethod(app.progressBar, "setValue", Qt.QueuedConnection, value)
            if d['status'] == 'finished':
                print('Done downloading, now post-processing ...')
        
        ydl_opts = {
            'logger': MyLogger(),
            'progress_hooks': [my_hook],
            'outtmpl': "Movies" + "/%(title)s.%(ext)s"
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            
            if self.signal:
                # ydl.stop_download()
                pass
            ydl.download([URL])

