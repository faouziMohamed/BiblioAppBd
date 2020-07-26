# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QMetaObject, QTranslator
from mainwindow import Ui_MainWindow


class bibEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(bibEditor, self).__init__(parent)
        self.setupUi(self)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_openAction_triggered(self):
        tr = QTranslator.tr
        gtOpFName = QFileDialog.getOpenFileName
        (fileName, filter) = gtOpFName(
                                None, tr(self, "Open a library file"),
                                filter=tr(self, "Library(*.bib);; all(*.*)"))
        if fileName:
            # TODO : will replace a code here
            QMessageBox.information(
                self, tr(self, "Trace"), tr(self, "File to open on :\n") +
                fileName)
