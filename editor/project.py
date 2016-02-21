# -*- coding:utf-8 -*-
import os
from PyQt5.QtCore import QObject


class Project(QObject):
    DEFAULT_DIRECTORIES = ("Images", "Data")

    def __init__(self, name, parentDir):
        self.name = name
        self.parentDir = parentDir

    @property
    def path(self):
        return os.path.join(self.parentDir, self.name)

    @classmethod
    def new(cls, name, parentDir):
        project = Project(name, parentDir)
        if not os.path.exists(project.path):
            os.mkdir(project.path)
        project.createConfigJSON()
        project.createDefaultDirectories()
        return project

    def createConfigJSON(self):
        pass

    def createDefaultDirectories(self):
        for name in self.DEFAULT_DIRECTORIES:
            path = os.path.join(self.path, name)
            if not os.path.exists(path):
                os.mkdir(path)
