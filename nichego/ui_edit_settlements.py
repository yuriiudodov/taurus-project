# -*- coding: utf-8 -*-
import pandas as pd
from IPython.display import display
################################################################################
## Form generated from reading UI file 'edit_settlements.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
from sqlalchemy import create_engine, text

import ui_dialog_open


class Ui_Dialog(object):

    def write_settlement_to_db(self, item_pk, text_to_write): #Должна редачить имя выбранного в тейблвиджете населенного пункта
        print(item_pk.text(), " ",text_to_write.text())
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
        UPDATE settlement SET name = :name WHERE pk = :pk
        """)
        VetTableQuery.bindValue(":name", text_to_write.text())
        VetTableQuery.bindValue(":pk", item_pk.text())
        VetTableQuery.exec()
        VetDbConnnection.close()
        #refresh table
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def add_settlement_to_db(self, text_to_write): #Должна редачить имя выбранного в тейблвиджете населенного пункта

        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
        INSERT INTO settlement (name) VALUES (:name)
        """)
        VetTableQuery.bindValue(":name", text_to_write.text())

        VetTableQuery.exec()
        VetDbConnnection.close()
        #refresh table
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def delete_settlement_to_db(self, item_pk):
        print(item_pk.text(), " ")
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
               DELETE FROM settlement WHERE pk = :pk
               """)

        VetTableQuery.bindValue(":pk", item_pk.text())
        VetTableQuery.exec()
        VetDbConnnection.close()
        # refresh table
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(670, 627)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 91, 16))
        self.settlementTableWidget = QTableWidget(Dialog)
        self.settlementTableWidget.setObjectName(u"settlementTableWidget")
        self.settlementTableWidget.setGeometry(QRect(30, 40, 211, 201))
        self.settlementLineEdit = QLineEdit(Dialog)
        self.settlementLineEdit.setObjectName(u"settlementLineEdit")
        self.settlementLineEdit.setGeometry(QRect(12, 270, 201, 21))
        self.pushButtonSaveSettlement = QPushButton(Dialog, clicked=lambda: self.write_settlement_to_db(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0),self.settlementLineEdit))
        self.pushButtonSaveSettlement.setObjectName(u"pushButton")
        self.pushButtonSaveSettlement.setGeometry(QRect(230, 270, 75, 24))
        self.pushButtonDeleteSettlement = QPushButton(Dialog, clicked=lambda: self.delete_settlement_to_db(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0)))
        self.pushButtonDeleteSettlement.setObjectName(u"pushButton_2")
        self.pushButtonDeleteSettlement.setGeometry(QRect(410, 350, 111, 41))
        self.pushButtonAddSettlement = QPushButton(Dialog, clicked=lambda: self.add_settlement_to_db(self.settlementLineEdit))
        self.pushButtonAddSettlement.setObjectName(u"pushButton_3")
        self.pushButtonAddSettlement.setGeometry(QRect(480, 420, 181, 111))
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(410, 300, 161, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 250, 151, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        #-----------------------------------------------------------------------------------

        DB_PATH = settings.DB_PATH  # vremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'),vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num, QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    # setupUi

        #self.settlementTableWidget.itemClicked.connect(lambda:self.settlementLineEdit.setText(text(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),2))))

        #Yura connects for the UI
        self.settlementTableWidget.itemClicked.connect(lambda: self.settlementLineEdit.setText(
            self.settlementTableWidget.item(self.settlementTableWidget.currentRow(), 1).text()))




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButtonAddSettlement.setText("ADD")
        self.label.setText(QCoreApplication.translate("Dialog", u"Settlements", None))
        self.pushButtonSaveSettlement.setText(QCoreApplication.translate("Dialog", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonDeleteSettlement.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u0435 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
    # retranslateUi

