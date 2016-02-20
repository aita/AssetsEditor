# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QWidget, QTableWidget

class SpreadSheet(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        rows = cols = 10
        self.table = QTableWidget(rows, cols, self)
        self.table.setSizeAdjustPolicy(QTableWidget.AdjustToContents)
