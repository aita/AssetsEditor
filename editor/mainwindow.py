# -*- coding:utf-8 -*-
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QMainWindow, QDockWidget, QTabWidget
from .spreadsheet import SpreadSheet
from .projecttree import ProjectTree

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(SpreadSheet(), "sheet1")
        self.tabWidget.addTab(SpreadSheet(), "sheet2")
        self.setCentralWidget(self.tabWidget)

        self.projectTree = ProjectTree()
        dockWidget = QDockWidget("Project", self)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(self.projectTree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)
