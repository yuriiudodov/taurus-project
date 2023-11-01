# This Python file uses the following encoding: utf-8
import sys
import ui_dialog_open
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from sqlalchemy import create_engine

from ui_form import Ui_MainWindow
class vet_db:
    DB_PATH = 'MainDatabaseVet'
    TABLE_ROW_LIMIT = 10
    vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.setWindowTitle("Система учёта животных домашних хозяйств Build 1000-7")
    #border verh


    #border niz
    sys.exit(app.exec())

