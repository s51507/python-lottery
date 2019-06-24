# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bet.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_bet(object):
    def setupUi(self, Form_bet):
        Form_bet.setObjectName("Form_bet")
        Form_bet.resize(895, 671)
        Form_bet.setStyleSheet("background-image: url(:/bg/halfmoon.jpg);")
        self.lotterys = QtWidgets.QTabWidget(Form_bet)
        self.lotterys.setGeometry(QtCore.QRect(30, 30, 441, 121))
        self.lotterys.setAutoFillBackground(False)
        self.lotterys.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url(:/bg/halfmoon_2.jpg);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: none;")
        self.lotterys.setTabPosition(QtWidgets.QTabWidget.North)
        self.lotterys.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.lotterys.setObjectName("lotterys")
        self.tab_ssc = QtWidgets.QWidget()
        self.tab_ssc.setAutoFillBackground(False)
        self.tab_ssc.setStyleSheet("")
        self.tab_ssc.setObjectName("tab_ssc")
        self.btn_xjssc = QtWidgets.QPushButton(self.tab_ssc)
        self.btn_xjssc.setGeometry(QtCore.QRect(340, 10, 71, 23))
        self.btn_xjssc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_xjssc.setObjectName("btn_xjssc")
        self.btn_jsssc = QtWidgets.QPushButton(self.tab_ssc)
        self.btn_jsssc.setGeometry(QtCore.QRect(100, 10, 71, 23))
        self.btn_jsssc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_jsssc.setObjectName("btn_jsssc")
        self.btn_lmssc = QtWidgets.QPushButton(self.tab_ssc)
        self.btn_lmssc.setGeometry(QtCore.QRect(180, 10, 71, 23))
        self.btn_lmssc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_lmssc.setObjectName("btn_lmssc")
        self.btn_cqssc = QtWidgets.QPushButton(self.tab_ssc)
        self.btn_cqssc.setGeometry(QtCore.QRect(20, 10, 71, 23))
        self.btn_cqssc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_cqssc.setObjectName("btn_cqssc")
        self.btn_txffc = QtWidgets.QPushButton(self.tab_ssc)
        self.btn_txffc.setGeometry(QtCore.QRect(260, 10, 71, 23))
        self.btn_txffc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_txffc.setObjectName("btn_txffc")
        self.v_cqssc = QtWidgets.QWidget(self.tab_ssc)
        self.v_cqssc.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_cqssc.setFont(font)
        self.v_cqssc.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_cqssc.setObjectName("v_cqssc")
        self.btn_cqssc_1 = QtWidgets.QPushButton(self.v_cqssc)
        self.btn_cqssc_1.setGeometry(QtCore.QRect(30, 10, 91, 61))
        self.btn_cqssc_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_cqssc_1.setObjectName("btn_cqssc_1")
        self.btn_cqssc_2 = QtWidgets.QPushButton(self.v_cqssc)
        self.btn_cqssc_2.setGeometry(QtCore.QRect(170, 10, 91, 61))
        self.btn_cqssc_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_cqssc_2.setObjectName("btn_cqssc_2")
        self.btn_cqssc_3 = QtWidgets.QPushButton(self.v_cqssc)
        self.btn_cqssc_3.setGeometry(QtCore.QRect(310, 10, 91, 61))
        self.btn_cqssc_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_cqssc_3.setObjectName("btn_cqssc_3")
        self.v_jsssc = QtWidgets.QWidget(self.tab_ssc)
        self.v_jsssc.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_jsssc.setFont(font)
        self.v_jsssc.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_jsssc.setObjectName("v_jsssc")
        self.btn_jsssc_1 = QtWidgets.QPushButton(self.v_jsssc)
        self.btn_jsssc_1.setGeometry(QtCore.QRect(30, 10, 91, 61))
        self.btn_jsssc_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_jsssc_1.setObjectName("btn_jsssc_1")
        self.btn_jsssc_2 = QtWidgets.QPushButton(self.v_jsssc)
        self.btn_jsssc_2.setGeometry(QtCore.QRect(170, 10, 91, 61))
        self.btn_jsssc_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_jsssc_2.setObjectName("btn_jsssc_2")
        self.btn_jsssc_3 = QtWidgets.QPushButton(self.v_jsssc)
        self.btn_jsssc_3.setGeometry(QtCore.QRect(310, 10, 91, 61))
        self.btn_jsssc_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_jsssc_3.setObjectName("btn_jsssc_3")
        self.v_lmssc = QtWidgets.QWidget(self.tab_ssc)
        self.v_lmssc.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_lmssc.setFont(font)
        self.v_lmssc.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_lmssc.setObjectName("v_lmssc")
        self.btn_lmssc_1 = QtWidgets.QPushButton(self.v_lmssc)
        self.btn_lmssc_1.setGeometry(QtCore.QRect(30, 10, 91, 61))
        self.btn_lmssc_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_lmssc_1.setObjectName("btn_lmssc_1")
        self.btn_lmssc_2 = QtWidgets.QPushButton(self.v_lmssc)
        self.btn_lmssc_2.setGeometry(QtCore.QRect(170, 10, 91, 61))
        self.btn_lmssc_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_lmssc_2.setObjectName("btn_lmssc_2")
        self.btn_lmssc_3 = QtWidgets.QPushButton(self.v_lmssc)
        self.btn_lmssc_3.setGeometry(QtCore.QRect(310, 10, 91, 61))
        self.btn_lmssc_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_lmssc_3.setObjectName("btn_lmssc_3")
        self.v_txffc = QtWidgets.QWidget(self.tab_ssc)
        self.v_txffc.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_txffc.setFont(font)
        self.v_txffc.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_txffc.setObjectName("v_txffc")
        self.btn_txffc_0 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_0.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.btn_txffc_0.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_0.setObjectName("btn_txffc_0")
        self.btn_txffc_1 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_1.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.btn_txffc_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_1.setObjectName("btn_txffc_1")
        self.btn_txffc_2 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_2.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.btn_txffc_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_2.setObjectName("btn_txffc_2")
        self.btn_txffc_3 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_3.setGeometry(QtCore.QRect(330, 10, 91, 21))
        self.btn_txffc_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_3.setObjectName("btn_txffc_3")
        self.btn_txffc_4 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_4.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.btn_txffc_4.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_4.setObjectName("btn_txffc_4")
        self.btn_txffc_5 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_5.setGeometry(QtCore.QRect(110, 40, 91, 21))
        self.btn_txffc_5.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_5.setObjectName("btn_txffc_5")
        self.btn_txffc_6 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_6.setGeometry(QtCore.QRect(220, 40, 91, 21))
        self.btn_txffc_6.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_6.setObjectName("btn_txffc_6")
        self.btn_txffc_7 = QtWidgets.QPushButton(self.v_txffc)
        self.btn_txffc_7.setGeometry(QtCore.QRect(330, 40, 91, 21))
        self.btn_txffc_7.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_txffc_7.setObjectName("btn_txffc_7")
        self.v_xjssc = QtWidgets.QWidget(self.tab_ssc)
        self.v_xjssc.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_xjssc.setFont(font)
        self.v_xjssc.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_xjssc.setObjectName("v_xjssc")
        self.btn_xjssc_1 = QtWidgets.QPushButton(self.v_xjssc)
        self.btn_xjssc_1.setGeometry(QtCore.QRect(30, 10, 91, 61))
        self.btn_xjssc_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_xjssc_1.setObjectName("btn_xjssc_1")
        self.btn_xjssc_2 = QtWidgets.QPushButton(self.v_xjssc)
        self.btn_xjssc_2.setGeometry(QtCore.QRect(170, 10, 91, 61))
        self.btn_xjssc_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_xjssc_2.setObjectName("btn_xjssc_2")
        self.btn_xjssc_3 = QtWidgets.QPushButton(self.v_xjssc)
        self.btn_xjssc_3.setGeometry(QtCore.QRect(310, 10, 91, 61))
        self.btn_xjssc_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_xjssc_3.setObjectName("btn_xjssc_3")
        self.lotterys.addTab(self.tab_ssc, "")
        self.tab_pk10 = QtWidgets.QWidget()
        self.tab_pk10.setAutoFillBackground(False)
        self.tab_pk10.setStyleSheet("")
        self.tab_pk10.setObjectName("tab_pk10")
        self.btn_horse88 = QtWidgets.QPushButton(self.tab_pk10)
        self.btn_horse88.setGeometry(QtCore.QRect(100, 40, 71, 23))
        self.btn_horse88.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_horse88.setObjectName("btn_horse88")
        self.btn_bjpk10 = QtWidgets.QPushButton(self.tab_pk10)
        self.btn_bjpk10.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.btn_bjpk10.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                      "background-image: url();\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_bjpk10.setObjectName("btn_bjpk10")
        self.btn_xyft = QtWidgets.QPushButton(self.tab_pk10)
        self.btn_xyft.setGeometry(QtCore.QRect(350, 40, 71, 23))
        self.btn_xyft.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_xyft.setObjectName("btn_xyft")
        self.btn_jssc = QtWidgets.QPushButton(self.tab_pk10)
        self.btn_jssc.setGeometry(QtCore.QRect(190, 40, 71, 23))
        self.btn_jssc.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_jssc.setObjectName("btn_jssc")
        self.btn_wnsst = QtWidgets.QPushButton(self.tab_pk10)
        self.btn_wnsst.setGeometry(QtCore.QRect(270, 40, 71, 23))
        self.btn_wnsst.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_wnsst.setObjectName("btn_wnsst")
        self.lotterys.addTab(self.tab_pk10, "")
        self.tab_syxw = QtWidgets.QWidget()
        self.tab_syxw.setAutoFillBackground(False)
        self.tab_syxw.setStyleSheet("")
        self.tab_syxw.setObjectName("tab_syxw")
        self.btn_gdsyxw = QtWidgets.QPushButton(self.tab_syxw)
        self.btn_gdsyxw.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.btn_gdsyxw.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                      "background-image: url();\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_gdsyxw.setObjectName("btn_gdsyxw")
        self.v_gdsyxw = QtWidgets.QWidget(self.tab_syxw)
        self.v_gdsyxw.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_gdsyxw.setFont(font)
        self.v_gdsyxw.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border: none;")
        self.v_gdsyxw.setObjectName("v_gdsyxw")
        self.btn_gdsyxw_1 = QtWidgets.QPushButton(self.v_gdsyxw)
        self.btn_gdsyxw_1.setGeometry(QtCore.QRect(70, 10, 91, 61))
        self.btn_gdsyxw_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                        "background-image: url();\n"
                                        "color: rgb(255, 255, 255);")
        self.btn_gdsyxw_1.setObjectName("btn_gdsyxw_1")
        self.btn_gdsyxw_2 = QtWidgets.QPushButton(self.v_gdsyxw)
        self.btn_gdsyxw_2.setGeometry(QtCore.QRect(260, 10, 91, 61))
        self.btn_gdsyxw_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                        "background-image: url();\n"
                                        "color: rgb(255, 255, 255);")
        self.btn_gdsyxw_2.setObjectName("btn_gdsyxw_2")
        self.lotterys.addTab(self.tab_syxw, "")
        self.tab_klsf = QtWidgets.QWidget()
        self.tab_klsf.setAutoFillBackground(False)
        self.tab_klsf.setStyleSheet("")
        self.tab_klsf.setObjectName("tab_klsf")
        self.btn_gdklsf = QtWidgets.QPushButton(self.tab_klsf)
        self.btn_gdklsf.setGeometry(QtCore.QRect(74, 40, 111, 23))
        self.btn_gdklsf.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                      "background-image: url();\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_gdklsf.setObjectName("btn_gdklsf")
        self.btn_cqxync = QtWidgets.QPushButton(self.tab_klsf)
        self.btn_cqxync.setGeometry(QtCore.QRect(240, 40, 111, 23))
        self.btn_cqxync.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                      "background-image: url();\n"
                                      "color: rgb(255, 255, 255);")
        self.btn_cqxync.setObjectName("btn_cqxync")
        self.lotterys.addTab(self.tab_klsf, "")
        self.tab_k3 = QtWidgets.QWidget()
        self.tab_k3.setAutoFillBackground(False)
        self.tab_k3.setStyleSheet("")
        self.tab_k3.setObjectName("tab_k3")
        self.btn_jsk3 = QtWidgets.QPushButton(self.tab_k3)
        self.btn_jsk3.setGeometry(QtCore.QRect(60, 40, 75, 23))
        self.btn_jsk3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_jsk3.setObjectName("btn_jsk3")
        self.btn_hbk3 = QtWidgets.QPushButton(self.tab_k3)
        self.btn_hbk3.setGeometry(QtCore.QRect(180, 40, 75, 23))
        self.btn_hbk3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_hbk3.setObjectName("btn_hbk3")
        self.btn_jlk3 = QtWidgets.QPushButton(self.tab_k3)
        self.btn_jlk3.setGeometry(QtCore.QRect(300, 40, 75, 23))
        self.btn_jlk3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_jlk3.setObjectName("btn_jlk3")
        self.lotterys.addTab(self.tab_k3, "")
        self.tab_3d = QtWidgets.QWidget()
        self.tab_3d.setAutoFillBackground(False)
        self.tab_3d.setStyleSheet("")
        self.tab_3d.setObjectName("tab_3d")
        self.btn_pl3 = QtWidgets.QPushButton(self.tab_3d)
        self.btn_pl3.setGeometry(QtCore.QRect(240, 40, 111, 23))
        self.btn_pl3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);")
        self.btn_pl3.setObjectName("btn_pl3")
        self.btn_fc3d = QtWidgets.QPushButton(self.tab_3d)
        self.btn_fc3d.setGeometry(QtCore.QRect(74, 40, 111, 23))
        self.btn_fc3d.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                    "background-image: url();\n"
                                    "color: rgb(255, 255, 255);")
        self.btn_fc3d.setObjectName("btn_fc3d")
        self.lotterys.addTab(self.tab_3d, "")
        self.tab_kl8 = QtWidgets.QWidget()
        self.tab_kl8.setAutoFillBackground(False)
        self.tab_kl8.setStyleSheet("")
        self.tab_kl8.setObjectName("tab_kl8")
        self.btn_bjkl8 = QtWidgets.QPushButton(self.tab_kl8)
        self.btn_bjkl8.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.btn_bjkl8.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_bjkl8.setObjectName("btn_bjkl8")
        self.lotterys.addTab(self.tab_kl8, "")
        self.tab_six = QtWidgets.QWidget()
        self.tab_six.setAutoFillBackground(False)
        self.tab_six.setStyleSheet("")
        self.tab_six.setObjectName("tab_six")
        self.btn_hksix = QtWidgets.QPushButton(self.tab_six)
        self.btn_hksix.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.btn_hksix.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                     "background-image: url();\n"
                                     "color: rgb(255, 255, 255);")
        self.btn_hksix.setObjectName("btn_hksix")
        self.v_hksix = QtWidgets.QWidget(self.tab_six)
        self.v_hksix.setGeometry(QtCore.QRect(0, 30, 431, 71))
        font = QtGui.QFont()
        font.setKerning(True)
        self.v_hksix.setFont(font)
        self.v_hksix.setStyleSheet("background-color: rgba(12, 12, 12, 0);\n"
                                   "background-image: url();\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "border: none;")
        self.v_hksix.setObjectName("v_hksix")
        self.btn_hksix_1 = QtWidgets.QPushButton(self.v_hksix)
        self.btn_hksix_1.setGeometry(QtCore.QRect(30, 10, 91, 61))
        self.btn_hksix_1.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_hksix_1.setObjectName("btn_hksix_1")
        self.btn_hksix_2 = QtWidgets.QPushButton(self.v_hksix)
        self.btn_hksix_2.setGeometry(QtCore.QRect(170, 10, 91, 61))
        self.btn_hksix_2.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_hksix_2.setObjectName("btn_hksix_2")
        self.btn_hksix_3 = QtWidgets.QPushButton(self.v_hksix)
        self.btn_hksix_3.setGeometry(QtCore.QRect(310, 10, 91, 61))
        self.btn_hksix_3.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                       "background-image: url();\n"
                                       "color: rgb(255, 255, 255);")
        self.btn_hksix_3.setObjectName("btn_hksix_3")
        self.lotterys.addTab(self.tab_six, "")
        self.tb_lottery = QtWidgets.QTextBrowser(Form_bet)
        self.tb_lottery.setGeometry(QtCore.QRect(30, 210, 441, 421))
        self.tb_lottery.setStyleSheet("background-color: rgba(12, 12, 12, 80);\n"
                                      "background-image: url();\n"
                                      "color: rgb(255, 255, 255);")
        self.tb_lottery.setObjectName("tb_lottery")

        self.retranslateUi(Form_bet)
        self.lotterys.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_bet)

    def retranslateUi(self, Form_bet):
        _translate = QtCore.QCoreApplication.translate
        Form_bet.setWindowTitle(_translate("Form_bet", "AutoBet"))
        self.btn_xjssc.setText(_translate("Form_bet", "新疆時時彩"))
        self.btn_jsssc.setText(_translate("Form_bet", "極速時時彩"))
        self.btn_lmssc.setText(_translate("Form_bet", "羅馬時時彩"))
        self.btn_cqssc.setText(_translate("Form_bet", "重慶時時彩"))
        self.btn_txffc.setText(_translate("Form_bet", "騰訊分分彩"))
        self.btn_cqssc_1.setText(_translate("Form_bet", "五星\n"
                                                        "龍虎\n"
                                                        "前三\n"
                                                        "任選三"))
        self.btn_cqssc_2.setText(_translate("Form_bet", "後三\n"
                                                        "定位膽\n"
                                                        "大小單雙\n"
                                                        "不定膽"))
        self.btn_cqssc_3.setText(_translate("Form_bet", "前二\n"
                                                        "任選二\n"
                                                        "任選四\n"
                                                        "四星"))
        self.btn_jsssc_1.setText(_translate("Form_bet", "五星\n"
                                                        "龍虎\n"
                                                        "前三\n"
                                                        "任選三"))
        self.btn_jsssc_2.setText(_translate("Form_bet", "後三\n"
                                                        "定位膽\n"
                                                        "大小單雙\n"
                                                        "不定膽"))
        self.btn_jsssc_3.setText(_translate("Form_bet", "前二\n"
                                                        "任選二\n"
                                                        "任選四\n"
                                                        "四星"))
        self.btn_lmssc_1.setText(_translate("Form_bet", "五星\n"
                                                        "龍虎\n"
                                                        "前三\n"
                                                        "任選三"))
        self.btn_lmssc_2.setText(_translate("Form_bet", "後三\n"
                                                        "定位膽\n"
                                                        "大小單雙\n"
                                                        "不定膽"))
        self.btn_lmssc_3.setText(_translate("Form_bet", "前二\n"
                                                        "任選二\n"
                                                        "任選四\n"
                                                        "四星"))
        self.btn_txffc_0.setText(_translate("Form_bet", "騰訊分分彩0"))
        self.btn_txffc_1.setText(_translate("Form_bet", "騰訊分分彩1"))
        self.btn_txffc_2.setText(_translate("Form_bet", "騰訊分分彩2"))
        self.btn_txffc_3.setText(_translate("Form_bet", "騰訊分分彩3"))
        self.btn_txffc_4.setText(_translate("Form_bet", "騰訊分分彩4"))
        self.btn_txffc_5.setText(_translate("Form_bet", "騰訊分分彩5"))
        self.btn_txffc_6.setText(_translate("Form_bet", "騰訊分分彩6"))
        self.btn_txffc_7.setText(_translate("Form_bet", "騰訊分分彩7"))
        self.btn_xjssc_1.setText(_translate("Form_bet", "五星\n"
                                                        "龍虎\n"
                                                        "前三\n"
                                                        "任選三"))
        self.btn_xjssc_2.setText(_translate("Form_bet", "後三\n"
                                                        "定位膽\n"
                                                        "大小單雙\n"
                                                        "不定膽"))
        self.btn_xjssc_3.setText(_translate("Form_bet", "前二\n"
                                                        "任選二\n"
                                                        "任選四\n"
                                                        "四星"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_ssc), _translate("Form_bet", "時時彩"))
        self.btn_horse88.setText(_translate("Form_bet", "88賽馬"))
        self.btn_bjpk10.setText(_translate("Form_bet", "北京賽車"))
        self.btn_xyft.setText(_translate("Form_bet", "幸運飛艇"))
        self.btn_jssc.setText(_translate("Form_bet", "極速賽車"))
        self.btn_wnsst.setText(_translate("Form_bet", "威尼斯賽艇"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_pk10), _translate("Form_bet", "PK10"))
        self.btn_gdsyxw.setText(_translate("Form_bet", "廣東11選5"))
        self.btn_gdsyxw_1.setText(_translate("Form_bet", "三碼\n"
                                                         "二碼\n"
                                                         "定位膽\n"
                                                         "不定膽"))
        self.btn_gdsyxw_2.setText(_translate("Form_bet", "任選單式\n"
                                                         "任選單拖\n"
                                                         "任選複式"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_syxw), _translate("Form_bet", "11選5"))
        self.btn_gdklsf.setText(_translate("Form_bet", "廣東快樂十分"))
        self.btn_cqxync.setText(_translate("Form_bet", "重慶幸運農場"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_klsf), _translate("Form_bet", "快樂十分"))
        self.btn_jsk3.setText(_translate("Form_bet", "江蘇快三"))
        self.btn_hbk3.setText(_translate("Form_bet", "湖北快三"))
        self.btn_jlk3.setText(_translate("Form_bet", "吉林快三"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_k3), _translate("Form_bet", "快三"))
        self.btn_pl3.setText(_translate("Form_bet", "體彩排列三"))
        self.btn_fc3d.setText(_translate("Form_bet", "福彩3D"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_3d), _translate("Form_bet", "3D"))
        self.btn_bjkl8.setText(_translate("Form_bet", "北京快樂8"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_kl8), _translate("Form_bet", "快樂8"))
        self.btn_hksix.setText(_translate("Form_bet", "香港六合彩"))
        self.btn_hksix_1.setText(_translate("Form_bet", "特碼\n"
                                                        "正碼\n"
                                                        "正特碼\n"
                                                        "正碼1-6"))
        self.btn_hksix_2.setText(_translate("Form_bet", "連碼\n"
                                                        "半波\n"
                                                        "一肖/尾數\n"
                                                        "特肖"))
        self.btn_hksix_3.setText(_translate("Form_bet", "合肖\n"
                                                        "連肖\n"
                                                        "尾數連\n"
                                                        "全不中"))
        self.lotterys.setTabText(self.lotterys.indexOf(self.tab_six), _translate("Form_bet", "六合彩"))
        self.tb_lottery.setHtml(_translate("Form_bet",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


import src.ui.style_rc
