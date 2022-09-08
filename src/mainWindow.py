"""
    主程序
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QDialog, QMessageBox
from PyQt6.QtGui import QAction

import sys

from mainWindowUI import Ui_MainWindow
from dialogMsg import dialogMsg

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.mainFunc()

    def mainFunc(self):
        """
        按钮功能
        """
        self.actionAuthor.triggered.connect(self.showAuthor)
        self.actionExit.triggered.connect(self.close)
        self.actionGithub.triggered.connect(self.showGithub)
        self.actionAbout.triggered.connect(self.showAbout)

    def showAbout(self):
        dialogMsg.infoMsg(self, "关于", "Renpy脚本编辑器UI版\n版本v0.0.1")

    def showGithub(self):
        dialogMsg.infoMsg(self, "Github仓库", "https://github.com/MRSlouzk/Renpy-editor")

    def showAuthor(self):
        dialogMsg.infoMsg(self, "制作信息", "MRSlouzk(Github)\n爱喝矿泉水\nHzzr")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())