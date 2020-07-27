# -*- coding : utf-8 -*-
import json
from PyQt5.QtCore import (QModelIndex, Qt, QAbstractTableModel,
                          QVariant)
from collections import namedtuple

Book = namedtuple('Book', 'title author editor kind year resume price')


class ModelTableBib(QAbstractTableModel):
    def __init__(self, books: list):
        super(ModelTableBib, self).__init__()
        self.columnsTitles = ('Title', 'Author', 'Editor')
        self.books = books

    def headerData(self, section, orientation, role):
        if (role == Qt.DisplayRole) and (orientation == Qt.Horizontal):
            return self.columnsTitles[section]
        return QVariant()

    def columnCount(self, parent):
        return len(self.columnsTitles)

    def rowCount(self, parent):
        return len(self.books)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.isValid():
            return self.books[index.row()][index.column()]
        return QVariant()

    def saveInFile(self, file_name: str):
        with open(file_name, 'w') as f:
            json.dump(self.books, f)

    @staticmethod
    def createFromFile(file_name: str):
        with open(file_name, 'r') as f:
            file_content = f.read()
        books_attributes = json.loads(file_content)
        books = [Book(*attributes) for attributes in books_attributes]
        return ModelTableBib(books)

    def addBook(self, book: Book):
        indexBook = len(self.books)
        self.beginInsertRows(QModelIndex(), indexBook, indexBook)
        self.books.append(book)
        self.endInsertRows()

    def deleteBook(self, index_book: int):
        self.beginRemoveRows(QModelIndex(), index_book, index_book)
        del self.books[index_book]
        self.endRemoveRows()

    def replaceBook(self, index_book: int, book: Book):
        self.books[index_book] = book
        self.dataChanged.emit(self.createIndex(index_book, 0),
                              self.createIndex(index_book, 2))
