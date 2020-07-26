# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from bibEditor import bibEditor

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bib = bibEditor()
    bib.show()
    sys.exit(app.exec_())
