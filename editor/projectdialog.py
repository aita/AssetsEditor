# -*- coding:utf-8 -*-
import os

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (
     QDialog, QGridLayout, QLayout,
    QLabel, QLineEdit, QDialogButtonBox,
)


class NewProjectDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QGridLayout(self)
        layout.setSizeConstraint(QLayout.SetFixedSize);

        layout.addWidget(QLabel("Parent Directory"), 0, 0)
        self.parentDirectoryEdit = QLineEdit(os.path.expanduser("~"), self)
        layout.addWidget(self.parentDirectoryEdit, 0, 1)

        layout.addWidget(QLabel("Project Name"), 1, 0)
        self.projectNameEdit = QLineEdit(self)
        layout.addWidget(self.projectNameEdit, 1, 1)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons, 2, 1)

    def done(self, result):
        if QDialog.Accepted == result:
            if self.parentDirectory == "" or self.projectName == "":
                return
            if not os.path.exists(self.parentDirectory):
                return
            if not os.path.isdir(self.parentDirectory):
                return
        super().done(result)
        return

    @property
    def parentDirectory(self):
        return self.parentDirectoryEdit.text()

    @property
    def projectName(self):
        return self.projectNameEdit.text()

    @classmethod
    def getNewProjectConfig(cls, parent=None):
        dialog = cls(parent)
        result = dialog.exec_()
        if result != QDialog.Accepted:
            return None
        return dialog.projectName, dialog.parentDirectory
