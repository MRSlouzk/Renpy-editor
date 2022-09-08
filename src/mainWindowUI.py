"""
    UI布局
"""
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 22))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.edit_menu = QtWidgets.QMenu(self.menubar)
        self.edit_menu.setObjectName("edit_menu")
        self.mode_menu = QtWidgets.QMenu(self.menubar)
        self.mode_menu.setObjectName("mode_menu")
        self.about_menu = QtWidgets.QMenu(self.menubar)
        self.about_menu.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setStatusTip("打开文件目录")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setStatusTip("存储文件")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setStatusTip("退出程序")

        self.actionAuthor = QtGui.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionAuthor.setStatusTip("作者")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.setStatusTip("关于")
        self.actionGithub = QtGui.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionGithub.setStatusTip("Github链接")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setStatusTip("帮助")

        self.file_menu.addAction(self.actionOpen)
        self.file_menu.addAction(self.actionSave)
        self.file_menu.addAction(self.actionExit)
        self.about_menu.addAction(self.actionAuthor)
        self.about_menu.addAction(self.actionAbout)
        self.about_menu.addAction(self.actionGithub)
        self.about_menu.addAction(self.actionHelp)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.edit_menu.menuAction())
        self.menubar.addAction(self.mode_menu.menuAction())
        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenpyEditor"))
        self.file_menu.setTitle(_translate("MainWindow", "文件"))
        self.edit_menu.setTitle(_translate("MainWindow", "编辑"))
        self.mode_menu.setTitle(_translate("MainWindow", "模式"))
        self.about_menu.setTitle(_translate("MainWindow", "关于"))
        self.actionOpen.setText(_translate("MainWindow", "打开"))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionExit.setText(_translate("MainWindow", "退出"))
        self.actionAuthor.setText(_translate("MainWindow", "制作信息"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionGithub.setText(_translate("MainWindow", "Github仓库"))
        self.actionHelp.setText(_translate("MainWindow", "帮助"))