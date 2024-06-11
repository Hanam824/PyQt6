from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)

        self.setGeometry(700, 300, 480, 480)
        self.setWindowTitle("Calculator")
        
        self.initUI()

    def initUI(self):

        # add menubar
        menubar = self.menuBar()

        # add drop down items
        exitAct = QAction('&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        #exitAct.triggered.connect(qApp.quit)

        newAct = QAction('New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('New Sudoku')
        #newAct.triggered.connect(GameLogic.clearFields)

        rulesAct = QAction('Rules', self)
        rulesAct.setShortcut('Ctrl+R')
        rulesAct.setStatusTip('Sudoku Rules')
        #rulesAct.triggered.connect(GameLogic.sudokuRules)

        # add menubar entries
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAct)
        fileMenu.addAction(exitAct)

        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(rulesAct)

        # call gridlayout function
        layout = self.gridLayout()
        self.setCentralWidget(layout)

    def gridLayout(self):
        w = QWidget()

        return w