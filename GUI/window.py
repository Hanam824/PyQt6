from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

class Window(QMainWindow):
    def __init__(self, parent: QWidget | None = ..., flags: Qt.WindowType = ...) -> None:
        super(Window, self).__init__()

        self.setGeometry(700, 300, 480, 480)
        self.setWindowTitle("Calculator")
        
