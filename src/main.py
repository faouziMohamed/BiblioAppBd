# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from bibEditor import BibEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bib = BibEditor()
    bib.show()
    sys.exit(app.exec_())
