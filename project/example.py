# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 21:24
# @Author  : weic
# @FileName: example.py
# @Software: PyCharm
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication
class Communicate(QObject):
    closeApp = pyqtSignal()
class exp(QMainWindow):
    """docstring for ex"""
    def __init__(self):
        super(exp, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(400, 400, 500, 300)
        self.setWindowTitle('Emitting')
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = exp()
    ex.show()
    sys.exit(app.exec_())

