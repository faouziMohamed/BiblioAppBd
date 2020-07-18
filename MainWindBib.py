from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QMainWindow, \
                      QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QMetaObject, pyqtSlot


class MainWindBib(QMainWindow):
    def __init__(self):
        super(MainWindBib, self).__init__()
        QMetaObject.connectSlotsByName(self)
        self.__configureTheWindow()
        self.__createWindowContent()
        self.__addContaintToTheWindow()
        self.__setUpWindowEvents()

    def __configureTheWindow(self):
        self.setWindowTitle("BiblioApp")
        self.resize(300, 150)

    def __createWindowContent(self):
        self.centralWidget = QWidget(self)
        self.mainVbox = QVBoxLayout(self.centralWidget)
        self.textLayout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.label = QLabel("Titre", self.centralWidget)
        self.labelField = QLineEdit(self.centralWidget)
        self.buttonOk = QPushButton("OK", self.centralWidget)

        self.textLayout.addWidget(self.label)
        self.textLayout.addWidget(self.labelField)

        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(self.buttonOk)
        self.buttonLayout.addStretch()

        self.mainVbox.addLayout(self.textLayout)
        self.mainVbox.addStretch()
        self.mainVbox.addLayout(self.buttonLayout)

    def __addContaintToTheWindow(self):
        self.centralWidget.setLayout(self.mainVbox)
        self.setCentralWidget(self.centralWidget)

    def __setUpWindowEvents(self):
        self.buttonOk.clicked.connect(self.on_buttonOk_clicked)

    @pyqtSlot()
    def on_buttonOk_clicked(self):
        QMessageBox.information(self, "Info", "Title : " +
                                self.labelField.text())
