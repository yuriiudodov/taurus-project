# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'utilities_choose_vet_organization_edit_vet_stationkJBzjK.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

import db_utils


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(539, 540)
        self.confirmPushButton = QPushButton(Form)
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(10, 480, 161, 51))
        self.cancelPushButton = QPushButton(Form)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(350, 480, 161, 51))
        self.vetUpravlenieTableWidget = QTableWidget(Form)
        self.vetUpravlenieTableWidget.setObjectName(u"vetUpravlenieTableWidget")
        self.vetUpravlenieTableWidget.setGeometry(QRect(150, 240, 371, 231))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 321, 51))
        self.nameLineEdit = QLineEdit(Form)
        self.nameLineEdit.setObjectName(u"nameLineEdit")
        self.nameLineEdit.setGeometry(QRect(150, 80, 371, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 80, 91, 21))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 111, 21))
        self.infoTextEdit = QTextEdit(Form)
        self.infoTextEdit.setObjectName(u"infoTextEdit")
        self.infoTextEdit.setGeometry(QRect(150, 120, 371, 101))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 240, 111, 21))
        self.isMainCheckBox = QCheckBox(Form)
        self.isMainCheckBox.setObjectName(u"isMainCheckBox")
        self.isMainCheckBox.setGeometry(QRect(350, 20, 111, 31))

        self.retranslateUi(Form)

        db_utils.refresh_table(self.vetUpravlenieTableWidget, "vet_administration")

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0435\u0442\u0443\u0447\u0430\u0441\u0442\u043a\u0430</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0412\u0435\u0442\u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435</span></p></body></html>", None))
        self.isMainCheckBox.setText(QCoreApplication.translate("Form", u"\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439", None))
    # retranslateUi

