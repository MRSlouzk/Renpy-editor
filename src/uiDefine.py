"""
    UI定义文件
"""
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QPixmap

from typing import List
import os
import imghdr

from src.ui.dialogAdd import Ui_dialogAdd
from src.ui.charaAdd import Ui_CharaEdit
from src.ui.dialogEdit import Ui_DialogEditNew
from src.ui.picAdd import Ui_picAdd
from src.ui.winSettings import Ui_winSettings
from dialogMsg import dialogMsg

class DialogAddWindow(QMainWindow, Ui_dialogAdd): #台词编辑窗口
    def __init__(self, parent=None):
        super(DialogAddWindow, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()

class CharaEditWindow(QMainWindow, Ui_CharaEdit):
    def __init__(self, parent=None):
        super(CharaEditWindow, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()

    def clearInput(self):
        self.charaTag.setText("")
        self.charaName.setText("")
        self.charaPrefix.setText("")

    def isEmptyInfo(self):
        charaTag = self.charaTag.text()  # 人物标签(renpy人物变量)
        charaName = self.charaName.text()  # 人物显示名
        charaPrefix = self.charaPrefix.text()  # 人物立绘前缀,格式如tohka_
        if (not charaTag):
            dialogMsg.warnMsg(self, "错误!", "未设置人物识别名!")
        elif (not charaName):
            dialogMsg.warnMsg(self, "错误!", "未设置人物名!")
        elif (not charaPrefix):
            dialogMsg.warnMsg(self, "错误!", "未设置人物立绘前缀!")
        else:
            return True

    def setCharaInfo(self, lst: List[str]):
        """
        设置人物属性文字框
        :param lst: 传入列表,依次是人物标签/人物显示名/人物立绘前缀
        :return: None
        """
        if(len(lst) == 3):
            self.charaTag.setText(lst[0])
            self.charaName.setText(lst[1])
            self.charaPrefix.setText(lst[2])
        else:
            raise Exception("参数数量错误")

class DialogEdit(QMainWindow, Ui_DialogEditNew):
    def __init__(self, parent=None):
        super(DialogEdit, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()

class PicAdd(QMainWindow, Ui_picAdd):
    def __init__(self, parent=None):
        super(PicAdd, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()

    def chooseFile(self): #选择图片文件
        fp = QFileDialog.getOpenFileUrl(self, "打开图片", QUrl("./"), "图像文件(*.jpg *.jpeg *.png *.webp)")
        if (not fp[0].isEmpty()):  # 防止用户直接关闭窗口
            path = fp[0].path().lstrip('/')  # 工作区文件夹路径,类型为str
            if(imghdr.what(path) is None):
                dialogMsg.warnMsg(self, "警告", "图片已损坏!")
                return
            else:
                self.picPathEdit.setText(path)

    def showPic(self): #显示图片
        try:
            pixmap = QPixmap(self.picPathEdit.text())
        except FileNotFoundError:
            dialogMsg.warnMsg(self, "警告", "不存在该文件!")
            return
        self.labelPic.setPixmap(pixmap)
        self.labelPic.setScaledContents(True)

class WinSetting(QMainWindow, Ui_winSettings):
    def __init__(self, parent=None):
        super(WinSetting, self).__init__(parent)
        self.setupUi(self)

    def exitWin(self):
        self.close()