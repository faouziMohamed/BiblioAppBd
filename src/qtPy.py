# -*- coding: utf-8 -*-
import sys

if 'PyQt5' in sys.modules :
    # PyQt5
    from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QMessageBox,
                                 QApplication)
    from PyQt5.QtCore import (QMetaObject, QTranslator, pyqtSignal as Signal,
                              pyqtSlot as Slot)
    from PyQt5 import QtCore, QtGui, QtWidgets
else:
    # PySide2
    from PySide2.QtWidgets import (QMainWindow, QFileDialog, QMessageBox,
                                   QApplication)
    from PySide2.QtCore import (QMetaObject, QTranslator,Signal, Slot)
    from PySide2 import QtCore, QtGui, QtWidgets


# for 'mainwindow.py' script use the import
# from qtPy import QtCore, QtGui, QtWidgets
