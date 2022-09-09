"""
    主程序
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QFileDialog
from PyQt6.QtGui import QAction, QDesktopServices, QIcon, QFont
from PyQt6.QtCore import QUrl

import sys
from pathlib import Path

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
        self.actionAuthor.triggered.connect(self.showAuthor)  #显示作者
        self.actionExit.triggered.connect(self.close)         #终止应用程序
        self.actionGithub.triggered.connect(self.showGithub)  #显示Github仓库
        self.actionAbout.triggered.connect(self.showAbout)    #显示关于
        self.actionHelp.triggered.connect(self.showHelp)      #显示帮助

        self.actionOpen.triggered.connect(self.showFileDialog)

    def showFileDialog(self):
        fp_name = QFileDialog.getExistingDirectoryUrl(self, "选择工作区文件夹", QUrl("./"))
        self.path = fp_name.path().lstrip('/') #工作区文件夹路径,类型为str

    def showAbout(self):
        dialogMsg.infoMsg(self, "关于", "Renpy脚本编辑器UI版\n版本v0.0.1")

    @staticmethod
    def showGithub():
        # dialogMsg.infoMsg(self, "Github仓库", "https://github.com/MRSlouzk/Renpy-editor")
        # 直接使用InfoBox显示,无法复制,不方便
        QDesktopServices.openUrl(QUrl("https://github.com/MRSlouzk/Renpy-editor"))

    def showAuthor(self):
        dialogMsg.infoMsg(self, "制作信息", "MRSlouzk(Github)\n爱喝矿泉水\nHzrr")

    @staticmethod
    def showHelp():
        #TODO 软件帮助链接,暂用仓库链接替代
        QDesktopServices.openUrl(QUrl("https://github.com/MRSlouzk/Renpy-editor"))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())