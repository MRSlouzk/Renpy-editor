"""
    主程序
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

import sys, os

from mainWindow import Ui_MainWindow
from dialogMsg import dialogMsg
from uiDefine import DialogEditWindow, CharaEditWindow
from rpyFileOperation import RpyFileOperation

class WindowApp(QMainWindow, Ui_MainWindow):
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

        self.actionOpen.triggered.connect(self.showFileDialog)#选择文件夹对话框

        self.pushButtonEnter.clicked.connect(self.showNewWindow)

    def showFileDialog(self):
        fp_name = QFileDialog.getExistingDirectoryUrl(self, "选择工作区文件夹", QUrl("./"))
        if(not fp_name.isEmpty()): #防止用户直接关闭窗口
            self.path = fp_name.path().lstrip('/') #工作区文件夹路径,类型为str
            if(not os.path.exists(self.path + '/rpy/script.rpy')):
                dialogMsg.warnMsg(self, "不存在renpy脚本文件!", "请确认你选择的目录下存在rpy文件夹,其中包含script.rpy文件\n"
                                                         "如果没有,请尝试重新创建工程!")
                self.path = ''
            else:
                self.fileOperate = RpyFileOperation(self.path) #存放用户工作区路径

    def showNewWindow(self): #跳转窗口选项
        if(self.comboBoxChoiceMode.currentText()=="台词编辑"):
            self.window1 = DialogEditWindow()
            self.window1.show()

            self.window1.btnDialogEditExit.clicked.connect(self.window1.exitWin)
            # self.window1.btnDialogEditDefine.clicked.connect(self.writeDialog) #TODO 暂时禁用,因为对接正在协调
        elif(self.comboBoxChoiceMode.currentText()=="人物编辑"):
            self.window2 = CharaEditWindow()
            self.window2.show()

            self.window2.btnDialogEditExit.clicked.connect(self.window2.exitWin)

            # self.window2.btnDefineChara.clicked.connect()
            self.window2.btnDelChara.clicked.connect(self.delChar)
            self.window2.btnAddChara.clicked.connect(self.addChar)
        else:
            dialogMsg.infoMsg(self, "功能未完善", f"你选择的是{self.comboBoxChoiceMode.currentText()}")
        # self.window1.close()

    def addChar(self): #写入人物
        charaTag = self.window2.charaTag.text()        #人物标签(renpy人物变量)
        charaName = self.window2.charaName.text()      #人物显示名
        charaPrefix = self.window2.charaPrefix.text()  #人物立绘前缀,格式如tohka_
        if(not charaTag):
            dialogMsg.warnMsg(self, "错误!", "未设置人物标签!")
        elif(not charaName):
            dialogMsg.warnMsg(self, "错误!", "未设置人物名!")
        elif(not charaPrefix):
            dialogMsg.warnMsg(self, "错误!", "未设置人物立绘前缀!")
        else:
            charaPrefix += '_'
            #TODO 新添加的与已存在的内容冲突报错
            #TODO 人物添加文件读写(此处为写入文件)
            self.window2.listWidget.addItem(charaName)
            self.window2.charaTag.setText("")
            self.window2.charaName.setText("")
            self.window2.charaPrefix.setText("")
        return

    def delChar(self):
        try:
            selectedRow = self.window2.listWidget.currentItem().text()
            #TODO 删除文件内容对接
            self.window2.listWidget.takeItem(self.window2.listWidget.currentRow())
        except AttributeError as e:
            dialogMsg.warnMsg(self, "警告!", "未选择任何人物!")
        return

    def writeDialog(self): #写入台词
        char = self.window1.comboBoxCharacter.currentText() #人物显示名
        dial = self.window1.DialogInput.toPlainText()       #台词内容
        if(dial == ''):
            dialogMsg.warnMsg(self, "错误!", "台词为空!")
            return
        #TODO 此处具体功能待对接

        # try:
        #     self.fileOperate.writeDialog(char, dial)
        # except AttributeError as e:
        #     print(e)
        #     dialogMsg.warnMsg(self, "错误!", "未选择工作区!")
        # self.window1.exitWin()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowApp()
    sys.exit(app.exec())