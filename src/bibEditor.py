from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QMessageBox,
                             QApplication)
from PyQt5.QtCore import (QMetaObject, QTranslator, pyqtSignal as Signal,
                          pyqtSlot as Slot)
from mainwindow import Ui_MainWindow
from modelTableBib import ModelTableBib, Book


class bibEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(bibEditor, self).__init__(parent)
        self.setupUi(self)
        book_1 = Book(
            "Une étude en rouge", "Conan Doyle", "Hachette", "Policier",
                      1888, "...", 13.)
        book_2 = Book(
            "Le Horla", "Guy de Maupassant", "Gallimard", "Fantastique",
                      1887, "...", 11.)
        book_3 = Book(
            "Napoléon", "André Castelot", "Perrin", "Biographie",
                      2008, "...", 24.)
        books = [book_1, book_2, book_3]


    @Slot()
    def on_openAction_triggered(self):
        tr = QTranslator.tr
        opFname = QFileDialog.getOpenFileName
        title = tr(self, "Open a library file")
        filter = tr(self, "Library(*.bib); all(*.*)")
        (fileName, filter) = opFname(None, title, filter=filter)

        if fileName:
            # TODO : will replace a code here
            title = tr(self, "Trace")
            open = tr(self, "File to open on")+" :\n" + fileName
            QMessageBox.information(self, title, open)

    @Slot()
    def on_closeAction_triggered(self):
        self.close()

    def closeEvent(self, event):
        tr = QTranslator.tr
        confirmMsg = tr(self,"Are you sure you want to exit BiblioApp");
        question = QMessageBox.question
        yes, no = QMessageBox.Yes, QMessageBox.No
        ans = question(self,"Confirm exit",confirmMsg,yes,no)

        if ans == yes :
            event.accept()
        else :
            event.ignore()



