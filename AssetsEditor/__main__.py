# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from .mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
