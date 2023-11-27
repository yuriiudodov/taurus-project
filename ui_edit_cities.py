# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_cities.ui'
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
                               QTableWidget, QTableWidgetItem, QWidget, QGridLayout, QFormLayout)
from sqlalchemy import create_engine, text
import pandas as pd
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(536, 387)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.cityNamelineEdit = QLineEdit(Form)
        self.cityNamelineEdit.setObjectName(u"cityNamelineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cityNamelineEdit)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.selectSettlementTableWidget = QTableWidget(Form)
        if (self.selectSettlementTableWidget.columnCount() < 2):
            self.selectSettlementTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.selectSettlementTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.selectSettlementTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.selectSettlementTableWidget.setObjectName(u"selectSettlementTableWidget")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.selectSettlementTableWidget)

        self.saveCityPushButton = QPushButton(Form)
        self.saveCityPushButton.setObjectName(u"saveCityPushButton")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.saveCityPushButton)

        self.NewCityPushButton = QPushButton(Form)
        self.NewCityPushButton.setObjectName(u"NewCityPushButton")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.NewCityPushButton)


        self.retranslateUi(Form)
        DB_PATH = 'MainDatabaseVet'
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection).astype(str)
        self.selectSettlementTableWidget.setColumnCount(2)
        self.selectSettlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.selectSettlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0433\u043e\u0440\u043e\u0434\u0430</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0435", None))
        ___qtablewidgetitem = self.selectSettlementTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.selectSettlementTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0435", None));
        self.saveCityPushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.NewCityPushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043a\u0430\u043a \u043d\u043e\u0432\u044b\u0439", None))
    # retranslateUi
