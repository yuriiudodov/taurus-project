import sqlite3

import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self,dbDir,parent=None):
        QtCore.QabstractTableModel.__init__(self,parent)
        dbConnection = sqlite3.connect("../MainDatabaseVet", isolation_level=None)
        cursor=dbConnection.cursor()
        dbConnection.execute("""SELECT * FROM city""")
        data=cursor.fetchall()
        data =[[]]
        count1=0
        for i in data:
            count2 = 0
        for x in i:
            data[count1][count2] =x
            count2 +=1

        self.__data=data
        self.__header=[" First "," Second "," Thirdt " ]

    def rowCount( self, parent ):
        return len(self.__data)

    def columnCount( self , parent ):
        return len(self.__data[0])

    def flags( self,index):
        return QtCore.Qt.ItemIsEnabled |QtCore.Qt.ItemIsSelectable

    def data ( self , index , role ):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__data[row][column]
            return value.name()

    def headerData(self , section , orientation , role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__header[section]

class Table(QDialog):
 def __init__(self, parent=None):
    super(Table, self).__init__(parent)
    layout = PySide6.QtWidgets.QGridLayout()
    self.MyTableMModel = MyTableModel("MainDatabaseVet") # pass directory in which table exists
    self.table = PySide6.QtWidgets.QTableView()
    self.table.setModel(self.MyTableModel)
    layout.addWidget(self.table)
    self.setLayout(layout)