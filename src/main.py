# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtCore import QLocale, QTranslator
from PyQt5.QtWidgets import QApplication
from bibEditor import BibEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    enNativeLang = len(sys.argv) == 1

    if enNativeLang:
        local = QLocale()
    else:
        langCountry = sys.argv[1]

    translators = []
    lang_path = "../assets/lang/"
    for prefixQm in ("biblioapp.", "qt_", "qtbase_"):
        translator = QTranslator()
        translators.append(translator)

        if enNativeLang:
            translator.load(local, lang_path+prefixQm)
        else:
            translator.load(lang_path+prefixQm + langCountry)
        app.installTranslator(translator)

    bib = BibEditor()
    bib.show()
    sys.exit(app.exec_())


