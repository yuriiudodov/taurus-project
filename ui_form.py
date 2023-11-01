# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QWidget, QDialog)

import ui_dialog_open #открыть новое окно из файла интерфейса
import ui_manage_households


def open_households_rus(self):  # RUS open households window
    self.window = QDialog()
    self.ui = ui_manage_households.Ui_Dialog()
    self.ui.setupUi(self.window)
    self.window.show()


def open_dialog_rus(self):  # открыть новое окно из файла интерфейса
    self.window = QDialog()
    self.ui = ui_dialog_open.Ui_Dialog()
    self.ui.setupUi(self.window)
    self.window.show()

class Ui_MainWindow(object):
    def open_households_rus(self):  # RUS open households window
        self.window = QDialog()
        self.ui = ui_manage_households.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_db_edit_rus(self):  # открыть новое окно из файла интерфейса
        self.window = QDialog()
        self.ui = ui_dialog_open.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget, clicked=lambda: self.open_households_rus())
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 450, 201, 24))
        self.warning_button = QPushButton(self.centralwidget, clicked=lambda: self.open_db_edit_rus())
        self.warning_button.setObjectName(u"warning_button")
        self.warning_button.setGeometry(QRect(490, 430, 151, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -10, 451, 361))
        self.label.setPixmap(QPixmap(u"./resources/2212_Zodiac_Taurus_Blog_Header_1200x628_EN.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 40, 171, 101))
        font = QFont()
        font.setFamilies([u"Onyx"])
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 70, 171, 101))
        self.label_3.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_1.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0444\u043e\u0440\u043c\u043b\u044f\u0442\u044c \u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u0430", None))
        self.warning_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u0410\u0412\u041a\u0410 \u0411\u0410\u0417", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">TABP</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0441\u0430\u043c\u043e\u0435 \u0441\u0442\u0438\u043b\u044c\u043d\u043e\u0435 \u043e\u043a\u043d\u043e \u043d\u0430 \u0434\u0438\u043a\u043e\u043c \u0437\u0430\u043f\u0430\u0434\u0435</p></body></html>", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u0432\u043a\u043b\u0430\u0434\u043a\u04301", None))
    # retranslateUi

