# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_households.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(744, 721)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, -10, 651, 711))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.settlementTableWidget = QTableWidget(self.layoutWidget)
        self.settlementTableWidget.itemClicked.connect(lambda: self.fill_cities_table())
        if (self.settlementTableWidget.columnCount() < 2):
            self.settlementTableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.settlementTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.settlementTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.settlementTableWidget.setObjectName(u"settlementTableWidget")

        self.gridLayout.addWidget(self.settlementTableWidget, 4, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.cityTableWidget = QTableWidget(self.layoutWidget)
        if (self.cityTableWidget.columnCount() < 3):
            self.cityTableWidget.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cityTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.cityTableWidget.setObjectName(u"cityTableWidget")

        self.gridLayout.addWidget(self.cityTableWidget, 4, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 2, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 3)

        self.saveButton = QPushButton(self.layoutWidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.saveButton, 5, 1, 1, 1)

        self.writeButton = QPushButton(self.layoutWidget)
        self.writeButton.setObjectName(u"writeButton")
        self.writeButton.setMinimumSize(QSize(0, 50))

        self.gridLayout.addWidget(self.writeButton, 5, 2, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.settlementTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.settlementTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0439\u043e\u043d", None));
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0435", None))
        ___qtablewidgetitem2 = self.cityTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem3 = self.cityTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u0441\u0442\u043e\u043b\u0431\u0435\u0446", None));
        ___qtablewidgetitem4 = self.cityTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0439\u043e\u043d", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446 ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:700;\">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0425\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u043e</span></p></body></html>", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.writeButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c \u043a\u0430\u043a \u043d\u043e\u0432\u044b\u0439", None))
    # retranslateUi

