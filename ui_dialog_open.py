import pandas as pd
################################################################################
## Form generated from reading UI file 'dialog_open.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##pyside6-uic dialog.ui -o ui_dialog.py
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from IPython.display import display
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
from sqlalchemy import create_engine, text

import db_utils
import ui_edit_settlements
import ui_edit_cities
import ui_edit_households
import settings
class transfer_data:
    def __init__(self, in_pk, in_name, in_settlement):
        self.pk=in_pk
        self.name=in_name
        self.settlement=in_settlement




class Ui_Dialog(object):
    selected_table=0

    def clean_table(self, tablewidget):
        tablewidget.setColumnCount(0)
        tablewidget.setRowCount(0)

    def set_edit_method(self, editmethod):
        self.selected_table=editmethod

    def current_household(self):
        return self.householdTableWidget.item(self.householdTableWidget.currentRow(),0)

    def delete_item(self):
        print("ne implemented")


    def edit_button_pressed(self):
        if(self.selected_table==0):
            self.open_settlement_edit()
        if(self.selected_table==1):
            self.open_city_edit()
        if (self.selected_table == 2):
            self.open_household_edit()
    def open_settlement_edit(self):
        self.window = QDialog()
        self.ui = ui_edit_settlements.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_city_edit(self):  # opens hyety nesysvetnyu
        self.window = QDialog()
        self.ui = ui_edit_cities.Ui_Form()
        ui_edit_cities.Ui_Form.transfer_city_data(ui_edit_cities.Ui_Form,self.cityTableWidget.item(self.cityTableWidget.currentRow(),0).text(),self.cityTableWidget.item(self.cityTableWidget.currentRow(),1).text(), self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0).text())
        self.ui.setupUi(self.window)
        self.window.show()

    def open_household_edit(self):
        self.window = QDialog()
        self.ui = ui_edit_households.Ui_Form()
        ui_edit_households.Ui_Form.transfer_household_data(ui_edit_households.Ui_Form, self.householdTableWidget.item(self.householdTableWidget.currentRow(),0).text(), self.householdTableWidget.item(self.householdTableWidget.currentRow(),2).text(),self.householdTableWidget.item(self.householdTableWidget.currentRow(),1).text(), self.cityTableWidget.item(self.cityTableWidget.currentRow(),0).text(),self.settlementTableWidget.item(self.settlementTableWidget.currentRow(),0).text())# только начал поэтому хуй хуй хуй хуй
        self.ui.setupUi(self.window)
        self.window.show()

    def fill_cities_table(self):
        self.clean_table(self.householdTableWidget)
        # loads the table
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        # -----------------cities_table------------------------"
        pandas_SQL_query = f'SELECT city.pk, city.name, settlement.name FROM settlement INNER JOIN city ON city.belongs_to_settlement = settlement.pk WHERE settlement.pk = {self.settlementTableWidget.item(self.settlementTableWidget.currentRow(), 0).text()}'

        data_for_table = pd.read_sql(text(pandas_SQL_query), vet_db_connection).astype(str)
        self.cityTableWidget.setColumnCount(3)
        self.cityTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.cityTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def fill_households_table(self):
        # loads the table
        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

        pandas_SQL_query = f'SELECT household.pk, household.address, household.owner, city.name FROM household INNER JOIN city ON household.belongs_to_city = city.pk WHERE city.pk = {self.cityTableWidget.item(self.cityTableWidget.currentRow(), 0).text()}'

        data_for_table = pd.read_sql(pandas_SQL_query, vet_db_connection).astype(str)

        self.householdTableWidget.setColumnCount(4)
        self.householdTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            print("\n")  # debug
            for row_num in range(0, len(data_for_table)):
                print(QTableWidgetItem(data_for_table.iloc[row_num, col_num]).text())  # debug
                self.householdTableWidget.setItem(row_num, col_num,
                                                  QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    def refresh_table(self):
        DB_PATH = settings.DB_PATH  # vremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        # -----------------settlements_table------------------------
        data_for_table = pd.read_sql(text(f'SELECT pk,name FROM settlement'), vet_db_connection)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))
        display(data_for_table)
        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
        # -----------------cities_table------------------------
        data_for_table = pd.read_sql(text(
            f'SELECT city.pk, city.name, settlement.name FROM city LEFT JOIN settlement ON city.belongs_to_settlement = settlement.pk'),
                                     vet_db_connection)
        self.cityTableWidget.setColumnCount(3)
        self.cityTableWidget.setRowCount(len(data_for_table))
        display(data_for_table)

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(0, len(data_for_table)):
                self.cityTableWidget.setItem(row_num, col_num,
                                             QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
        #--------------------------households_table------------------------------------
        pandas_SQL_query = f'SELECT household.pk, household.address, household.owner, city.name FROM household INNER JOIN city ON household.belongs_to_city = city.pk WHERE city.pk = {self.cityTableWidget.item(self.cityTableWidget.currentRow(), 0).text()}'

        data_for_table = pd.read_sql(pandas_SQL_query, vet_db_connection).astype(str)

        self.householdTableWidget.setColumnCount(4)
        self.householdTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            print("\n")  # debug
            for row_num in range(0, len(data_for_table)):
                print(QTableWidgetItem(data_for_table.iloc[row_num, col_num]).text())  # debug
                self.householdTableWidget.setItem(row_num, col_num,
                                                  QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1062, 575)


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
        self.cityTableWidget.itemClicked.connect(lambda: self.fill_households_table())
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
        self.settlementTableWidget.itemClicked.connect(lambda: self.fill_cities_table())
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
        self.pushButton = QPushButton(Form, clicked= lambda: self.edit_button_pressed() )
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 530, 181, 31))

#pryachyshayasa knopka udalenia
        self.deletePushButton = QPushButton(Form, clicked= lambda:self.delete_item())
        self.deletePushButton.setObjectName(u"pushButton_2")
        self.deletePushButton.setGeometry(QRect(754, 530, 181, 31))
        self.deletePushButton.setText("Удалить выбранное")
        self.settlementTableWidget.cellClicked.connect(lambda:self.deletePushButton.hide())
        self.cityTableWidget.cellClicked.connect(lambda: self.deletePushButton.show())
        self.householdTableWidget.cellClicked.connect(lambda: self.deletePushButton.show())

        #  dlya knopki vibora
        self.settlementTableWidget.itemSelectionChanged.connect(lambda: self.set_edit_method(0))
        self.cityTableWidget.itemSelectionChanged.connect(lambda: self.set_edit_method(1))
        self.householdTableWidget.itemSelectionChanged.connect(lambda: self.set_edit_method(2))
        #  dlya knopki vibora

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        DB_PATH = settings.DB_PATH  # bezvremennoe reshenie
        TABLE_ROW_LIMIT = 10
        vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
        # ---------------settlements_table------------------------
        data_for_table = pd.read_sql(text(f'SELECT pk, name FROM settlement'), vet_db_connection).astype(str)
        self.settlementTableWidget.setColumnCount(2)
        self.settlementTableWidget.setRowCount(len(data_for_table))

        for col_num in range(len(data_for_table.columns)):
            for row_num in range(len(data_for_table)):
                self.settlementTableWidget.setItem(row_num, col_num,
                                                   QTableWidgetItem(data_for_table.iloc[row_num, col_num]))

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle("Правка Баз")

        ___qtablewidgetitem = self.householdTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem1 = self.householdTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441", None));
        ___qtablewidgetitem2 = self.householdTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u0412\u043b\u0430\u0434\u0435\u043b\u0435\u0446", None));
        ___qtablewidgetitem3 = self.householdTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None));
        ___qtablewidgetitem4 = self.cityTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem5 = self.cityTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None));
        ___qtablewidgetitem6 = self.cityTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText("Поселение");
        ___qtablewidgetitem7 = self.settlementTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"\u041f\u041a", None));
        ___qtablewidgetitem8 = self.settlementTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText("Поселение");
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0425\u043e\u0437\u044f\u0439\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u043b\u0435\u043d\u0438\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0435", None))
    # retranslateUi

