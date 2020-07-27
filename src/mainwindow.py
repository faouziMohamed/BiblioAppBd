# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(372, 463)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(475, 568))
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("QPushButton{background-color:#f5d555;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(self.groupBox)
        self.titleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.authorLabel = QtWidgets.QLabel(self.groupBox)
        self.authorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.kindLabel = QtWidgets.QLabel(self.groupBox)
        self.kindLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kindLabel.setObjectName("kindLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.kindLabel)
        self.kindFieldHLayout = QtWidgets.QHBoxLayout()
        self.kindFieldHLayout.setObjectName("kindFieldHLayout")
        self.kindComboBox = QtWidgets.QComboBox(self.groupBox)
        self.kindComboBox.setObjectName("kindComboBox")
        self.kindFieldHLayout.addWidget(self.kindComboBox)
        spacerItem = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.kindFieldHLayout.addItem(spacerItem)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.kindFieldHLayout)
        self.editorLabel = QtWidgets.QLabel(self.groupBox)
        self.editorLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.editorLabel.setObjectName("editorLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.editorLabel)
        self.editorLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.editorLineEdit.setObjectName("editorLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.editorLineEdit)
        self.yearLabel = QtWidgets.QLabel(self.groupBox)
        self.yearLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearFieldHLayout = QtWidgets.QHBoxLayout()
        self.yearFieldHLayout.setObjectName("yearFieldHLayout")
        self.yearDateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.yearDateEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.yearDateEdit.setSpecialValueText("")
        self.yearDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 2, 1), QtCore.QTime(0, 0, 0)))
        self.yearDateEdit.setCalendarPopup(True)
        self.yearDateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.yearDateEdit.setObjectName("yearDateEdit")
        self.yearFieldHLayout.addWidget(self.yearDateEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.yearFieldHLayout.addItem(spacerItem1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.yearFieldHLayout)
        self.resumLabel = QtWidgets.QLabel(self.groupBox)
        self.resumLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resumLabel.setObjectName("resumLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.resumLabel)
        self.resumTextEdit = QtWidgets.QTextEdit(self.groupBox)
        self.resumTextEdit.setObjectName("resumTextEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.resumTextEdit)
        self.priceLabel = QtWidgets.QLabel(self.groupBox)
        self.priceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.priceFieldHLayout = QtWidgets.QHBoxLayout()
        self.priceFieldHLayout.setObjectName("priceFieldHLayout")
        self.priceDSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.priceDSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.priceDSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.priceDSpinBox.setMinimum(0.0)
        self.priceDSpinBox.setMaximum(999999.0)
        self.priceDSpinBox.setObjectName("priceDSpinBox")
        self.priceFieldHLayout.addWidget(self.priceDSpinBox)
        spacerItem2 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.priceFieldHLayout.addItem(spacerItem2)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.priceFieldHLayout)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.btnHLayout = QtWidgets.QHBoxLayout()
        self.btnHLayout.setObjectName("btnHLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem3)
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setObjectName("newButton")
        self.btnHLayout.addWidget(self.newButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem4)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.btnHLayout.addWidget(self.saveButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem5)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.btnHLayout.addWidget(self.removeButton)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btnHLayout.addItem(spacerItem6)
        self.gridLayout.addLayout(self.btnHLayout, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 18))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.openAction = QtWidgets.QAction(MainWindow)
        self.openAction.setObjectName("openAction")
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.closeAction = QtWidgets.QAction(MainWindow)
        self.closeAction.setObjectName("closeAction")
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.closeAction)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BiblioApp"))
        self.groupBox.setTitle(_translate("MainWindow", "Details"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.authorLabel.setText(_translate("MainWindow", "Authors"))
        self.kindLabel.setText(_translate("MainWindow", "Kind"))
        self.editorLabel.setText(_translate("MainWindow", "Editor"))
        self.yearLabel.setText(_translate("MainWindow", "Publication year"))
        self.yearDateEdit.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.resumLabel.setText(_translate("MainWindow", "Resume"))
        self.priceLabel.setText(_translate("MainWindow", "Price"))
        self.priceDSpinBox.setSuffix(_translate("MainWindow", "$", "0"))
        self.newButton.setText(_translate("MainWindow", "&New"))
        self.saveButton.setText(_translate("MainWindow", "&Save"))
        self.removeButton.setText(_translate("MainWindow", "&Remove"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.openAction.setText(_translate("MainWindow", "&Open"))
        self.openAction.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.saveAction.setText(_translate("MainWindow", "&Save"))
        self.saveAction.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.closeAction.setText(_translate("MainWindow", "&Close"))
        self.closeAction.setShortcut(_translate("MainWindow", "Ctrl+Q"))
