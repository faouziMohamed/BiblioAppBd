# -*- coding : utf-8 -*-

from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex, QVariant
from collections import namedtuple


Book = namedtuple('Book', 'title author editor kind year resume price')


class ModelTableBib(QAbstractTableModel):
    def __init__(self, books):
        super(ModelTableBib, self).__init()
        self.columnsTitles = ('title', 'Author', 'Editor')
        self.book = books

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.columnsTitles[section]
        return QVariant()

    def columnCount(self, parent):
        return len(self.columnsTitles)

    def rowCount(self, parent):
        return len(self.books)

    def data(self, index, role):
        if role == Qt.DisplayRole and index.isValid():
            return (self.books[index.row()][index.column()])
        return QVariant()
