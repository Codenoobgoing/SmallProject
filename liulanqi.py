from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class Mainwindow(QMainWindow):
    def __init__(self,*args,**Kwargs):
        super().__init__(*args,**Kwargs)

        #设置窗口标题
        self.setWindowTitle('My first App')

        #设置标签
        lable = QLabel('welcom to there')
        #设置标签显示在中央
        lable.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(lable)

app = QApplication(sys.argv)

window = Mainwindow()

window.show()

app.exec()