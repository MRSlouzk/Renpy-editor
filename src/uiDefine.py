"""
    UI定义文件
"""
from PyQt6.QtWidgets import QMainWindow

from src.ui.dialogEdit import Ui_DialogEdit
from src.ui.charaEdit import Ui_CharaEdit

class DialogEditWindow(QMainWindow, Ui_DialogEdit): #台词编辑窗口
    def __init__(self, parent=None):
        super(DialogEditWindow, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()

class CharaEditWindow(QMainWindow, Ui_CharaEdit):
    def __init__(self, parent=None):
        super(CharaEditWindow, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()