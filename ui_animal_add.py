# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'animal_add.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

import settings


class Ui_Form(object):
    def transfer_animal_add_data(self, household_pk):
        self.household_pk=household_pk
        print("A V ui animals add peredan pk hoziaistva:", self.household_pk)
    def add_animal_to_household(self):
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        VetDbConnnection = QSqlDatabase.addDatabase("QSQLITE")
        VetDbConnnection.setDatabaseName(DB_PATH)
        VetDbConnnection.open()
        VetTableQuery = QSqlQuery()
        VetTableQuery.prepare("""
                       INSERT INTO report_entries (household, specie,count, data_from_administration, prevous_count, is_conditions_good) VALUES (:household, :specie,:count, :data_from_administration, :prevous_count, :is_conditions_good)
                       """)
        VetTableQuery.bindValue(":specie",self.specieLineEdit.text())
        VetTableQuery.bindValue(":household", self.household_pk)
        VetTableQuery.bindValue(":count", self.countFactLineEdit.text())
        VetTableQuery.bindValue(":data_from_administration", self.countAdmLineEdit.text())
        VetTableQuery.bindValue(":is_conditions_good", self.containmentConditionsLineEdit.text())
        VetTableQuery.exec()
        VetDbConnnection.close()
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 550)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.specieLineEdit = QLineEdit(Form)
        self.specieLineEdit.setObjectName(u"specieLineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.specieLineEdit.sizePolicy().hasHeightForWidth())
        self.specieLineEdit.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.specieLineEdit, 1, 0, 1, 1)

        self.countFactLineEdit = QLineEdit(Form)
        self.countFactLineEdit.setObjectName(u"countFactLineEdit")

        self.gridLayout.addWidget(self.countFactLineEdit, 2, 0, 1, 1)

        self.countAdmLineEdit = QLineEdit(Form)
        self.countAdmLineEdit.setObjectName(u"countAdmLineEdit")

        self.gridLayout.addWidget(self.countAdmLineEdit, 3, 0, 1, 1)

        self.confirmButton = QPushButton(Form)
        self.confirmButton.setObjectName(u"confirmButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.confirmButton.sizePolicy().hasHeightForWidth())
        self.confirmButton.setSizePolicy(sizePolicy1)
        self.confirmButton.setMaximumSize(QSize(200, 120))

        self.gridLayout.addWidget(self.confirmButton, 6, 0, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(230, 16777215))

        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)

        self.containmentConditionsLineEdit = QTextEdit(Form)
        self.containmentConditionsLineEdit.setObjectName(u"containmentConditionsLineEdit")

        self.gridLayout.addWidget(self.containmentConditionsLineEdit, 5, 0, 1, 2)

        self.countPrevLineEdit = QLineEdit(Form)
        self.countPrevLineEdit.setObjectName(u"countPrevLineEdit")

        self.gridLayout.addWidget(self.countPrevLineEdit, 4, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0433\u043e \u0432 \u043e\u0442\u0447\u0451\u0442", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0433\u043e", None))
        self.specieLineEdit.setText("")
        self.specieLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0438\u0434", None))
        self.countFactLineEdit.setText("")
        self.countFactLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 ", None))
        self.countAdmLineEdit.setText("")
        self.countAdmLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u0430\u0434\u043c.", None))
        self.confirmButton.setText(QCoreApplication.translate("Form", u"\u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.containmentConditionsLineEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f...</p></body></html>", None))
        self.countPrevLineEdit.setText("")
        self.countPrevLineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0440\u0435\u0434.", None))
    # retranslateUi

