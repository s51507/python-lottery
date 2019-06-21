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
        Form_login.resize(332, 255)
        Form_login.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/初音/12.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_login.setWindowIcon(icon)
        Form_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form_login.setAutoFillBackground(False)
        Form_login.setStyleSheet("border-image: url(:/bg/halfmoon.jpg);")
        self.lb_user = QtWidgets.QLabel(Form_login)
        self.lb_user.setGeometry(QtCore.QRect(10, 30, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lb_user.setFont(font)
        self.lb_user.setStyleSheet("border-image: url();\n"
                                   "color: rgb(255, 255, 255);")
        self.lb_user.setObjectName("lb_user")
        self.input_user = QtWidgets.QLineEdit(Form_login)
        self.input_user.setGeometry(QtCore.QRect(50, 30, 121, 21))
        self.input_user.setStyleSheet("border-image: url();")
        self.input_user.setInputMask("")
        self.input_user.setText("")
        self.input_user.setObjectName("input_user")
        self.lb_pwd = QtWidgets.QLabel(Form_login)
        self.lb_pwd.setGeometry(QtCore.QRect(10, 70, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lb_pwd.setFont(font)
        self.lb_pwd.setStyleSheet("border-image: url();\n"
                                  "color: rgb(255, 255, 255);")
        self.lb_pwd.setObjectName("lb_pwd")
        self.input_pwd = QtWidgets.QLineEdit(Form_login)
        self.input_pwd.setGeometry(QtCore.QRect(50, 70, 121, 21))
        self.input_pwd.setStyleSheet("border-image: url();")
        self.input_pwd.setInputMask("")
        self.input_pwd.setText("")
        self.input_pwd.setObjectName("input_pwd")
        self.btn_login = QtWidgets.QPushButton(Form_login)
        self.btn_login.setGeometry(QtCore.QRect(40, 180, 81, 31))
        self.btn_login.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_login.setStyleSheet("border-image: url();")
        self.btn_login.setAutoDefault(False)
        self.btn_login.setObjectName("btn_login")
        self.lb_pwd.raise_()
        self.lb_user.raise_()
        self.input_user.raise_()
        self.input_pwd.raise_()
        self.btn_login.raise_()

        self.retranslateUi(Form_login)
        QtCore.QMetaObject.connectSlotsByName(Form_login)

    def retranslateUi(self, Form_login):
        _translate = QtCore.QCoreApplication.translate
        Form_login.setWindowTitle(_translate("Form_login", "AutoBet"))
        self.lb_user.setText(_translate("Form_login", "帳號："))
        self.input_user.setPlaceholderText(_translate("Form_login", "              ಠ- ಠ"))
        self.lb_pwd.setText(_translate("Form_login", "密碼："))
        self.input_pwd.setPlaceholderText(_translate("Form_login", "              ಠ- ಠ"))
        self.btn_login.setText(_translate("Form_login", "登入"))


import src.ui.style_rc
