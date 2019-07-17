# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_check(object):
    def setupUi(self, Form_check):
        Form_check.setObjectName("Form_check")
        Form_check.setEnabled(True)
        Form_check.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/miku.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_check.setWindowIcon(icon)
        Form_check.setStyleSheet("")
        self.bg = QtWidgets.QLabel(Form_check)
        self.bg.setGeometry(QtCore.QRect(30, 20, 565, 344))
        self.bg.setStyleSheet("border-image: url(:/bg/yuki.png);\n"
"border-color: rgba(12, 12, 12, 0);\n"
"background-image: url();\n"
"background-color: rgba(12, 12, 12, 0);\n"
"border-radius: 70px;")
        self.bg.setText("")
        self.bg.setObjectName("bg")
        self.btn_fixnum = QtWidgets.QPushButton(Form_check)
        self.btn_fixnum.setGeometry(QtCore.QRect(90, 70, 121, 51))
        self.btn_fixnum.setStyleSheet("background-color: rgba(120, 120, 120, 80);\n"
"background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.btn_fixnum.setObjectName("btn_fixnum")
        self.btn_rannum = QtWidgets.QPushButton(Form_check)
        self.btn_rannum.setGeometry(QtCore.QRect(90, 140, 121, 51))
        self.btn_rannum.setStyleSheet("background-color: rgba(120, 120, 120, 80);\n"
"background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.btn_rannum.setObjectName("btn_rannum")
        self.btn_cancel = QtWidgets.QPushButton(Form_check)
        self.btn_cancel.setGeometry(QtCore.QRect(90, 280, 121, 51))
        self.btn_cancel.setStyleSheet("background-color: rgba(120, 120, 120, 80);\n"
"background-image: url();\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.btn_cancel.setObjectName("btn_cancel")

        self.retranslateUi(Form_check)
        QtCore.QMetaObject.connectSlotsByName(Form_check)

    def retranslateUi(self, Form_check):
        _translate = QtCore.QCoreApplication.translate
        Form_check.setWindowTitle(_translate("Form_check", "Form"))
        self.btn_fixnum.setText(_translate("Form_check", "固定號碼"))
        self.btn_rannum.setText(_translate("Form_check", "機選"))
        self.btn_cancel.setText(_translate("Form_check", "∑(ι´Дン)ノ"))

import src.ui.style_rc
