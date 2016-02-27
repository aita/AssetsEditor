# -*- coding:utf-8 -*-
import os
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    qApp,
    QAction,
    QMainWindow,
    QDockWidget,
    QTabWidget,
    QTextEdit,
    QFileDialog,
    QMessageBox,
)

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

        openAction = QAction(QIcon('open.png'), '&Open Project', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open Project')
        openAction.triggered.connect(self.openProject)
        fileMenu.addAction(openAction)

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

        self.projectTree.fileOpen.connect(self.openFile)

    def newProject(self):
        projectConfig = NewProjectDialog.getNewProjectConfig(self)
        if projectConfig is None:
            return
        projectName, parentDir = projectConfig['name'], projectConfig['parentDir']
        rootDir = os.path.join(parentDir, projectName)
        if os.path.exists(Project.getConfigJSONPath(rootDir)):
            QMessageBox.warning(
                self, "", "The project already exists.", QMessageBox.Ok)
            return
        self._openProject(Project.new(projectName, rootDir))

    def openProject(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "", os.path.expanduser("~"),
            "Assets files ({filename})".format(filename=Project.CONFIG_FILENAME))
        if not path:
            return
        project = Project.open(path)
        if project is None:
            QMessageBox.critical(
                self, "", "Colud not open the project.", QMessageBox.Ok)
            return
        self._openProject(project)

    def _openProject(self, project):
        self.project = project
        self.projectTree.load(self.project)

    def openFile(self, filePath):
        _, ext = os.path.splitext(filePath)
        if ext in ('.txt', '.json'):
            self.openTextFile(filePath)
        if ext in ('.png', '.jpeg', '.bmp'):
            self.openImageFile(filePath)

    def openTextFile(self, filePath):
        with open(filePath) as fp:
            text = fp.read()
        textEdit = QTextEdit(text)
        textEdit.setReadOnly(True)
        self.tabWidget.addTab(textEdit, os.path.basename(filePath))

    def openImageFile(self, filePath):
        pass
