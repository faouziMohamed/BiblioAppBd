# -*- coding : utf-8 -*-
import os
from PyQt5.QtCore import (QModelIndex, Qt, QAbstractTableModel, QVariant)
from collections import namedtuple
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

fields = ("idBook", "title", "author", "editor", "genre", "year", "resume", "price")
Book = namedtuple("Book", fields)
DB_FILE_NAME = "library.db"


class ModelTableBib(QAbstractTableModel):
    def __init__(self, books: list):
        super(ModelTableBib, self).__init__()
        self.columnsTitles = (self.tr("Title"), self.tr("Author"),
                              self.tr("Editor"), self.tr("Genre"))
        self.books = books
        bdExists = os.path.exists(DB_FILE_NAME)
        bd = QSqlDatabase.addDatabase('QSLITE')
        bd.setDatabaseName(DB_FILE_NAME)
        bd.open()

        if not bdExists:
            self.createBD()
        self.readDB()

    def createBD(self):
        QSqlQuery(''' CREATE TABLE genres ( 
                genre_id  INTEGER PRIMARY KEY,
                genre     TEXT)''')

        QSqlQuery(''' CREATE TABLE books(
                book_id   INTEGER PRIMARY KEY,
                title     TEXT,
                author    TEXT,
                publisher TEXT,
                genre_id  INTEGER,
                year      INTEGER,
                summary   TEXT,
                price     FLOAT)''')

    def headerData(self, section: int, orientation: Qt.Orientation, role):
        if (role == Qt.DisplayRole) and (orientation == Qt.Horizontal):
            return self.tr(self.columnsTitles[section])
        return QVariant()

    def columnCount(self, parent):
        return len(self.columnsTitles)

    def rowCount(self, parent):
        return len(self.books)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.isValid():
            return self.books[index.row()][index.column()+1]
        return QVariant()

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