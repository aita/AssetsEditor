# -*- coding:utf-8 -*-
import os
import json
from PyQt5.QtCore import QObject


class Project(QObject):
    CONFIG_FILENAME = "assets.json"
    DEFAULT_DIRECTORIES = ("Images", "Properties")

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
        project.initConfig()
        project.createRootDir()
        project.createConfigJSON()
        project.createDefaultDirectories()
        return project

    @classmethod
    def open(cls, configPath):
        config = cls.loadConfigJSON(configPath)
        if config is None:
            return None
        parentDir = os.path.dirname(os.path.dirname(configPath))
        project = Project(config['name'], parentDir)
        project.config = config
        return project

    @classmethod
    def loadConfigJSON(self, path):
        with open(path) as io:
            config = json.load(io)
        # TODO: Validate the config
        return config

    def initConfig(self):
        self.config = {
            'name': self.name,
            # 'ignores': [],
        }

    def createRootDir(self):
        if os.path.exists(self.path):
            return
        os.mkdir(self.path)

    def createConfigJSON(self):
        jsonPath = os.path.join(self.path, self.CONFIG_FILENAME)
        with open(jsonPath, "w") as io:
            json.dump(self.config, io)

    def createDefaultDirectories(self):
        for name in self.DEFAULT_DIRECTORIES:
            path = os.path.join(self.path, name)
            if not os.path.exists(path):
                os.mkdir(path)
