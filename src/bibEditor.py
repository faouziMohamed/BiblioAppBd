from mainwindow import Ui_MainWindow
from modelTableBib import Book, ModelTableBib
from PyQt5.QtCore import (pyqtSlot as Slot, QDate, QItemSelection,
                          QItemSelectionModel, QTranslator)
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QMessageBox)


class BibEditor(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(BibEditor, self).__init__(parent)
        self.setupUi(self)
        self.unsaved_file = False
        self.library = ModelTableBib()
        self.genreComboBox.addItems(self.library.genres())

        self.treeView.setModel(self.library)
        self.initialize_fields()
        self.clearDetailsFields()
        self.initialize_event_connection()

    def initialize_fields(self):
        self.yearDateEdit.setMinimumDate(QDate(1000, 1, 1))
        self.priceDSpinBox.setSpecialValueText(" ")
        self.yearDateEdit.setSpecialValueText(" ")
        self.removeButton.setEnabled(False)
        self.saveButton.setEnabled(False)

    def clearDetailsFields(self):
        for text_field in (self.titleLineEdit, self.authorLineEdit,
                           self.editorLineEdit, self.summaryTextEdit):
            text_field.setText("")
        self.genreComboBox.setCurrentIndex(0)
        self.yearDateEdit.setDate(self.yearDateEdit.minimumDate())
        self.priceDSpinBox.setValue(self.priceDSpinBox.minimum())

    def initialize_event_connection(self):
        for fields in (self.titleLineEdit, self.authorLineEdit,
                       self.editorLineEdit):
            fields.textEdited.connect(self.input_in_progress)

        self.genreComboBox.currentIndexChanged.connect(self.input_in_progress)
        self.yearDateEdit.dateChanged.connect(self.input_in_progress)
        self.summaryTextEdit.textChanged.connect(self.input_in_progress)
        self.priceDSpinBox.valueChanged.connect(self.input_in_progress)
        self.treeView.selectionModel().selectionChanged \
            .connect(self.on_treeview_selectionChanged)

    def input_in_progress(self):
        self.newButton.setEnabled(False)
        correct_input = len(self.titleLineEdit.text().strip()) > 0
        self.saveButton.setEnabled(correct_input)

    def on_treeview_selectionChanged(self, selected: QItemSelection,
                                     deselected: QItemSelection):
        selectedIndex = selected.indexes()
        abandon, no = self.askIf_WantAbandon_CurrentEntry(selected, deselected)
        if abandon == no:
            return
        if len(selectedIndex) == 0:
            self.clearDetailsFields()
            self.removeButton.setEnabled(False)
        else:
            index_of_selectedBook = selectedIndex[0].row()
            self.displayBookDetails(self.library.books[index_of_selectedBook])
            self.removeButton.setEnabled(True)
            self.newButton.setEnabled(True)
        self.saveButton.setEnabled(False)

    def askIf_WantAbandon_CurrentEntry(self, selected, deselected):
        yes, no = QMessageBox.Yes, QMessageBox.No
        question, answer = QMessageBox.question, yes
        msg_title = self.tr("Confirmation")
        msg = self.tr("Abandon the unsaved entry ?")
        if self.saveButton.isEnabled():
            answer = question(self, msg_title, msg, yes, no)
        if answer == no:
            QIS = QItemSelectionModel
            selection_model = self.treeView.selectionModel()
            selection_model.selectionChanged \
                .disconnect(self.on_treeview_selectionChanged)
            selection_model.select(selected, QIS.Deselect)
            selection_model.select(deselected, QIS.Select)
            selection_model.selectionChanged \
                .connect(self.on_treeview_selectionChanged)
        return answer, no

    def displayBookDetails(self, book):
        self.titleLineEdit.setText(book.title)
        self.authorLineEdit.setText(book.author)
        self.genreComboBox.setCurrentText(book.genre)
        self.editorLineEdit.setText(book.editor)
        self.yearDateEdit.setDate(QDate(book.year, 1, 1))
        self.summaryTextEdit.setPlainText(book.summary)
        self.priceDSpinBox.setValue(book.price)

    @Slot()
    def on_newButton_clicked(self):
        self.treeView.selectionModel().clearSelection()
        self.clearDetailsFields()
        self.saveButton.setEnabled(False)


    @Slot()
    def on_saveButton_clicked(self):
        book = Book(idBook=None,
                    title=self.titleLineEdit.text(),
                    author=self.authorLineEdit.text(),
                    editor=self.editorLineEdit.text(),
                    genre=self.genreComboBox.currentText(),
                    year=self.yearDateEdit.date().year(),
                    summary=self.summaryTextEdit.toPlainText(),
                    price=self.priceDSpinBox.value())

        currentSelection = self.treeView.selectionModel()
        columns_of_selected_book = currentSelection.selectedRows()

        if len(columns_of_selected_book) == 0:
            self.library.addBook(book)
            self.on_newButton_clicked()
        else:
            selected_book = columns_of_selected_book[0].row()
            self.library.replaceBook(selected_book, book)
        self.saveButton.setEnabled(False)
        self.newButton.setEnabled(True)

    @Slot()
    def on_removeButton_clicked(self):
        currentSelection = self.treeView.selectionModel()
        columns_of_selected_book = currentSelection.selectedRows()
        if len(columns_of_selected_book) > 0:
            selected_book = columns_of_selected_book[0].row()
            self.library.deleteBook(selected_book)

    @Slot()
    def on_closeAction_triggered(self):
        self.close()
