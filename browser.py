
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = None

def browser(url):
    global app
    app = QApplication(sys.argv)
    view = QWebEngineView()
    if url != None:
        view.load(QUrl(url))
    view.show()
    sys.exit(app.exec_())

def main():
    if len(sys.argv) == 1:
        browser(None)
    else:
        browser(sys.argv[1])

if __name__ == '__main__':
    main()

