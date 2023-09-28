# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manage_households.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import pandas as pd
from sqlalchemy import create_engine



class Ui_Dialog(object):
    def __init__(self):
        super().__init__()

    def get_data_db(self, table_name, db_connection):
        data = pd.read_sql(f'SELECT * FROM {table_name}', db_connection)


    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(898, 450)
        self.householdsWidget = QTableWidget(Dialog)
        self.householdsWidget.setObjectName(u"householdsWidget", )
        self.householdsWidget.setGeometry(QRect(30, 30, 461, 221))
        self.citiesWidget = QTableWidget(Dialog)
        self.citiesWidget.setObjectName(u"citiesWidget")
        self.citiesWidget.setGeometry(QRect(610, 40, 221, 251))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(640, 10, 111, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 111, 16))
        self.refreshButton = QPushButton(Dialog)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(40, 260, 80, 24))

        self.retranslateUi(Dialog)
        DB_PATH = 'MainDatabaseVet'#vremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        # data_for_table=self.get_data_db(self, vet_db_connection, "city")
        # cities         = pd.read_sql(f'''SELECT * FROM city''', vet_db_connection).rename(columns={'name': 'city_name'})
        # settlements    = pd.read_sql(f'''SELECT * FROM settlement''', vet_db_connection).rename(columns={'pk': 'pk_settlement', 'name': 'settlement_name'})
        # data_for_table = cities.merge(settlements, left_on='belongs_to_settlement', right_on='pk_settlement', how='outer')
        # data_for_table = data_for_table[['city_name', 'settlement_name']].fillna('')

        data_for_table = pd.read_sql(f'''
            SELECT city.name as CityName, settlement.name as SettlementName FROM city
            INNER JOIN settlement
                ON settlement.pk = city.belongs_to_settlement;
        ''', vet_db_connection)

        data_for_table = data_for_table.filter(set(data_for_table.columns) - {'belongs_to_settlement', 'pk'})
        print(data_for_table)

        self.citiesWidget.setColumnCount(len(data_for_table.columns))
        self.citiesWidget.setRowCount(len(data_for_table))
        self.citiesWidget.setHorizontalHeaderLabels(data_for_table.columns)

        for col_num, col in enumerate(data_for_table.columns):
            for row_num, row in enumerate(data_for_table.index):
                self.citiesWidget.setItem(row_num, col_num, QTableWidgetItem(data_for_table.loc[row, col]))

        def add_new_city(event, table, label):
            if event.key() == Qt.Key.Key_Delete and table.currentColumn() == 0:
                label.setText(table.currentItem().text())

        self.citiesWidget.keyPressEvent = lambda x: add_new_city(x, self.citiesWidget, self.label)

        QMetaObject.connectSlotsByName(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0411\u043e\u043b\u044c\u0448\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0425\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430", None))
        self.refreshButton.setText(QCoreApplication.translate("Dialog", u"refresh", None))
    # retranslateUi

