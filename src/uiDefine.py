"""
    UI定义文件
"""
import os.path
import time

from PyQt6.QtWidgets import QMainWindow, QFileDialog, QHeaderView, QAbstractItemView, QTableView
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QPixmap, QStandardItemModel, QStandardItem

from typing import List
import imghdr, shutil

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
        self.path = path

        self.readFiles()

    def __findFiles(self, path):
        """
        遍历文件夹下所有文件\n
        :param path:要遍历的文件夹
        :return None
        """
        # 首先遍历当前目录所有文件及文件夹
        ori_path = self.path + "/others"
        file_list = os.listdir(path)
        # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
        for file in file_list:
            # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
            cur_path = os.path.join(path, file)
            # 判断是否是文件夹
            if os.path.isdir(cur_path):
                self.__findFiles(cur_path)
            else:
                if (not file.endswith((".jpg", ".jpeg", ".png", ".webp"))):  # 判断文件类型
                    print(f"{file}不是图片文件!!!")
                    continue
                dir = cur_path.replace(ori_path + "\\", "").replace("\\" + file, "")
                inner_lst = [file, dir]
                self.img_lst.append(inner_lst)

    def readFiles(self):
        """
        在treeView中显示images文件夹结构
        """
        #TODO 读取images.rpy中文件路径
        # 显示至tableView当中
        self.img_lst = []
        self.__findFiles(self.path + "/others")

        # img_lst = [["imgName1","imgUrl1"],["imgName2","imgUrl2"],
        #            ["imgName3","imgUrl3"],["imgName4","imgUrl4"]]
        self.model = QStandardItemModel(0, 2)
        self.model.setHorizontalHeaderLabels(['文件名', '归类'])
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True) # 列填满窗口
        # self.tableview.horizontalHeader.setSectionResizeMode(QHeaderView.Stretch)  # 所有列自动拉伸，充满界面
        self.tableView.setSelectionMode(QAbstractItemView.selectionMode(self.tableView).SingleSelection)
        # self.tableview.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中整行
        self.tableView.setSelectionBehavior(QAbstractItemView.selectionBehavior(self.tableView).SelectRows)
        # self.tableview.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中一行
        self.tableView.setEditTriggers(QTableView.editTriggers(self.tableView).NoEditTriggers)  # 不可编辑

        for i in self.img_lst:
            self.model.appendRow([QStandardItem(i[0]),QStandardItem(i[1])])
        # self.model.appendRow(
        #     [QStandardItem('row %s,column %s' % (11, 11)),
        #      QStandardItem('row %s,column %s' % (11, 11))]
        # )

    def exitWin(self):
        self.close()

    def chooseFile(self): #选择图片文件
        fp = QFileDialog.getOpenFileUrl(self, "打开图片", QUrl("./"), "图像文件(*.jpg *.jpeg *.png *.webp)")
        if (not fp[0].isEmpty()):  # 防止用户直接关闭窗口
            path = fp[0].path().lstrip('/')  # 文件路径,类型为str
            if(imghdr.what(path) is None):
                dialogMsg.warnMsg(self, "警告", "图片已损坏!")
                return
            else:
                self.picPathEdit.setText(path)

    def __getPicPath(self, row: int) -> str:
        fileName = self.model.item(row, 0).text()  # 文件名
        nowPath = self.model.item(row, 1).text()  # 文件路径
        abspath = self.path + "/others/" + nowPath + "/" + fileName
        return abspath

    def deletePic(self): #删除图片
        index = self.tableView.currentIndex()  # 取得当前选中行的index
        abspath = self.__getPicPath(index.row())
        try:
            os.remove(abspath)
        except FileNotFoundError:
            dialogMsg.warnMsg(self, "警告", "文件不存在!")
        self.model.removeRow(index.row())  # 通过index的row()操作得到行数进行删除
        self.labelPic.clear() #清空
        #TODO 后续文件操作(删除本地文件与rpy文件中对应代码)

    def chooseFilePath(self): #选择图片存储路径
        fp_name = QFileDialog.getExistingDirectoryUrl(self, "选择图片存储文件夹", QUrl(self.path))
        if (not fp_name.isEmpty()):  # 防止用户直接关闭窗口
            path = fp_name.path().lstrip('/')  # 工作区文件夹路径,类型为str
            self.chosen_path = path
            return 0
        else:
            return -1

    def addPic(self):
        current_path = self.picPathEdit.text()
        if(current_path == ""):
            dialogMsg.warnMsg(self, "警告", "未选择文件!")
        elif(not os.path.isfile(current_path)):
            dialogMsg.warnMsg(self, "警告", "不存在该文件,可能已被删除或者更改!")
        else:
            if(self.chooseFilePath() == -1):
                return
            if((self.path + "/others") in self.chosen_path): #判断是否为应存放图片的路径
                shutil.copy(current_path, self.chosen_path) #TODO rpy文件操作以及图片移动
                dialogMsg.infoMsg(self, "信息", "已成功添加!")
                self.readFiles()
            else:
                dialogMsg.warnMsg(self, "警告", "此路径不允许存放图片")
                return

    def showPic(self): #显示图片
        #TODO 改写,加载表格中选定的内容
        try:
            index = self.tableView.currentIndex()  # 取得当前选中行的index
            pic_path = self.__getPicPath(index.row())
            if (imghdr.what(pic_path) is None):
                dialogMsg.warnMsg(self, "警告", "图片已损坏!")
                return
            pixmap = QPixmap(pic_path)
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