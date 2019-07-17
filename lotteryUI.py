import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtCore import QTimer, Qt
from src.ui.login import Ui_Form_login as F_login
from src.ui.bet import Ui_Form_bet as F_bet
from src.ui.check import Ui_Form_check as F_check
from src.lottertBet import login
from src.lotteryGame import *
from src.ui.log import LogStream as ls
import threading


class LoginWindow(QDialog, F_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFocus()
        self.lb_login.hide()
        self.btn_login.clicked.connect(self.sayGoodBye)

    def sayGoodBye(self):
        loading = QMovie(":/loading/01.gif")
        self.lb_login.setMovie(loading)
        loading.start()
        self.lb_login.show()
        self.input_user.hide()
        self.input_pwd.hide()
        threading.Thread(target=login, args=(self.input_user.text(), self.input_pwd.text(),)).start()
        threading.Timer(3.0, self.close).start()


class CheckWindow(QDialog, F_check):
    def __init__(self, parent=None):
        super(CheckWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFocus()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        shadow = QGraphicsDropShadowEffect(blurRadius=100, xOffset=0, yOffset=0)
        self.bg.setGraphicsEffect(shadow)
        self.btn_fixnum.clicked.connect(self.fixNum)
        self.btn_rannum.clicked.connect(self.ranNum)
        self.btn_cancel.clicked.connect(self.close)
        nowGame = ''

    def fixNum(self):
        w_bet.bet(self.nowGame)
        self.close()

    def ranNum(self):
        print(self.nowGame + '機選尚未完成  _(¦3」∠)_')
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class BetWindow(QDialog, F_bet):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resetAll()
        sys.stdout = ls(textWritten=self.showLog)
        sys.stderr = ls(textWritten=self.showLog)

        # 時時彩
        self.btn_cqssc.clicked.connect(lambda: self.vShow('cqssc'))
        self.btn_jsssc.clicked.connect(lambda: self.vShow('jsssc'))
        self.btn_lmssc.clicked.connect(lambda: self.vShow('lmssc'))
        self.btn_txffc.clicked.connect(lambda: self.vShow('txffc'))
        self.btn_xjssc.clicked.connect(lambda: self.vShow('xjssc'))

        self.btn_cqssc_1.clicked.connect(lambda: self.check('cqssc_1'))
        self.btn_cqssc_2.clicked.connect(lambda: self.check('cqssc_2'))
        self.btn_cqssc_3.clicked.connect(lambda: self.check('cqssc_3'))

        self.btn_jsssc_1.clicked.connect(lambda: self.check('jsssc_1'))
        self.btn_jsssc_2.clicked.connect(lambda: self.check('jsssc_2'))
        self.btn_jsssc_3.clicked.connect(lambda: self.check('jsssc_3'))

        self.btn_lmssc_1.clicked.connect(lambda: self.check('lmssc_1'))
        self.btn_lmssc_2.clicked.connect(lambda: self.check('lmssc_2'))
        self.btn_lmssc_3.clicked.connect(lambda: self.check('lmssc_3'))

        self.btn_txffc_0.clicked.connect(lambda: self.check('txffc_0'))
        self.btn_txffc_1.clicked.connect(lambda: self.check('txffc_1'))
        self.btn_txffc_2.clicked.connect(lambda: self.check('txffc_2'))
        self.btn_txffc_3.clicked.connect(lambda: self.check('txffc_3'))
        self.btn_txffc_4.clicked.connect(lambda: self.check('txffc_4'))
        self.btn_txffc_5.clicked.connect(lambda: self.check('txffc_5'))
        self.btn_txffc_6.clicked.connect(lambda: self.check('txffc_6'))
        self.btn_txffc_7.clicked.connect(lambda: self.check('txffc_7'))

        self.btn_xjssc_1.clicked.connect(lambda: self.check('xjssc_1'))
        self.btn_xjssc_2.clicked.connect(lambda: self.check('xjssc_2'))
        self.btn_xjssc_3.clicked.connect(lambda: self.check('xjssc_3'))

        # PK10
        self.btn_bjpk10.clicked.connect(lambda: self.check('bjpk10'))
        self.btn_horse88.clicked.connect(lambda: self.check('horse88'))
        self.btn_jssc.clicked.connect(lambda: self.check('jssc'))
        self.btn_wnsst.clicked.connect(lambda: self.check('wnsst'))
        self.btn_xyft.clicked.connect(lambda: self.check('xyft'))

        # 11選5
        self.btn_gdsyxw.clicked.connect(lambda: self.vShow('gdsyxw'))

        self.btn_gdsyxw_1.clicked.connect(lambda: self.check('gdsyxw_1'))
        self.btn_gdsyxw_2.clicked.connect(lambda: self.check('gdsyxw_2'))

        # 快樂十分
        self.btn_gdklsf.clicked.connect(lambda: self.check('gdklsf'))
        self.btn_cqxync.clicked.connect(lambda: self.check('cqxync'))

        # 快三
        self.btn_jsk3.clicked.connect(lambda: self.check('jsk3'))
        self.btn_hbk3.clicked.connect(lambda: self.check('hbk3'))
        self.btn_jlk3.clicked.connect(lambda: self.check('jlk3'))

        # 3D
        self.btn_fc3d.clicked.connect(lambda: self.check('fc3d'))
        self.btn_pl3.clicked.connect(lambda: self.check('pl3'))

        # 快樂8
        self.btn_bjkl8.clicked.connect(lambda: self.check('bjkl8'))

        # 六合彩
        self.btn_hksix.clicked.connect(lambda: self.vShow('hksix'))

        self.btn_hksix_1.clicked.connect(lambda: self.check('hksix_1'))
        self.btn_hksix_2.clicked.connect(lambda: self.check('hksix_2'))
        self.btn_hksix_3.clicked.connect(lambda: self.check('hksix_3'))

    def vShow(self, game):
        self.resetAll()
        if game == 'cqssc':
            self.btn_cqssc.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_cqssc.show()
        elif game == 'jsssc':
            self.btn_jsssc.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_jsssc.show()
        elif game == 'lmssc':
            self.btn_lmssc.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_lmssc.show()
        elif game == 'txffc':
            self.btn_txffc.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_txffc.show()
        elif game == 'xjssc':
            self.btn_xjssc.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_xjssc.show()
        elif game == 'gdsyxw':
            self.btn_gdsyxw.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_gdsyxw.show()
        elif game == 'hksix':
            self.btn_hksix.setStyleSheet(
                'background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\ncolor: rgb(255, 255, 12)')
            self.v_hksix.show()

    def check(self, game):
        w_check.nowGame = game
        w_check.show()

    def bet(self, game):
        tBet = threading.Thread(target=self.betting, args=(game,))
        tBet.start()

    def betting(self, game):
        if game == 'cqssc_1':
            cqssc('1')
        elif game == 'cqssc_2':
            cqssc('2')
        elif game == 'cqssc_3':
            cqssc('3')
        elif game == 'jsssc_1':
            jsssc('1')
        elif game == 'jsssc_2':
            jsssc('2')
        elif game == 'jsssc_3':
            jsssc('3')
        elif game == 'lmssc_1':
            lmssc('1')
        elif game == 'lmssc_2':
            lmssc('2')
        elif game == 'lmssc_3':
            lmssc('3')
        elif game == 'txffc_0':
            txffc('0')
        elif game == 'txffc_1':
            txffc('1')
        elif game == 'txffc_2':
            txffc('2')
        elif game == 'txffc_3':
            txffc('3')
        elif game == 'txffc_4':
            txffc('4')
        elif game == 'txffc_5':
            txffc('5')
        elif game == 'txffc_6':
            txffc('6')
        elif game == 'txffc_7':
            txffc('7')
        elif game == 'xjssc_1':
            xjssc('1')
        elif game == 'xjssc_2':
            xjssc('2')
        elif game == 'xjssc_3':
            xjssc('3')
        elif game == 'bjpk10':
            bjpk10()
        elif game == 'horse88':
            horse88()
        elif game == 'jssc':
            jssc()
        elif game == 'wnsst':
            wnsst()
        elif game == 'xyft':
            xyft()
        elif game == 'gdsyxw_1':
            gdsyxw('1')
        elif game == 'gdsyxw_2':
            gdsyxw('2')
        elif game == 'gdklsf':
            gdklsf()
        elif game == 'cqxync':
            cqxync()
        elif game == 'jsk3':
            jsk3()
        elif game == 'hbk3':
            hbk3()
        elif game == 'jlk3':
            jlk3()
        elif game == 'fc3d':
            fc3d()
        elif game == 'pl3':
            pl3()
        elif game == 'bjkl8':
            bjkl8()
        elif game == 'hksix_1':
            hksix('1')
        elif game == 'hksix_2':
            hksix('2')
        elif game == 'hksix_3':
            hksix('3')

    def resetAll(self):
        # ScrollBar
        self.tb_lottery.verticalScrollBar().setStyleSheet(
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: rgba(12, 12, 12, 80);}\n"
            "QScrollBar::handle:vertical{background: rgba(120, 120, 120, 80); border-radius:8px;}\n"
            "QScrollBar::handle:vertical:hover{background: rgba(150, 150, 150, 80); border-radius:8px;}\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {border:none;}\n"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {border:none;}")
        # 時時彩
        self.v_cqssc.hide()
        self.v_jsssc.hide()
        self.v_lmssc.hide()
        self.v_txffc.hide()
        self.v_xjssc.hide()

        self.btn_cqssc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_cqssc_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_cqssc_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_cqssc_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        self.btn_jsssc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_jsssc_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_jsssc_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_jsssc_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        self.btn_lmssc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_lmssc_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_lmssc_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_lmssc_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        self.btn_txffc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_0.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_4.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_5.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_6.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_txffc_7.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        self.btn_xjssc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_xjssc_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_xjssc_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_xjssc_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # PK10
        self.btn_bjpk10.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_horse88.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_jssc.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_wnsst.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_xyft.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 11選5
        self.v_gdsyxw.hide()
        self.btn_gdsyxw.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_gdsyxw_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_gdsyxw_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 快樂十分
        self.btn_gdklsf.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_cqxync.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 快三
        self.btn_jsk3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_hbk3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_jlk3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 3D
        self.btn_fc3d.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_pl3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 快樂8
        self.btn_bjkl8.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

        # 六合彩
        self.v_hksix.hide()
        self.btn_hksix.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_hksix_1.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_hksix_2.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')
        self.btn_hksix_3.setStyleSheet('background-color: rgba(12, 12, 12, 80);\nbackground-image: url();\n')

    def showLog(self, msg):
        self.tb_lottery.append(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w_login = LoginWindow()
    w_bet = BetWindow()
    w_check = CheckWindow()
    timer = QTimer()


    def wBetShow():
        timer.stop()
        w_bet.show()


    w_login.show()
    w_login.btn_login.clicked.connect(lambda: timer.start(2500))
    timer.timeout.connect(wBetShow)
    sys.exit(app.exec_())
