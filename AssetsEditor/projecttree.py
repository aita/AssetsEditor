# -*- coding:utf-8 -*-
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QTreeView, QFileSystemModel
# from PyQt5.QtGui import QIcon


class ProjectTree(QTreeView):
    fileOpen = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.project = None
        self.header().close()
        self.doubleClicked.connect(self.onDoubleClicked)

    def load(self, project):
        self.project = project
        model = QFileSystemModel()
        model.setRootPath(self.project.path)
        self.setModel(model)
        self.setRootIndex(model.index(self.project.path))
        # show only file names
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)

    def onDoubleClicked(self, modelIndex):
        filePath = modelIndex.model().filePath(modelIndex)
        if os.path.isfile(filePath):
            self.fileOpen.emit(filePath)
