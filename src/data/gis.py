from ..db.database import get_engine
import logging
import os
import pandas as pd
from sqlalchemy.exc import OperationalError, ProgrammingError

dirname = os.path.dirname(__file__)
log = logging.getLogger(__name__)

def fetch_sql(file):
    engine = get_engine()
    file_path = os.path.join(dirname, f'sql/{file}.sql')

    try:   
        df = pd.read_sql_query(open(file_path, "r").read(), engine)
        return df
    except (OperationalError, ProgrammingError) as err:
        log.error(f"Error executing: \n{file}.sql: \n{err}")


def get_county_layers():
    print(fetch_sql("county"))


