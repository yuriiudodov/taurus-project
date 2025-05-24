import pandas as pd
from PySide6.QtWidgets import QTableWidgetItem
from sqlalchemy import text, create_engine
import settings
DB_PATH           = settings.DB_PATH  # bezvremennoe reshenie
vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()


def refresh_table(tablewidget, tablename):
    vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()
    data_for_table = pd.read_sql(text(f'SELECT * FROM {tablename}'), vet_db_connection).astype(str)
    print(data_for_table)
    tablewidget.setColumnCount(len(data_for_table.columns))
    tablewidget.setRowCount(len(data_for_table))

    for col_num in range(len(data_for_table.columns)):
        for row_num in range(0, len(data_for_table)):
            tablewidget.setItem(row_num, col_num,
                                QTableWidgetItem(data_for_table.iloc[row_num, col_num]))
def db_get_city_name(city):
    return pd.read_sql(f'''SELECT name from city WHERE city.pk = {city}''',vet_db_connection).iloc[0]['name']
def db_get_settlement(settlement):
    return pd.read_sql(f'''SELECT name from settlement WHERE settlement.pk = {settlement}''',vet_db_connection).iloc[0]['name']
def db_get_owner(household):
    return pd.read_sql(f'''SELECT owner, address from household WHERE household.pk = {household}''',vet_db_connection)[['owner', 'address']].iloc[0].to_dict()
