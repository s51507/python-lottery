# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class LogStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))
