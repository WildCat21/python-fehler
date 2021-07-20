from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from deta import Deta    
        
class main(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.stack = QStackedWidget()
        self.stack.addWidget(login())
        self.stack.addWidget(registrer())
        
        layout = QGridLayout()
        layout.addWidget(self.stack, 0, 0)
        
        self.setLayout(layout)
        self.show()
        
    def login(self):
        self.stack.setCurrentIndex(0)
    
    def registrer(self):
        self.stack.setCurrentIndex(1)
        
class login(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        llly = QGridLayout()
        
        us = QLabel("Benutzername *")
        us1 = QLineEdit()
        ps = QLabel("Passwort *")
        ps1 = QLineEdit()
        fe = QPushButton("login")
        pfff = QLabel("* Pflichtfelder")
        rg = QPushButton("registrieren")
        pltz = QLabel()
        
        rg.clicked.connect(main.registrer)
        
        llly.addWidget(us, 0, 1)
        llly.addWidget(us1, 1, 1)
        llly.addWidget(ps, 2, 1)
        llly.addWidget(ps1, 3, 1)
        llly.addWidget(pltz, 4, 1)
        llly.addWidget(fe, 5, 0)
        llly.addWidget(pfff, 5, 1)
        llly.addWidget(rg, 5, 2)
        
        self.setLayout(llly)

class registrer(QWidget): 
    def __init__(self, parent=None): 
        super().__init__(parent)
        
        ly = QGridLayout()
        
        lvn = QLabel("Vorname")
        self.vn = QLineEdit()
        lnn = QLabel("Nachname")
        self.nn = QLineEdit()
        lag = QLabel("Alter")
        self.ag = QLineEdit()
        lgb = QLabel("Geburtsdatum (tt.mm.jjjj)")
        self.gb = QLineEdit()
        
        lus = QLabel("Benutzername *")
        self.us = QLineEdit()
        lem = QLabel("E-Mail-Adresse *")
        self.em = QLineEdit()
        lps = QLabel("Passwort *")
        self.ps = QLineEdit()
        lpss = QLabel("Passwort wiederholen *")
        self.pss = QLineEdit()
        
        fertig = QPushButton("registrieren")
        pf = QLabel("* Pflichtfelder")
        log = QPushButton("login")

        fertig.clicked.connect(self.regg)
        log.clicked.connect(main.login)
        
        ly.addWidget(fertig, 8, 0)
        ly.addWidget(pf, 8, 1)
        ly.addWidget(log, 8, 2)
        
        ly.addWidget(lvn, 0, 0)
        ly.addWidget(self.vn, 1, 0)
        ly.addWidget(lnn, 2, 0)
        ly.addWidget(self.nn, 3, 0)
        ly.addWidget(lag, 4, 0)
        ly.addWidget(self.ag, 5, 0)
        ly.addWidget(lgb, 6, 0)
        ly.addWidget(self.gb, 7, 0)
        
        ly.addWidget(lus, 0, 3)
        ly.addWidget(self.us, 1, 3)
        ly.addWidget(lem, 2, 3)
        ly.addWidget(self.em, 3, 3)
        ly.addWidget(lps, 4, 3)
        ly.addWidget(self.ps, 5, 3)
        ly.addWidget(lpss, 6, 3)
        ly.addWidget(self.pss, 7, 3)
        
        self.setLayout(ly)
        

    def regg(self):
        print("registrieren")
        
        
app = QApplication(sys.argv) 
reg = main()
reg.show()
sys.exit(app.exec_())
