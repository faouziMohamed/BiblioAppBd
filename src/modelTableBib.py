# -*- coding : utf-8 -*-
import os
from PyQt5.QtCore import (qDebug, QModelIndex, Qt, QAbstractTableModel,
                          QVariant)
from collections import namedtuple, OrderedDict

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

Book = namedtuple("Book", ("idBook", "title", "author", "editor",
                           "genre", "year", "summary", "price"))

DB_PATH = "../assets/db/"
DB_FILE = "library.sqlite"
DB_FILE_NAME = DB_PATH+DB_FILE


class ModelTableBib(QAbstractTableModel):
    def __init__(self):
        super(ModelTableBib, self).__init__()

        self.columnsTitles = (self.tr("Title"), self.tr("Author"),
                              self.tr("Editor"), self.tr("Genre"))
        self.books = []
        self.id_by_genre = None

        bdExists = os.path.exists(DB_FILE_NAME)
        bd = QSqlDatabase.addDatabase('QSQLITE')
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
        QSqlQuery(''' INSERT INTO genres (genre)
                VALUES ("---"), ("Biography"), ("Fantastic"), ("Historical"), 
                ("Detective"), ("Science-Fiction")''')

    def readDB(self):
        query = QSqlQuery('''SELECT genre_id, genre 
                             FROM genres 
                             ORDER BY genre_id''')
        self.id_by_genre = OrderedDict()
        while query.next():
            self.id_by_genre[query.value(1)] = query.value(0)
            # print(query.value(1))
        query = QSqlQuery(''' SELECT book_id, title, author, publisher,
                                     genre, year, summary, price
                              FROM books
                              JOIN genres ON 
                               genres.genre_id = books.genre_id ''')
        self.books = []
        while query.next():
            book = Book(*(query.value(i) for i in range(8)))
            self.books.append(book)

    def genres(self):
        return self.id_by_genre.keys()

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
            return self.books[index.row()][index.column() + 1]
        return QVariant()

    def addBook(self, book: Book):
        query = QSqlQuery()
        query.prepare(''' 
        INSERT INTO books (book_id,   title,    author, 
                           publisher, genre_id, year, 
                           summary,   price)
        VALUES (NULL,:title,:author, :editor,:idGenre, :year, :summary, :price)
        ''')

        query.bindValue(":title",   book.title)
        query.bindValue(":author",  book.author)
        query.bindValue(":editor",  book.editor)
        query.bindValue(":idGenre", self.id_by_genre[book.genre])
        query.bindValue(":year",    book.year)
        query.bindValue(":summary", book.summary)
        query.bindValue(":price",   book.price)
        query.exec_()
        qDebug(query.lastError().text())

        id_book = query.lastInsertId()
        book = Book(id_book, *book[1:])

        indexBook = len(self.books)
        self.beginInsertRows(QModelIndex(), indexBook, indexBook)
        self.books.append(book)
        self.endInsertRows()

    def deleteBook(self, index_book: int):
        query = QSqlQuery()
        query.prepare(''' DELETE FROM books WHERE book_id = :id_book ''')
        query.bindValue(":id_book", self.books[index_book].idBook)
        query.exec_()

        self.beginRemoveRows(QModelIndex(), index_book, index_book)
        del self.books[index_book]
        self.endRemoveRows()

    def replaceBook(self, index_book: int, book: Book):
        query = QSqlQuery()
        query.prepare(''' UPDATE books
                    SET title     = :title,
                        author    = :author,
                        publisher = :editor,
                        genre_id  = :idGenre,
                        year      = :year,
                        summary   = :summary,
                        price     = :price 
                    WHERE book_id = :idBook ''')
        query.bindValue(":idBook",  self.books[index_book].idBook)
        query.bindValue(":title",   book.title)
        query.bindValue(":author",  book.author)
        query.bindValue(":editor",  book.editor)
        query.bindValue(":idGenre", self.id_by_genre[book.genre])
        query.bindValue(":year",    book.year)
        query.bindValue(":summary", book.summary)
        query.bindValue(":price",   book.price)
        query.exec_()

        self.books[index_book] = book
        self.dataChanged.emit(self.createIndex(index_book, 0),
                              self.createIndex(index_book, 2))
