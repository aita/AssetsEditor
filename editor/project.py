# -*- coding:utf-8 -*-
from PyQt5.QtCore import QObject


class Project(QObject):
    def __init__(self, name, parentDirectory):
        self.name = name
        self.parentDirectory = parentDirectory
