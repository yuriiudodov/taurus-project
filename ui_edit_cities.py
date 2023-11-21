# -*- coding: utf-8 -*-

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
                               QTableWidget, QTableWidgetItem, QWidget, QGridLayout)
from sqlalchemy import create_engine, text
import pandas as pd


class Ui_Dialog(object):
    def write_city_to_db(self, item_pk,
                         city_name_to_write, belongs_to_settlement):  # Должна редачить имя выбранного в тейблвиджете населенного пункта
        print(item_pk.text(), " ", city_name_to_write.text())
        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
           UPDATE city SET name = :city_name, belongs_to_settlement = :settlement WHERE pk = :pk
           """)
        VetTableQuery.bindValue(":city_name", city_name_to_write.text())
        VetTableQuery.bindValue(":settlement", belongs_to_settlement.text())
        VetTableQuery.bindValue(":pk", item_pk.text())
        VetTableQuery.exec()
        VetDbConnnection.close()
        # refresh table
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT city.pk, city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(3)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def add_settlement_to_db(self, text_to_write):  # Должна редачить имя выбранного в тейблвиджете населенного пункта

        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
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
        # refresh table
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT city.pk, city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(3)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def delete_settlement_to_db(self, item_pk):
        print(item_pk.text(), " ")
        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
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
        data_for_table = pd.read_sql(text(f'SELECT city.pk, city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(3)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(509, 340)
        icon = QIcon(QIcon.fromTheme(u"accessories-text-editor"))
        Dialog.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.settlementTableWidget = QTableWidget(Dialog)
        self.settlementTableWidget.setObjectName(u"settlementTableWidget")

        self.gridLayout.addWidget(self.settlementTableWidget, 1, 0, 1, 2)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButtonSaveSettlement = QPushButton(Dialog, clicked=lambda: self.write_settlement_to_db(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0),self.settlementLineEdit))
        self.pushButtonSaveSettlement.setObjectName(u"pushButtonSaveSettlement")

        self.gridLayout.addWidget(self.pushButtonSaveSettlement, 3, 1, 1, 1)

        self.pushButtonDeleteSettlement = QPushButton(Dialog, clicked=lambda: self.delete_settlement_to_db(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0)))
        self.pushButtonDeleteSettlement.setObjectName(u"pushButtonDeleteSettlement")

        self.gridLayout.addWidget(self.pushButtonDeleteSettlement, 5, 3, 1, 1)

        self.settlementLineEdit = QLineEdit(Dialog)
        self.settlementLineEdit.setObjectName(u"settlementLineEdit")

        self.gridLayout.addWidget(self.settlementLineEdit, 3, 0, 1, 1)

        self.pushButtonAddSettlement = QPushButton(Dialog, clicked=lambda: self.add_settlement_to_db(self.settlementLineEdit))
        self.pushButtonAddSettlement.setObjectName(u"pushButtonAddSettlement")

        self.gridLayout.addWidget(self.pushButtonAddSettlement, 3, 2, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 4, 3, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

        # -----------------------------------------------------------------------------------

        DB_PATH = 'MainDatabaseVet'  # vremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT city.pk, city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(3)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
        # setupUi

        # self.settlementTableWidget.itemClicked.connect(lambda:self.settlementLineEdit.setText(text(self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),2))))

        # Yura connects for the UI
        self.settlementTableWidget.itemClicked.connect(lambda: self.settlementLineEdit.setText(
            self.settlementTableWidget.item(self.settlementTableWidget.currentRow(), 1).text()))
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(statustip)
        Dialog.setStatusTip(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u0441\u0442\u0430\u0442\u0443\u0441\u0430 ", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        Dialog.setWhatsThis(QCoreApplication.translate("Dialog", u"\u0447\u0442\u043e \u044d\u0442\u043e \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0439", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleName(QCoreApplication.translate("Dialog", u"\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0439 \u0438\u043c\u044f", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleDescription(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0435\u043b\u0435\u0438\u0439 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435</p></body></html>", None))
#endif // QT_CONFIG(accessibility)
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u0435 \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u043f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u044f", None))
        self.pushButtonSaveSettlement.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButtonDeleteSettlement.setText(QCoreApplication.translate("Dialog", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButtonAddSettlement.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0435 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

