import pandas as pd
from sqlalchemy import text, create_engine

DB_PATH           = 'MainDatabaseVet'  # bezvremennoe reshenie
vet_db_connection = create_engine(f'sqlite:///{DB_PATH}').connect()


def db_get_city_name(city):
    return pd.read_sql(f'''SELECT name from city WHERE city.pk = {city}''',vet_db_connection).iloc[0]['name']
def db_get_settlement(settlement):
    return pd.read_sql(f'''SELECT name from settlement WHERE settlement.pk = {settlement}''',vet_db_connection).iloc[0]['name']
def db_get_owner(household):
    return pd.read_sql(f'''SELECT owner, address from household WHERE household.pk = {household}''',vet_db_connection)[['owner', 'address']].iloc[0].to_dict()