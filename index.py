import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

class FenPrincipal(QMainWindow) :
    def __init__(self):
        super(FenPrincipal,self).__init__()
        self.showMaximized()
        self.navigator = QWebEngineView()
        self.navigator.setUrl(QUrl('https://www.bing.com/'))
        self.setCentralWidget(self.navigator)
        self.setWindowIcon(QtGui.QIcon('student.png'))
        navbar = QToolBar()
        self.addToolBar(navbar)
        
        prev_btn = QAction('Retour',self)
        prev_btn.triggered.connect(self.navigator.back)
        navbar.addAction(prev_btn)
        
        refresh_btn = QAction('Rafraichir',self)
        refresh_btn.triggered.connect(self.navigator.reload)
        navbar.addAction(refresh_btn)
        
        next_btn = QAction('Suivant',self)
        next_btn.triggered.connect(self.navigator.forward)
        navbar.addAction(next_btn)
        
        home_btn = QAction('Accueil',self)
        home_btn.triggered.connect(self.url_home)
        navbar.addAction(home_btn)
        
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)
        
        self.navigator.urlChanged.connect(self.update_url)
        
    def url_home(self):
        self.navigator.setUrl(QUrl('https://www.bing.com/'))
        
    def navigation(self) :
        url = self.url_bar.text()
        self.navigator.setUrl(QUrl(url))
        
    def update_url(self,url) :
        self.url_bar.setText(url.toString())
        
        
app = QApplication(sys.argv)
QApplication.setApplicationName("Go MZ")
fenetre = FenPrincipal()
app.exec()