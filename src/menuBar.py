"""
    菜单栏功能类
"""
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QErrorMessage, QWidget
from PyQt6.QtGui import QFont

class MenuBar(QWidget):
    def __init__(self):
        super().__init__()
