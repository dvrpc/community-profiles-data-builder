from ..db.database import get_gis_engine
import logging
import os
import pandas as pd
import functools as ft
from sqlalchemy.exc import OperationalError, ProgrammingError

dirname = os.path.dirname(__file__)
log = logging.getLogger(__name__)


def fetch_sql(file, geo):
    engine = get_gis_engine()
    file_path = os.path.join(dirname, f'sql/gis/{geo}/{file}.sql')

    try:
        df = pd.read_sql_query(open(file_path, "r").read(), engine)
        return df
    except (OperationalError, ProgrammingError) as err:
        log.error(f"Error executing: \n{file}.sql: \n{err}")


def get_county_layers():
    spatial = fetch_sql("spatial", "county")
    pop_emp_forecasts = fetch_sql("pop_emp_forecasts", "county")
    land_use = fetch_sql("land_use", "county")

    dfs = [spatial, pop_emp_forecasts, land_use]
    county_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='fips'), dfs)
    return county_merged
