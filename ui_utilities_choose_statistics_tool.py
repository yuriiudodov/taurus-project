# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PySide6 import QtGui
################################################################################
## Form generated from reading UI file 'statistics_toolxlsIwo.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QWidget, QDialog)
import seaborn as sns
from pandas import DataFrame

import ui_utilities_choose_statistics_tool_choose_data


class Ui_Form(object):
    selected_city=0
    selected_settlement=0
    def open_choose_data(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_statistics_tool_choose_data.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def transfer_data(self, selected_city=-1, selected_settlement=-1):
        self.selected_settlement=selected_settlement
        self.selected_city=selected_city

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(719, 502)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 511, 31))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.graphLabel = QLabel(Form)
        self.graphLabel.setObjectName(u"graphLabel")
        print("hyyyp")
        self.graphLabel.setGeometry(QRect(20, 60, 641, 371))
        pixmap=QPixmap("graph.png")
        self.graphLabel.setPixmap(pixmap)
        self.graphLabel.setScaledContents(True)


        self.chooseDataPushButton = QPushButton(Form, clicked = lambda:self.open_choose_data())
        self.chooseDataPushButton.setObjectName(u"chooseDataPushButton")
        self.chooseDataPushButton.setGeometry(QRect(10, 443, 111, 41))
        self.drawGraphPushButton = QPushButton(Form)
        self.drawGraphPushButton.setObjectName(u"drawGraphPushButton")
        self.drawGraphPushButton.setGeometry(QRect(150, 443, 121, 41))
        self.createReportPushButton = QPushButton(Form)
        self.createReportPushButton.setObjectName(u"createReportPushButton")
        self.createReportPushButton.setGeometry(QRect(290, 443, 121, 41))
        self.cancelPushButton = QPushButton(Form, clicked =lambda:Form.close())
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(610, 440, 101, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0438", None))
        #self.graphLabel.setText("Выберитте данные для построения графика")
        self.chooseDataPushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.drawGraphPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a", None))
        self.createReportPushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u043e\u0442\u0447\u0435\u0442", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

