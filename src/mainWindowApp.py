"""
    主程序
"""
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

import sys, os, shutil

from src.ui.mainWindow import Ui_MainWindow
from dialogMsg import dialogMsg
from uiDefine import DialogAddWindow, CharaEditWindow, DialogEdit, PicEdit, WinSetting, VideoAdd
from rpyFileOperation import RpyFileOperation

from settings import Settings

class WindowApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
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

        self.actionOpen.triggered.connect(self.showFileDialog) #选择文件夹对话框
        # self.actionSettings.triggered.connect(self.showSettingWindow) #TODO 设置对话框

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
                #TODO rpy文件读入缓存
                # 进度条对话框
                self.fileOperate = RpyFileOperation(self.path) #存放用户工作区路径

    def showSettingWindow(self): #设置界面
        self.windowSet = WinSetting()
        self.windowSet.show()

        self.windowSet.btnOpenFileMana.clicked.connect()
        self.windowSet.btnSettingSave.clicked.connect(self.settingSave)
        self.windowSet.btnSettingExit.clicked.connect(self.windowSet.exitWin)

    def settingSave(self): #确认保存
        #TODO 缓存文件写入rpy
        pass

    def showNewWindow(self): #跳转窗口选项
        choice = self.comboBoxChoiceMode.currentText()
        if(choice=="添加台词"):
            self.window1 = DialogAddWindow()
            self.window1.show()

            self.window1.btnDialogEditExit.clicked.connect(self.window1.exitWin)
            # self.window1.btnDialogEditDefine.clicked.connect(self.writeDialog) #TODO 暂时禁用,因为对接正在协调
        elif(choice=="人物编辑"):
            self.window2 = CharaEditWindow()
            self.window2.show()

            self.window2.btnDialogEditExit.clicked.connect(self.window2.exitWin) #取消按钮

            self.window2.listWidget.itemSelectionChanged.connect(self.charaInfoUpdate)

            self.window2.btnDefineChara.clicked.connect(self.changeChar)
            self.window2.btnDelChara.clicked.connect(self.delChar) #删除
            self.window2.btnAddChara.clicked.connect(self.addChar) #添加
        elif(choice=="台词编辑"):
            try:
                currentDialog = self.listWidget.currentItem().text()
            except AttributeError:
                dialogMsg.warnMsg(self, "警告!", "未选择任何台词!")
                return
            self.window3 = DialogEdit()
            self.window3.show()

            self.window3.DialogEdit.setPlainText(currentDialog)
            self.window3.comboBoxChara.setCurrentText("test") #TODO 获取说此台词的人

            self.window3.btnCancel.clicked.connect(self.window3.exitWin)
            # self.window3.btnDelete.clicked.connect() #TODO 删除台词
            # self.window3.btnDefine.clicked.connect() #TODO 确认键
        elif(choice=="编辑图片列表"):
            try:
                if(self.path!=''):
                    self.window4 = PicEdit(self.path + "/images")
                    self.window4.show()
                else:
                    dialogMsg.warnMsg(self, "警告", "未正确选择工作区路径!")
                    return
            except AttributeError as e:
                dialogMsg.warnMsg(self, "警告", "未选择工作区路径!")
                return

            self.window4.btnOpenFileMana.clicked.connect(self.window4.chooseFile)
            # self.tableView.selectionChanged.connect(self.window4)
            self.window4.btnDelete.clicked.connect(self.window4.deletePic)
            # self.window4.btnAdd.clicked.connect()

            self.window4.btnReload.clicked.connect(self.window4.showPic)
            self.window4.btnDefine.clicked.connect(self.definePic)
            self.window4.btnCancel.clicked.connect(self.window4.exitWin)
        elif(choice=="添加视频"):
            self.window5 = VideoAdd()
            self.window5.show()

            self.window5.btnOpenFileMana.clicked.connect(self.window5.chooseFile)

            # self.window5.btnDefine.clicked.connect()
            self.window5.btnCancel.clicked.connect(self.window5.exitWin)
        else:
            dialogMsg.infoMsg(self, "功能未完善", f"你选择的是{self.comboBoxChoiceMode.currentText()}")

    def definePic(self): #图片添加确认键
        try:
            work_path = self.path
        except AttributeError:
            dialogMsg.warnMsg(self, "警告", "未设置工作区路径!")
            return
        if(not os.path.isdir(work_path)):
            dialogMsg.warnMsg(self, "警告", "路径无效!")
            return
        path = self.window4.picPathEdit.text()
        if(not os.path.isfile(path)):
            dialogMsg.warnMsg(self, "警告", "文件不存在!")
        else:
            try:
                name = os.path.split(path)[1]
                if not os.path.exists(work_path+"/images"):
                    os.makedirs(work_path+"/images")
                shutil.copy(path, work_path+"/images/"+name)
                #TODO 脚本文件更改(images.rpy+script.rpy)
                self.window4.exitWin()
            # 无法使用
            # except FileExistsError:
            #     dialogMsg.warnMsg(self, "警告", "文件已存在!")
            #     return
            except Exception as e:
                print(e)
                return

    def defineVideo(self): #视频添加确认键
        try:
            work_path = self.path
        except AttributeError:
            dialogMsg.warnMsg(self, "警告", "未设置工作区路径!")
            return
        if(not os.path.isdir(work_path)):
            dialogMsg.warnMsg(self, "警告", "路径无效!")
            return
        path = self.window5.chooseVideo.text()
        if(not os.path.isfile(path)):
            dialogMsg.warnMsg(self, "警告", "文件不存在!")
        else:
            try:
                name = os.path.split(path)[1]
                if not os.path.exists(work_path+"/audio"):
                    os.makedirs(work_path+"/audio")
                shutil.copy(path, work_path+"/audio/"+name)
                #TODO 脚本文件更改(script.rpy)
                self.window5.exitWin()
            # 无法使用
            # except FileExistsError:
            #     dialogMsg.warnMsg(self, "警告", "文件已存在!")
            #     return
            except Exception as e:
                print(e)
                return

    def charaInfoUpdate(self):
        try:
            self.selectedRow = self.window2.listWidget.currentItem().text()
            #TODO 通过显示名读取标签以及人物立绘前缀
            self.charaTag = 'testContent'
            self.charaPre = 'testContent'
            lst = [self.charaTag, self.selectedRow, self.charaPre]
            self.window2.setCharaInfo(lst)
        except AttributeError as e:
            dialogMsg.warnMsg(self, "警告!", "未选择任何人物!")

    def changeChar(self): #修改人物
        if (self.window2.isEmptyInfo()):
            charaTag = self.window2.charaTag.text()  # 人物标签(renpy人物变量)
            charaName = self.window2.charaName.text()  # 人物显示名
            try:
                if(charaName != self.window2.listWidget.currentItem().text()):
                    raise Exception("参数指向错误!")
            except AttributeError as e:
                dialogMsg.warnMsg(self, "警告!", "未选择任何人物!")
                return
            charaPrefix = self.window2.charaPrefix.text()  # 人物立绘前缀,格式如tohka_
            #TODO 人物标签,显示名,立绘前缀冲突判定
            #TODO 修改标签以及人物立绘前缀(文件操作)
            dialogMsg.infoMsg(self, "提示", "修改成功!")
        return


    def addChar(self): #写入人物
        if(self.window2.isEmptyInfo()):
            charaTag = self.window2.charaTag.text()        #人物标签(renpy人物变量)
            charaName = self.window2.charaName.text()      #人物显示名
            charaPrefix = self.window2.charaPrefix.text()  #人物立绘前缀,格式如tohka_
            charaPrefix += '_'
            #TODO 人物标签,显示名,立绘前缀冲突判定(2)
            #TODO 人物添加文件读写(此处为写入文件)
            self.window2.listWidget.addItem(charaName)
            self.window2.clearInput()
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

    def showAbout(self):
        dialogMsg.infoMsg(self, "关于", "Renpy脚本编辑器UI版\n版本v0.0.1")

    @staticmethod
    def showGithub():
        QDesktopServices.openUrl(QUrl("https://github.com/MRSlouzk/Renpy-editor"))

    def showAuthor(self):
        dialogMsg.infoMsg(self, "制作信息", "程序/UI:MRSlouzk(Github)\n程序:爱喝矿泉水\n程序:Hzrr(Github)")

    @staticmethod
    def showHelp():
        #TODO 软件帮助链接,暂用仓库链接替代
        QDesktopServices.openUrl(QUrl("https://github.com/MRSlouzk/Renpy-editor"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowApp()
    sys.exit(app.exec())