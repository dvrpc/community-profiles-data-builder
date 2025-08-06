from .data import acs, gis, ckan
from .db.database import get_write_engine
import pandas as pd
import functools as ft
import logging

log = logging.getLogger(__name__)

def exec():
    # build_county_data()
    build_muni_data()
    pass

def save_data(df: pd.DataFrame, table):
    engine = get_write_engine()
    try:
        df.to_sql(table, engine, if_exists='replace', index=False)
        log.info(f"Succesfully wrote Dataframe to {table} table")
    except Exception as e:
        log.error(f'Error writing Dataframe to {table} table: {e}')
    

def build_county_data():
    acs_data = acs.get_county_data()
    gis_data = gis.get_county_data()
    ckan_data = ckan.get_county_data()
    
    dfs = [acs_data, gis_data, ckan_data]
    df_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='fips'), dfs)
    
    save_data(df_merged, 'county')


def build_muni_data():
    acs_data = acs.get_muni_data()
    gis_data = gis.get_muni_data()
    ckan_data = ckan.get_muni_data()
    
    dfs = [acs_data, gis_data, ckan_data]
    df_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='geoid', how='left'), dfs)
    
    save_data(df_merged, 'municipality')
