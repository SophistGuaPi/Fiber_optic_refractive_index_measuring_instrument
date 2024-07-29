#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :gui.py
# @Time      :2024/7/29 
# @Author    :SophistGuaPi

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

import src.dependent_env.instrument as instrument
from src.config import conf

# gui类
class Gui:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = instrument.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    gui = Gui()
