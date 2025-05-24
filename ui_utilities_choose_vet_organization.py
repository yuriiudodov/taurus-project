# -*- coding: utf-8 -*-
import pandas as pd
################################################################################
## Form generated from reading UI file 'utilities_choose_vet_organizationwjEHcj.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
                               QSizePolicy, QTableWidget, QTableWidgetItem, QWidget, QDialog)
from sqlalchemy import create_engine, text

import ui_utilities_choose_vet_organization_add_vet_station
import ui_utilities_choose_vet_organization_add_vet_upr
import ui_utilities_choose_vet_organization_edit_vet_station
import ui_utilities_choose_vet_organization_edit_vet_upr
from db_utils import DB_PATH


class Ui_Form(object):
    workmode="default"

    def refresh_table(self, tablewidget, tablename):
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        data_for_table = pd.read_sql(text(f'SELECT * FROM {tablename}'), vet_db_connection).astype(str)
        print(data_for_table)
        tablewidget.setColumnCount(len(data_for_table.columns))
        tablewidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                tablewidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))


    def change_workmode(self, workmode):
        self.workmode = workmode

    def edit_button_clicked(self):
        match self.workmode:
            case "Station":
                self.open_utilities_vet_organiization_edit_vet_station()
            case "Upr":
                self.open_utilities_vet_organiization_edit_vet_upr()
            case _:
                print("Nepravilnoe znachenie workmode")
    def add_button_clicked(self):
        match self.workmode:
            case "Station":
                self.open_utilities_vet_organiization_add_vet_station()
            case "Upr":
                self.open_utilities_vet_organiization_add_vet_upr()
            case _:
                print("Nepravilnoe znachenie workmode")
    def open_utilities_vet_organiization_add_vet_station(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_vet_organization_add_vet_station.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_utilities_vet_organiization_edit_vet_station(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_vet_organization_edit_vet_station.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_utilities_vet_organiization_add_vet_upr(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_vet_organization_add_vet_upr.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_utilities_vet_organiization_edit_vet_upr(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_vet_organization_edit_vet_upr.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(889, 668)
        self.editPushButton = QPushButton(Form,clicked=lambda:self.edit_button_clicked())
        self.editPushButton.setObjectName(u"editPushButton")
        self.editPushButton.setGeometry(QRect(170, 610, 121, 41))
        self.confirmPushButton = QPushButton(Form)
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(310, 610, 131, 41))
        self.closePushButton = QPushButton(Form)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(690, 610, 151, 41))
        self.vetUpravlenietableWidget = QTableWidget(Form, itemClicked = lambda:self.change_workmode("Upr"))
        self.vetUpravlenietableWidget.setObjectName(u"vetUpravlenietableWidget")
        self.vetUpravlenietableWidget.setGeometry(QRect(25, 120, 401, 451))
        self.vetStationTableWidget = QTableWidget(Form, itemClicked = lambda:self.change_workmode("Station"))
        self.vetStationTableWidget.setObjectName(u"vetStationTableWidget")
        self.vetStationTableWidget.setGeometry(QRect(460, 120, 391, 451))
        self.titleLabel = QLabel(Form)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(30, 20, 401, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 90, 101, 16))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 90, 101, 16))
        self.addPushButton = QPushButton(Form,clicked = lambda:self.add_button_clicked())
        self.addPushButton.setObjectName(u"addPushButton")
        self.addPushButton.setGeometry(QRect(30, 610, 121, 41))
        self.deletePushButton = QPushButton(Form)
        self.deletePushButton.setObjectName(u"deletePushButton")
        self.deletePushButton.setGeometry(QRect(550, 610, 61, 41))

        self.retranslateUi(Form)

        self.refresh_table(self.vetStationTableWidget, "vet_station")
        self.refresh_table(self.vetUpravlenietableWidget, "vet_administration")  # vet_upr

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.editPushButton.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.closePushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
        self.titleLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u041d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0432\u0435\u0442\u0443\u0447\u0430\u0441\u0442\u043a\u0430</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0442\u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0442\u0443\u0447\u0430\u0441\u0442\u043e\u043a", None))
        self.addPushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.deletePushButton.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

