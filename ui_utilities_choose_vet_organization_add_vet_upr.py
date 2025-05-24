# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'utilities_choose_vet_organization_add_vet_uprcwtiCe.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(539, 329)
        self.confirmPushButton = QPushButton(Form)
        self.confirmPushButton.setObjectName(u"confirmPushButton")
        self.confirmPushButton.setGeometry(QRect(10, 250, 161, 51))
        self.cancelPushButton = QPushButton(Form)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setGeometry(QRect(350, 250, 161, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 351, 51))
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.confirmPushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:18pt;\">\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0432\u0435\u0442\u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f</span></p></body></html>", None))
    # retranslateUi

