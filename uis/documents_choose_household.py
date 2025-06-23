# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'documents_household_choose.ui'
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
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1062, 575)
        self.choosePushButton = QPushButton(Form)
        self.choosePushButton.setObjectName(u"choosePushButton")
        self.choosePushButton.setGeometry(QRect(30, 530, 91, 31))
        self.closePushButton = QPushButton(Form)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setGeometry(QRect(900, 530, 91, 31))
        self.householdTableWidget = QTableWidget(Form)
        if (self.householdTableWidget.columnCount() < 4):
            self.householdTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.householdTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.householdTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.householdTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.householdTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.householdTableWidget.setObjectName(u"householdTableWidget")
        self.householdTableWidget.setGeometry(QRect(640, 40, 411, 471))
        self.cityTableWidget = QTableWidget(Form)
        if (self.cityTableWidget.columnCount() < 3):
            self.cityTableWidget.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.cityTableWidget.setObjectName(u"cityTableWidget")
        self.cityTableWidget.setGeometry(QRect(280, 40, 331, 471))
        self.settlementTableWidget = QTableWidget(Form)
        if (self.settlementTableWidget.columnCount() < 2):
            self.settlementTableWidget.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.settlementTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.settlementTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.settlementTableWidget.setObjectName(u"settlementTableWidget")
        self.settlementTableWidget.setGeometry(QRect(20, 40, 231, 471))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(660, 10, 101, 21))
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 10, 101, 21))
        self.label_4.setFont(font)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 101, 21))
        self.label_5.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u043e\u0440 \u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430 \u0434\u043b\u044f \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.choosePushButton.setText(QCoreApplication.translate("Form", u"\u0412\u042b\u0411\u041e\u0420", None))
        self.closePushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0410\u0417\u0410\u0414", None))
        ___qtablewidgetitem = self.householdTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem1 = self.householdTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem2 = self.householdTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446", None));
        ___qtablewidgetitem3 = self.householdTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None));
        ___qtablewidgetitem4 = self.cityTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem5 = self.cityTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem6 = self.cityTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText("Поселение");
        ___qtablewidgetitem7 = self.settlementTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem8 = self.settlementTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText("Поселение");
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0435", None))
    # retranslateUi

