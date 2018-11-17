# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 56, 12))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 231, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 231, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.lineEdit_2.returnPressed.connect(self.pushButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "로그인"))
        self.label.setText(_translate("MainWindow", "ID  :"))
        self.label_2.setText(_translate("MainWindow", "PW :"))
        self.pushButton.setText(_translate("MainWindow", "로그인"))

class myWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def pushButtonClicked(self):
        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        html = requests.get('http://175.195.214.55/pyy/getUserInfo.php?id={}&pw={}'.format(id, pw))
        res = html.text.strip()
        try:
            status, expire, conneting = res.split('<br>')[:3]
            print(status)
            print(expire)
            print(conneting)
            QMessageBox.about(self, "라이센스 만료 알림","[ %s ]고객님 환영합니다.\n\n라이센스 만료일 :  ~ %s 까지 입니다.\n추가이용을 원하시면 라이센스 재구매를 부탁드립니다.    "
                              % (id,expire))
            QtWidgets.QApplication.quit()
        except:
            QMessageBox.about(self, "로그인", "로그인 실패하셨습니다. \nID 와 PW를 확인해주세요 ")

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 230)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 56, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 56, 12))
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 231, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 80, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")



        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 120, 231, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.lineEdit_2.returnPressed.connect(self.pushButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "로그인"))
        self.label.setText(_translate("MainWindow", "ID  :"))
        self.label_2.setText(_translate("MainWindow", "PW :"))
        self.pushButton.setText(_translate("MainWindow", "로그인"))

class myWindow2(QMainWindow,Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def pushButtonClicked(self):
        id = self.lineEdit.text()
        pw = self.lineEdit_2.text()
        html = requests.get('http://175.195.214.55/pyy/getUserInfo.php?id={}&pw={}'.format(id, pw))
        res = html.text.strip()
        try:
            status, expire, conneting = res.split('<br>')[:3]
            print(status)
            print(expire)
            print(conneting)
            QMessageBox.about(self, "라이센스 만료 알림","[ %s ]고객님 환영합니다.\n\n라이센스 만료일 :  ~ %s 까지 입니다.\n추가이용을 원하시면 라이센스 재구매를 부탁드립니다.    "
                              % (id,expire))

        except:
            QMessageBox.about(self, "로그인", "로그인 실패하셨습니다. \nID 와 PW를 확인해주세요 ")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myWindow()
    window.show()
    app.exec_()

    window = myWindow2()
    window.show()
    app.exec_()


