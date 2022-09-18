"""
    对话框类
"""
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QMessageBox, QDialogButtonBox

import typing

class dialogMsg(QDialog):
    @staticmethod
    def infoMsg(self, title: str, msg):
        QMessageBox.information(self, title, msg)

    @staticmethod
    def warnMsg(self, title: str, msg):
        QMessageBox.warning(self, title, msg)

    @staticmethod
    def queryMsg(self, title: str, msg) -> bool:
        """
            弹出问询对话框
        :param self: 窗口对象
        :param title: 问询对话框标题
        :param msg: 问询对话框内容
        :return: True(用户选择是)/False(用户选择否)
        """
        btn = QMessageBox.question(self, title, msg)
        if(btn.__repr__() == QDialogButtonBox.StandardButton.Yes.__repr__()):
            return True
        else:
            return False