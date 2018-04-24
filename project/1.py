import  mainWindow

from PyQt5 import QtWidgets,QtCore,QtGui
import sys
if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    #主窗口
    mW=QtWidgets.QMainWindow()
    #创建主窗口的UI
    mW_ui=mainWindow.Ui_MainWindow()
    #设置主窗口的UI
    mW_ui.setupUi(mW)
    #显示窗口
    mW.show()
    sys.exit(app.exec_())