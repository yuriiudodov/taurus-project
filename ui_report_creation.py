# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_creation.ui'
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
import ui_animal_add

class Ui_Form(object):
    def create_report(self):
        print("ne sozdayotsa")
    def delete_animal(self):
        print("ne ydalyaetsya")
    def open_animals_add(self):
        self.window = QWidget()
        self.ui = ui_animal_add.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_animals_edit(self):
        print("ne redachitsa")
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(758, 527)
        font = QFont()
        font.setPointSize(9)
        Form.setFont(font)
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))
        Form.setWindowIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 50, 81, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 91, 41))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 81, 41))
        self.label_3.setFont(font1)
        self.placeForCity = QLabel(Form)
        self.placeForCity.setObjectName(u"placeForCity")
        self.placeForCity.setGeometry(QRect(90, 10, 251, 41))
        self.placeForCity.setFont(font1)
        self.placeForAddress = QLabel(Form)
        self.placeForAddress.setObjectName(u"placeForAddress")
        self.placeForAddress.setGeometry(QRect(100, 50, 251, 41))
        self.placeForAddress.setFont(font1)
        self.placeForOwner = QLabel(Form)
        self.placeForOwner.setObjectName(u"placeForOwner")
        self.placeForOwner.setGeometry(QRect(110, 90, 251, 41))
        self.placeForOwner.setFont(font1)
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 160, 701, 281))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 120, 191, 51))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.documentAddAnimal = QPushButton(Form, clicked=lambda:self.open_animals_add())
        self.documentAddAnimal.setObjectName(u"documentAddAnimal")
        self.documentAddAnimal.setGeometry(QRect(20, 470, 141, 41))
        self.createHouseholdReport = QPushButton(Form, clicked=lambda:self.create_report())
        self.createHouseholdReport.setObjectName(u"createHouseholdReport")
        self.createHouseholdReport.setGeometry(QRect(540, 460, 191, 51))
        self.createHouseholdReport.setToolTipDuration(2)
        self.documentDeleteAnimal = QPushButton(Form, clicked=lambda:self.delete_animal())
        self.documentDeleteAnimal.setObjectName(u"documentDeleteAnimal")
        self.documentDeleteAnimal.setGeometry(QRect(340, 470, 141, 41))
        self.documentAddAnimal_2 = QPushButton(Form, clicked=lambda:self.open_animals_edit())#i forgot to rename it, it is actually edit button
        self.documentAddAnimal_2.setObjectName(u"documentAddAnimal_2")
        self.documentAddAnimal_2.setGeometry(QRect(170, 470, 161, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u0443\u0441\u043a \u041e\u0442\u0447\u0451\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.placeForCity.setText(QCoreApplication.translate("Form", u"placeForCity", None))
        self.placeForAddress.setText(QCoreApplication.translate("Form", u"placeForAddress", None))
        self.placeForOwner.setText(QCoreApplication.translate("Form", u"placeForOwner", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u0444\u0430\u043a\u0442.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u0430\u0434\u043c.", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u043f\u0440\u0435\u0434", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u0423\u0441\u043b\u043e\u0432\u0438\u044f \n"
"\u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText("Вид");
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0416\u0438\u0432\u043e\u0442\u043d\u044b\u0435 \u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430", None))
        self.documentAddAnimal.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0435", None))
#if QT_CONFIG(tooltip)
        self.createHouseholdReport.setToolTip(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u0443\u0441\u043a \u043e\u0442\u0447\u0451\u0442\u0430 \u0438 \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0444\u0430\u0439\u043b", u"\u0412\u044b\u043f\u0443\u0441\u043a \u043e\u0442\u0447\u0451\u0442\u0430 \u0438 \u0437\u0430\u043f\u0438\u0441\u044c \u0432 \u0444\u0430\u0439\u043b"))
#endif // QT_CONFIG(tooltip)
        self.createHouseholdReport.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0431\u0435\u0448\u0435\u043d\u044b\u0445 \u043f\u0438\u0434\u043e\u0440\u043e\u0432", None))
        self.documentDeleteAnimal.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0435", None))
        self.documentAddAnimal_2.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0416\u0438\u0432\u043e\u0442\u043d\u043e\u0435", None))
    # retranslateUi

