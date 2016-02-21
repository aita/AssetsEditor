# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon


class ProjectTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setColumnCount(1)
        self.header().close()

    def load(self, project):
        # Add directories
        for name in("Images", "Sheets"):
            item = QTreeWidgetItem([name])
            item.setIcon(0, QIcon("folder.png"))
            self.addTopLevelItem(item)
