from PySide6.QtWidgets import QTableWidgetItem
from sqlalchemy import create_engine
import pandas as pd


def get_data_db(self, table_name, db_connection):
    data = pd.read_sql(f'SELECT * FROM {table_name}', db_connection)
def vet_table_widget_fill(widget,DB_PATH, column_count):
    if DB_PATH=="default":
        DB_PATH="MainDatabaseVet"#vremennoe reshenie

    TABLE_ROW_LIMIT = 10
    vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()

    data_for_table=get_data_db( "city", vet_db_connection)
    data_for_table=pd.read_sql(f'SELECT * FROM city', vet_db_connection)
    widget.setColumnCount(column_count)
    widget.setRowCount(len(data_for_table))
    #display(data_for_table)
    for col_num in range(0,column_count-1):
        for row_num in range(0,len(data_for_table)):
           widget.setItem(row_num, col_num,QTableWidgetItem(data_for_table.iloc[row_num, col_num]))