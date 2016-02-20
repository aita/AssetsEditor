# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import  QMainWindow
from .spreadsheet import SpreadSheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.spreadsheet = SpreadSheet()
        self.setCentralWidget(self.spreadsheet)
