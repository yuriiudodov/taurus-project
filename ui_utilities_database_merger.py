# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_mergerATGYHk.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):

    def change_nonstandart_database_box_visibility(self):
        if self.nonStandartDatabaseCheckBox.checkState().value ==2:
            self.groupBox.show()
        if self.nonStandartDatabaseCheckBox.checkState().value ==0:
            self.groupBox.hide()
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(847, 488)
        self.titleLabel = QLabel(Form)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, -10, 421, 81))
        font = QFont()
        font.setPointSize(18)
        self.titleLabel.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 270, 391, 201))
        self.groupBox.hide()
        self.schemeGeneratePushButton = QPushButton(self.groupBox)
        self.schemeGeneratePushButton.setObjectName(u"schemeGeneratePushButton")
        self.schemeGeneratePushButton.setGeometry(QRect(210, 140, 151, 51))
        self.schemeFilenameChoosePushButton = QPushButton(self.groupBox)
        self.schemeFilenameChoosePushButton.setObjectName(u"schemeFilenameChoosePushButton")
        self.schemeFilenameChoosePushButton.setGeometry(QRect(10, 140, 151, 51))
        self.schemeFilenameLabel = QLabel(self.groupBox)
        self.schemeFilenameLabel.setObjectName(u"schemeFilenameLabel")
        self.schemeFilenameLabel.setGeometry(QRect(10, 110, 191, 16))
        self.schemeFilenameLabel_2 = QLabel(self.groupBox)
        self.schemeFilenameLabel_2.setObjectName(u"schemeFilenameLabel_2")
        self.schemeFilenameLabel_2.setGeometry(QRect(210, 110, 191, 16))
        self.schemeFilenameChoosePushButton_2 = QPushButton(self.groupBox)
        self.schemeFilenameChoosePushButton_2.setObjectName(u"schemeFilenameChoosePushButton_2")
        self.schemeFilenameChoosePushButton_2.setGeometry(QRect(200, 40, 171, 51))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 60, 391, 201))
        self.nonStandartDatabaseCheckBox = QCheckBox(self.groupBox_2,stateChanged=lambda:self.change_nonstandart_database_box_visibility())
        self.nonStandartDatabaseCheckBox.setObjectName(u"nonStandartDatabaseCheckBox")
        self.nonStandartDatabaseCheckBox.setGeometry(QRect(10, 170, 191, 20))

        self.filenameChoosePushButton_2 = QPushButton(self.groupBox_2)
        self.filenameChoosePushButton_2.setObjectName(u"filenameChoosePushButton_2")
        self.filenameChoosePushButton_2.setGeometry(QRect(200, 60, 151, 51))
        self.filenameLabel_2 = QLabel(self.groupBox_2)
        self.filenameLabel_2.setObjectName(u"filenameLabel_2")
        self.filenameLabel_2.setGeometry(QRect(210, 20, 151, 20))
        self.filenameChoosePushButton_1 = QPushButton(self.groupBox_2)
        self.filenameChoosePushButton_1.setObjectName(u"filenameChoosePushButton_1")
        self.filenameChoosePushButton_1.setGeometry(QRect(10, 60, 151, 51))
        self.filenameLabel_1 = QLabel(self.groupBox_2)
        self.filenameLabel_1.setObjectName(u"filenameLabel_1")
        self.filenameLabel_1.setGeometry(QRect(10, 20, 211, 16))
        self.autoCheckBox = QCheckBox(self.groupBox_2)
        self.autoCheckBox.setObjectName(u"autoCheckBox")
        self.autoCheckBox.setGeometry(QRect(10, 140, 141, 20))
        self.autoCheckBox.setChecked(True)
        self.autoCheckBox.setTristate(False)
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(420, 270, 411, 201))
        self.filenameChoosePushButton_3 = QPushButton(self.groupBox_3)
        self.filenameChoosePushButton_3.setObjectName(u"filenameChoosePushButton_3")
        self.filenameChoosePushButton_3.setGeometry(QRect(20, 120, 151, 51))
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 120, 161, 51))
        self.exportPathLineEdit = QLineEdit(self.groupBox_3)
        self.exportPathLineEdit.setObjectName(u"exportPathLineEdit")
        self.exportPathLineEdit.setGeometry(QRect(10, 80, 391, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel.setText("Выбор предприятия")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041d\u0435\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f \u0431\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.schemeGeneratePushButton.setText(QCoreApplication.translate("Form", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0445\u0435\u043c\u044b", None))
        self.schemeFilenameChoosePushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.schemeFilenameLabel.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u0439\u043b \u0441\u0445\u0435\u043c\u044b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.schemeFilenameLabel_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 ", None))
        self.schemeFilenameChoosePushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b \n"
" \u0414\u043b\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u0412\u0445\u043e\u0434", None))
        self.nonStandartDatabaseCheckBox.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0441\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u0430\u044f \u0431\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.filenameChoosePushButton_2.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.filenameLabel_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u0439\u043b \u0411\u0430\u0437\u044b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.filenameChoosePushButton_1.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.filenameLabel_1.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u0439\u043b \u0411\u0430\u0437\u044b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.autoCheckBox.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0441\u0445\u0435\u043c\u044b", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u043e\u0434", None))
        self.filenameChoosePushButton_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
    # retranslateUi

