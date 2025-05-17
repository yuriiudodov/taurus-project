# -*- coding: utf-8 -*-
import os

import pandas as pd
################################################################################
## Form generated from reading UI file 'details_settingscfEXHJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

import settings


class Ui_Form(object):
    def read_details_from_file(self):
        filename = settings.DETAILS_FILE

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        open(filename, "r").readlines()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1042, 513)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label)

        self.specialistLineEdit = QLineEdit(Form)
        self.specialistLineEdit.setObjectName(u"specialistLineEdit")
        font1 = QFont()
        font1.setPointSize(14)
        self.specialistLineEdit.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.specialistLineEdit)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_3)

        self.vetOrganizationLineEdit = QLineEdit(Form)
        self.vetOrganizationLineEdit.setObjectName(u"vetOrganizationLineEdit")
        self.vetOrganizationLineEdit.setFont(font1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.vetOrganizationLineEdit)

        self.saveDetailsPushButton = QPushButton(Form)
        self.saveDetailsPushButton.setObjectName(u"saveDetailsPushButton")
        self.saveDetailsPushButton.setFont(font1)

        self.formLayout.setWidget(12, QFormLayout.SpanningRole, self.saveDetailsPushButton)

        self.closePushButton = QPushButton(Form)
        self.closePushButton.setObjectName(u"closePushButton")
        font2 = QFont()
        font2.setPointSize(13)
        self.closePushButton.setFont(font2)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.closePushButton)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(True)
        self.label_4.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.managerLineEdit = QLineEdit(Form)
        self.managerLineEdit.setObjectName(u"managerLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.managerLineEdit.sizePolicy().hasHeightForWidth())
        self.managerLineEdit.setSizePolicy(sizePolicy)
        self.managerLineEdit.setMinimumSize(QSize(0, 0))
        self.managerLineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.managerLineEdit.setBaseSize(QSize(0, 0))
        self.managerLineEdit.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.managerLineEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("Настройка реквизитов")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418.\u041e. \u0437\u0430\u0432\u0435\u0434\u0443\u0449\u0435\u0433\u043e  \u0432\u0435\u0442\u0443\u0447\u0430\u0441\u0442\u043a\u043e\u043c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0412\u0435\u0442\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.saveDetailsPushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0420\u0435\u043a\u0432\u0438\u0437\u0438\u0442\u044b", None))
        self.closePushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u043e\u043a\u043d\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0410 \u0420\u0415\u041a\u0412\u0418\u0417\u0418\u0422\u041e\u0412 \u041e\u0422\u0427\u0401\u0422\u0410", None))
    # retranslateUi

