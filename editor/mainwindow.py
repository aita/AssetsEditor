# -*- coding:utf-8 -*-
import os
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QDockWidget, QTabWidget,
    qApp, QAction,
    QMessageBox,
)
from PyQt5.QtGui import QIcon

from .project import Project
from .projectdialog import NewProjectDialog
from .projecttree import ProjectTree
from .spreadsheet import SpreadSheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.project = None
        self.initMenu()
        self.initWidgets()

    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')

        newAction = QAction(QIcon('new.png'), '&New Project', self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New Project')
        newAction.triggered.connect(self.newProject)
        fileMenu.addAction(newAction)

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

    def initWidgets(self):
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)

        self.projectTree = ProjectTree()
        dockWidget = QDockWidget("Project", self)
        dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(self.projectTree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

    def newProject(self):
        projectConfig = NewProjectDialog.getNewProjectConfig(self)
        if projectConfig is None:
            return
        projectName, parentDir = projectConfig
        if os.path.exists(os.path.join(projectName, parentDir)):
            QMessageBox.warning(self, "",
                "The project already exists.", QMessageBox.Ok)
            return
        self.open(Project.new(projectName, parentDir))

    def open(self, project):
        self.project = project
        self.projectTree.load(self.project)
