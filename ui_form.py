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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
                               QSizePolicy, QStatusBar, QWidget, QDialog)

import ui_dialog_open #открыть новое окно из файла интерфейса
import ui_manage_households


class Ui_MainWindow(object):
    def open_households_rus(self):#RUS open households window
        self.window=QDialog()
        self.ui=ui_manage_households.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_dialog_rus(self): #открыть новое окно из файла интерфейса
        self.window = QDialog()
        self.ui=ui_dialog_open.Ui_Dialog()
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
        self.pushButton.setGeometry(QRect(130, 420, 111, 24))
        self.warning_button = QPushButton(self.centralwidget, clicked=lambda: self.open_dialog_rus())
        self.warning_button.setObjectName(u"warning_button")
        self.warning_button.setGeometry(QRect(450, 400, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"knopka v okno", None))
        self.warning_button.setText(QCoreApplication.translate("MainWindow", u"knopka v warn", None))
    # retranslateUi

