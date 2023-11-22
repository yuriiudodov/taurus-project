# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'dialog_open.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##pyside6-uic dialog.ui -o ui_dialog.py
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
from sqlalchemy import create_engine, text

import ui_edit_cities
import ui_edit_settlements


class Ui_Dialog(object):
    def open_settlement_edit(self):
        self.window = QDialog()
        self.ui = ui_edit_settlements.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_city_edit(self):#opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui=ui_edit_cities.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_household_edit(self):
        print("nichego poka chto")

    def fill_cities_table(self):
        # loads the table
        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        # -----------------cities_table------------------------
        data_for_table = pd.read_sql(text(
            f'SELECT city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'),
            vet_db_connection)
        self.cityTableWidget.setColumnCount(2)
        self.cityTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.cityTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def fill_households_table(self):
        # loads the table
        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        pandas_SQL_query=f'SELECT household.address, household.owner, city.name FROM city right JOIN household ON household.belongs_to_city = ' + (self.cityTableWidget.item(self.cityTableWidget.currentRow(), 0).text())# need help blin
        data_for_table = pd.read_sql(text(pandas_SQL_query,vet_db_connection))
        self.householdTableWidget.setColumnCount(3)
        self.householdTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.householdTableWidget.setItem(row_num, col_num,
                                                  QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def refres_table(self):
        DB_PATH = 'MainDatabaseVet'  # vremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        #-----------------settlements_table------------------------
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
        # -----------------cities_table------------------------
        data_for_table = pd.read_sql(text(f'SELECT city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'), vet_db_connection)
        self.cityTableWidget.setColumnCount(2)
        self.cityTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.cityTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(851, 621)
        self.cityTableWidget = QTableWidget(Dialog)
        self.cityTableWidget.setObjectName(u"cityTableWidget")
        self.cityTableWidget.setGeometry(QRect(300, 70, 256, 192))
        self.settlementTableWidget = QTableWidget(Dialog)
        self.settlementTableWidget.itemClicked.connect(lambda: self.fill_cities_table())
        self.settlementTableWidget.setObjectName(u"settlementTableWidget")
        self.settlementTableWidget.setGeometry(QRect(10, 70, 256, 192))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 141, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 50, 141, 16))
        self.settlementPushButton = QPushButton(Dialog, clicked=lambda: self.open_settlement_edit())
        self.settlementPushButton.setObjectName(u"settlementPushButton")
        self.settlementPushButton.setGeometry(QRect(20, 270, 161, 24))
        self.cityPushButton = QPushButton(Dialog, clicked=lambda: self.open_city_edit())
        self.cityPushButton.setObjectName(u"cityPushButton")
        self.cityPushButton.setGeometry(QRect(300, 270, 161, 24))
        self.householdTableWidget = QTableWidget(Dialog)
        self.householdTableWidget.setObjectName(u"householdTableWidget")
        self.householdTableWidget.setGeometry(QRect(580, 70, 256, 192))
        self.householdPushButton = QPushButton(Dialog, clicked=lambda: self.open_household_edit())
        self.cityTableWidget.itemClicked.connect(lambda: self.fill_households_table())
        self.householdPushButton.setObjectName(u"householdPushButton")
        self.householdPushButton.setGeometry(QRect(580, 270, 161, 24))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 40, 141, 16))
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 580, 91, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        #loads the table
        DB_PATH = 'MainDatabaseVet'  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        # ---------------settlements_table------------------------
        data_for_table = pd.read_sql(text(f'SELECT name FROM settlement'), vet_db_connection)
        self.settlementTableWidget.setColumnCount(1)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))




    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0439\u043e\u043d\u044b", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0440\u043e\u0434\u0430", None))
        self.settlementPushButton.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.cityPushButton.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.householdPushButton.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0425\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
    # retranslateUi

