# Form implementation generated from reading ui file 'editAnimation.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_editAnimation(object):
    def setupUi(self, editAnimation):
        editAnimation.setObjectName("editAnimation")
        editAnimation.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        editAnimation.resize(600, 520)
        self.labelAni = QtWidgets.QLabel(editAnimation)
        self.labelAni.setGeometry(QtCore.QRect(380, 10, 201, 501))
        self.labelAni.setObjectName("labelAni")
        self.cobChara = QtWidgets.QComboBox(editAnimation)
        self.cobChara.setGeometry(QtCore.QRect(20, 40, 80, 22))
        self.cobChara.setObjectName("cobChara")
        self.comboBox_2 = QtWidgets.QComboBox(editAnimation)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 40, 80, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(editAnimation)
        self.label.setGeometry(QtCore.QRect(30, 15, 55, 21))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.cobFace = QtWidgets.QLabel(editAnimation)
        self.cobFace.setGeometry(QtCore.QRect(140, 15, 55, 21))
        self.cobFace.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cobFace.setObjectName("cobFace")
        self.btnLoad = QtWidgets.QPushButton(editAnimation)
        self.btnLoad.setGeometry(QtCore.QRect(260, 20, 80, 24))
        self.btnLoad.setObjectName("btnLoad")
        self.pushButton = QtWidgets.QPushButton(editAnimation)
        self.pushButton.setGeometry(QtCore.QRect(260, 60, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.btnAddChara = QtWidgets.QPushButton(editAnimation)
        self.btnAddChara.setGeometry(QtCore.QRect(20, 80, 80, 24))
        self.btnAddChara.setObjectName("btnAddChara")
        self.btnAddFace = QtWidgets.QPushButton(editAnimation)
        self.btnAddFace.setGeometry(QtCore.QRect(130, 80, 80, 24))
        self.btnAddFace.setObjectName("btnAddFace")

        self.retranslateUi(editAnimation)
        QtCore.QMetaObject.connectSlotsByName(editAnimation)

    def retranslateUi(self, editAnimation):
        _translate = QtCore.QCoreApplication.translate
        editAnimation.setWindowTitle(_translate("editAnimation", "????????????"))
        self.labelAni.setText(_translate("editAnimation", "TODO???????????????"))
        self.label.setText(_translate("editAnimation", "??????"))
        self.cobFace.setText(_translate("editAnimation", "??????"))
        self.btnLoad.setText(_translate("editAnimation", "??????"))
        self.pushButton.setText(_translate("editAnimation", "??????"))
        self.btnAddChara.setText(_translate("editAnimation", "????????????"))
        self.btnAddFace.setText(_translate("editAnimation", "????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editAnimation = QtWidgets.QWidget()
    ui = Ui_editAnimation()
    ui.setupUi(editAnimation)
    editAnimation.show()
    sys.exit(app.exec())
