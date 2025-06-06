# -*- coding: utf-8 -*-
from time import sleep

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
                               QWidget, QDialog, QTabWidget, QGridLayout, QFileDialog)

import ui_utilities_choose_statistics_tool
import ui_utilities_choose_vet_organization
import ui_utilities_database_merger
import ui_details_settings
import ui_dialog_open #открыть новое окно из файла интерфейса
import ui_documents_choose_household
import settings

class Ui_MainWindow(object):

    def open_households_rus(self):  # RUS open households window
        self.window = QDialog()
        self.ui = ui_documents_choose_household.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_db_edit_rus(self):  # открыть новое окно из файла интерфейса
        self.window = QDialog()
        self.ui = ui_dialog_open.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
#===============================menu buttons==================================================
    def open_details_edit(self):
        self.window = QDialog()
        self.ui = ui_details_settings.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_utilities_database_merger(self):
        self.window = QDialog()
        self.ui = ui_utilities_database_merger.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_utilities_vet_organiization_choose(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_vet_organization.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_utilities_statistics(self):
        self.window = QDialog()
        self.ui = ui_utilities_choose_statistics_tool.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_settings_window(self):
        print("nety")


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(673, 534)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.openHouseholdButton = QPushButton(self.centralwidget, clicked=lambda: self.open_households_rus())
        self.openHouseholdButton.setObjectName(u"openHouseholdButton")

        self.gridLayout_2.addWidget(self.openHouseholdButton, 3, 0, 2, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Onyx"])
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"./resources/2212_Zodiac_Taurus_Blog_Header_1200x628_EN.png"))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.editDbButton = QPushButton(self.centralwidget, clicked=lambda: self.open_db_edit_rus())
        self.editDbButton.setObjectName(u"editDbButton")

        self.gridLayout_2.addWidget(self.editDbButton, 1, 1, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 673, 22))

        self.menu_1 = QMenu(self.menubar)
        self.menu_1.setObjectName(u"menu_1")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)


        #Utils=========================================================
        self.menuActionUtilitiesDatabasesMerger = QAction()
        self.menuActionUtilitiesDatabasesMerger.triggered.connect(lambda:self.open_utilities_database_merger())
        self.menuActionUtilitiesDatabasesMerger.setText("Объединитель баз")

        self.menuActionUtilitiesVetOrgChoose = QAction()
        self.menuActionUtilitiesVetOrgChoose.triggered.connect(lambda: self.open_utilities_vet_organiization_choose())
        self.menuActionUtilitiesVetOrgChoose.setText("Выбор предприятия")

        self.menuActionUtilitiesStatistics = QAction()
        self.menuActionUtilitiesStatistics.triggered.connect(lambda: self.open_utilities_statistics())
        self.menuActionUtilitiesStatistics.setText("Cтатиcтическая утилита")



        #exxxxperimentyyyy=====================================
        self.utilitiesMenu =self.menubar.addMenu("Другие утилиты")
        self.utilitiesMenu.addAction(self.menuActionUtilitiesDatabasesMerger)
        self.utilitiesMenu.addAction(self.menuActionUtilitiesVetOrgChoose)
        self.utilitiesMenu.addAction(self.menuActionUtilitiesStatistics)
        # exxxxperimentyyyy=====================================

        # Utils=========================================================

        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText("Редактировать реквизиты")
        self.action.triggered.connect(lambda:self.open_details_edit())
#if QT_CONFIG(tooltip)
        self.openHouseholdButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u043a \u043e\u0444\u043e\u0440\u043c\u043b\u0435\u043d\u0438\u044e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
#endif // QT_CONFIG(tooltip)
        self.openHouseholdButton.setText("-------------------\n"
                                         "Оформление хозяйств\n"
                                         "-------------------")

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:700;\">TABP</span></p><p>подсистема поддержки процесса учёта животных ЛПХ</p></body></html>", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.editDbButton.setToolTip(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438 \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435 \u0445\u043e\u0437\u044f\u0439\u0441\u0442\u0432 \u0438\u0437 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
#endif // QT_CONFIG(tooltip)
        self.editDbButton.setText(QCoreApplication.translate("MainWindow", u"--------------\n"
"\u041f\u0420\u0410\u0412\u041a\u0410 \u0411\u0410\u0417\n"
"--------------", None))
        self.menu_1.setTitle(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u044d\u043a\u0440\u0430\u043d", None))
        self.menu.setTitle("Реквизиты ветеринарной службы")
        self.menu_settings.setTitle("Настройки")
    # retranslateUi


