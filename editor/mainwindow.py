# -*- coding:utf-8 -*-
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (
    QMainWindow, QDockWidget, QTabWidget,
    qApp, QAction
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
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(self.projectTree)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

    def newProject(self):
        projectConfig = NewProjectDialog.getNewProjectName(self)
        if projectConfig is None:
            return

        projectName, parentDirectory = projectConfig
        project = Project(projectName, parentDirectory)
        self.open(project)

    def open(self, project):
        pass
