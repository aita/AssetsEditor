# -*- coding:utf-8 -*-
# from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget)


class SpreadSheet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        rows = cols = 10
        self.table = QTableWidget(rows, cols, self)
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
        layout.addWidget(self.table)

        self.setLayout(layout)
