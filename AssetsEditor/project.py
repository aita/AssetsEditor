# -*- coding:utf-8 -*-
import os
import json
from PyQt5.QtCore import QObject


class Project(QObject):
    CONFIG_FILENAME = "assets.json"
    DEFAULT_DIRECTORIES = (
        "Images",
        "Properties",
        "Scenes",
        "Sounds",
        "Shaders",
        "Textures",
    )

    def __init__(self, name, rootDir):
        self.name = name
        self.rootDir = rootDir
        self.config = None

    @property
    def path(self):
        return self.rootDir

    @property
    def configJSONPath(self):
        return Project.getConfigJSONPath(self.rootDir)

    @classmethod
    def getConfigJSONPath(cls, rootDir):
        return os.path.join(rootDir, cls.CONFIG_FILENAME)

    @classmethod
    def new(cls, name, rootDir):
        project = Project(name, rootDir)
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
        rootDir = os.path.dirname(configPath)
        project = Project(config['name'], rootDir)
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

    def createConfigJSON(self):
        with open(self.configJSONPath, "w") as io:
            self.dumpConfigJSON(io)

    def dumpConfigJSON(self, io):
        json.dump(self.config, io, indent=2)

    def createRootDir(self):
        if os.path.exists(self.path):
            return
        os.mkdir(self.path)

    def createDefaultDirectories(self):
        for name in self.DEFAULT_DIRECTORIES:
            path = os.path.join(self.path, name)
            if not os.path.exists(path):
                os.mkdir(path)
