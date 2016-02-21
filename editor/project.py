# -*- coding:utf-8 -*-
import os
import json
from PyQt5.QtCore import QObject


class Project(QObject):
    CONFIG_FILENAME = "assets.json"
    DEFAULT_DIRECTORIES = ("Images", "Data")

    def __init__(self, name, parentDir):
        self.name = name
        self.parentDir = parentDir
        self.config = None

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

    def initConfig(self):
        self.config = {
            'name': self.name,
            # 'ignores': [],
        }

    def createConfigJSON(self):
        jsonPath = os.path.join(self.path, self.CONFIG_FILENAME)
        with open(jsonPath, "w") as io:
            json.dump(self.config, io)

    def createDefaultDirectories(self):
        for name in self.DEFAULT_DIRECTORIES:
            path = os.path.join(self.path, name)
            if not os.path.exists(path):
                os.mkdir(path)
