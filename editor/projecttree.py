# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QTreeWidget


class ProjectTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__()
