# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import QLocale, QTranslator
from PyQt5.QtWidgets import QApplication
from bibEditor import BibEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    if len(sys.argv) == 1:
        local = QLocale()
        translator.load(local, "biblioapp", ".")
    else:
        translator.load("biblioapp." + sys.argv[1])
    app.installTranslator(translator)
    bib = BibEditor()
    bib.show()
    sys.exit(app.exec_())
