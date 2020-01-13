
import sys
import os
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = None

def readText(filename):
    text = open(filename).read()
    print(text)
    return text

class Browser(QWebEngineView):
    def __init__(self):
        super().__init__()
        self.loadProgress.connect(self.onProgress)
        self.loadFinished.connect(self.pageReady)
        self.resize(600, 600)
        self.setStyleSheet('background-color:green')
    def onProgress(self, progress):
        print('progress:\t' + str(progress) + '%')
    def load(self, url):
        if url.startswith('http'):
            self.setUrl(QUrl(url))
            self.setFocus()
        elif os.path.exists(url):
            self.setHtml(readText(url))
        else:
            print('ERROR: unkown url ' + str(url))
    def pageReady(self, success):
        if success:
            self.resize(640, 400)
            self.show()
        else:
            print('page failed to load')

def browser(url):
    global app
    app = QApplication(sys.argv)
    #win = QMainWindow()
    view = Browser()
    #win.setCentralWidget(view)
    view.load(url)
    #win.show()
    view.show()
    app.exec_()

def main():
    if len(sys.argv) == 1:
        browser(None)
    else:
        browser(sys.argv[1])

if __name__ == '__main__':
    main()

