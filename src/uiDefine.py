"""
    UI定义文件
"""
from PyQt6.QtWidgets import QMainWindow

from typing import List

from src.ui.dialogEdit import Ui_DialogEdit
from src.ui.charaEdit import Ui_CharaEdit
from dialogMsg import dialogMsg

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