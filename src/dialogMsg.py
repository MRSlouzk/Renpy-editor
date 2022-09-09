"""
    对话框类
"""
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QDialog, QMessageBox

import typing

class dialogMsg(QDialog):
    @staticmethod
    def infoMsg(self, title: str, msg):
        QMessageBox.information(self, title, msg)

    @staticmethod
    def warnMsg(self, title: str, msg):
        QMessageBox.warning(self, title, msg)