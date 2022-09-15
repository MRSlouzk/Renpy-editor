"""
    UI定义文件
"""
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QAbstractItemView, QTableView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QPixmap, QStandardItemModel, QStandardItem

from typing import List
import imghdr

from src.ui.dialogAdd import Ui_dialogAdd
from src.ui.charaAdd import Ui_CharaEdit
from src.ui.dialogEdit import Ui_DialogEditNew
from src.ui.editPicList import Ui_picEdit
from src.ui.winSettings import Ui_winSettings
from src.ui.videoAdd import Ui_VideoAdd
from dialogMsg import dialogMsg

class DialogAddWindow(QMainWindow, Ui_dialogAdd): #台词编辑窗口
    def __init__(self, parent=None):
        super(DialogAddWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def exitWin(self):
        self.close()

class CharaEditWindow(QMainWindow, Ui_CharaEdit):
    def __init__(self, parent=None):
        super(CharaEditWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

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
        self.setFixedSize(self.width(), self.height())

    def exitWin(self):
        self.close()

class PicEdit(QMainWindow, Ui_picEdit):
    def __init__(self, path: str, parent=None):
        super(PicEdit, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        self.readFiles(path)

    def readFiles(self, path: str):
        """
        在treeView中显示images文件夹结构\n
        :param path: 工作区路径
        :return: None
        """
        #TODO 读取images.rpy中文件路径
        # 显示至tableView当中
        self.model = QStandardItemModel(0, 2)
        self.model.setHorizontalHeaderLabels(['文件名', '归类'])
        self.tableView.setModel(self.model)
        self.tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableview.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中整行
        self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中一行
        self.tableview.setEditTriggers(QTableView.NoEditTriggers)  # 不可编辑


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

    def deletePic(self):
        index = self.tableview.currentIndex()  # 取得当前选中行的index
        self.model.removeRow(index.row())  # 通过index的row()操作得到行数进行删除
        #TODO 后续文件操作(删除本地文件与rpy文件中对应代码)

    def addPic(self):
        pass

    def showPic(self): #显示图片
        try:
            pixmap = QPixmap(self.picPathEdit.text())
        except FileNotFoundError:
            dialogMsg.warnMsg(self, "警告", "不存在该文件!")
            return
        self.labelPic.setPixmap(pixmap)
        self.labelPic.setScaledContents(True)

class VideoAdd(QMainWindow, Ui_VideoAdd):
    def __init__(self, parent=None):
        super(VideoAdd, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def chooseFile(self):
        fp = QFileDialog.getOpenFileUrl(self, "打开视频", QUrl("./"), "图像文件(*.ogv)")
        if (not fp[0].isEmpty()):  # 防止用户直接关闭窗口
            path = fp[0].path().lstrip('/')  # 工作区文件夹路径,类型为str
            #TODO 因为检测视频是否损坏需要OpenCv2模块,所以暂不处理
            self.chooseVideo.setText(path)

    def exitWin(self):
        self.close()

class WinSetting(QMainWindow, Ui_winSettings):
    def __init__(self, parent=None):
        super(WinSetting, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def exitWin(self):
        self.close()