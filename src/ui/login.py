# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_login(object):
    def setupUi(self, Form_login):
        Form_login.setObjectName("Form_login")
        Form_login.resize(895, 558)
        Form_login.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/miku.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_login.setWindowIcon(icon)
        Form_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form_login.setAutoFillBackground(False)
        Form_login.setStyleSheet("border-image: url(:/bg/kiminonawa.jpg);")
        self.input_user = QtWidgets.QLineEdit(Form_login)
        self.input_user.setGeometry(QtCore.QRect(280, 230, 341, 21))
        self.input_user.setStyleSheet("border-image: url();\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: none;\n"
"text-align:center;")
        self.input_user.setInputMask("")
        self.input_user.setText("")
        self.input_user.setAlignment(QtCore.Qt.AlignCenter)
        self.input_user.setObjectName("input_user")
        self.input_pwd = QtWidgets.QLineEdit(Form_login)
        self.input_pwd.setGeometry(QtCore.QRect(280, 270, 341, 21))
        self.input_pwd.setStyleSheet("border-image: url();\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: none;\n"
"text-align:center;")
        self.input_pwd.setInputMask("")
        self.input_pwd.setText("")
        self.input_pwd.setAlignment(QtCore.Qt.AlignCenter)
        self.input_pwd.setObjectName("input_pwd")
        self.btn_login = QtWidgets.QPushButton(Form_login)
        self.btn_login.setGeometry(QtCore.QRect(390, 310, 131, 21))
        self.btn_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_login.setStyleSheet("border-image: url();\n"
"background-color: rgba(255, 255, 255, 50);\n"
"border: none;\n"
"color: rgba(0 , 0 , 0, 120);")
        self.btn_login.setAutoDefault(True)
        self.btn_login.setDefault(False)
        self.btn_login.setFlat(False)
        self.btn_login.setObjectName("btn_login")

        self.retranslateUi(Form_login)
        QtCore.QMetaObject.connectSlotsByName(Form_login)

    def retranslateUi(self, Form_login):
        _translate = QtCore.QCoreApplication.translate
        Form_login.setWindowTitle(_translate("Form_login", "AutoBet"))
        self.input_user.setPlaceholderText(_translate("Form_login", "打你的帳號　ಠ- ಠ"))
        self.input_pwd.setPlaceholderText(_translate("Form_login", "啊密碼勒　　ಠ- ಠ"))
        self.btn_login.setText(_translate("Form_login", "登入"))

import src.ui.style_rc
