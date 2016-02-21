# -*- coding:utf-8 -*-
import os
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon


class ProjectTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.project = None
        self.setColumnCount(1)
        self.header().close()

    def load(self, project):
        self.project = project
        root = self.addChildren(None, self.project.path)
        self.addTopLevelItem(root)

    def addChildren(self, parent, path):
        name = os.path.basename(path)
        item = QTreeWidgetItem(parent, [name])
        if os.path.isdir(path):
            for name in sorted(os.listdir(path)):
                self.addChildren(item, os.path.join(path, name))
        return item
