from .data import acs, gis, ckan, regional
from .db.database import get_write_engine
import pandas as pd
import functools as ft
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def exec():
    # build_county_data()
    # build_muni_data()
    build_regional_data()


def save_data(df: pd.DataFrame, table):
    log.info(f'Wrting dataframe to {table} table')
    engine = get_write_engine()
    try:
        df.to_sql(table, engine, if_exists='replace', index=False)
        log.info(f"Succesfully wrote Dataframe to {table} table")
    except Exception as e:
        log.error(f'Error writing Dataframe to {table} table: {e}')

    engine.dispose()


def to_numeric(s):
    try:
        return pd.to_numeric(s, errors='raise')
    except ValueError:
        return s


def build_county_data():
    acs_data = acs.get_county_data()
    gis_data = gis.get_county_data()
    ckan_data = ckan.get_county_data()

    dfs = [acs_data, gis_data, ckan_data]
    df_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='fips'), dfs)

    excluded_columns = ['fips', 'state', 'county', 'co_name', 'buffer_bbox']
    columns_to_update = [
        col for col in df_merged.columns if col not in excluded_columns]
    df_merged[columns_to_update] = df_merged[columns_to_update].apply(
        pd.to_numeric)

    df_merged = df_merged.rename(columns={'fips': 'geoid'})
    save_data(df_merged, 'county')


def build_muni_data():
    acs_data = acs.get_muni_data()
    gis_data = gis.get_muni_data()
    ckan_data = ckan.get_muni_data()

    dfs = [acs_data, gis_data, ckan_data]
    df_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='geoid', how='left'), dfs)

    excluded_columns = ['geoid', 'state', 'county', 'mun_name', 'buffer_bbox']
    columns_to_update = [
        col for col in df_merged.columns if col not in excluded_columns]
    df_merged[columns_to_update] = df_merged[columns_to_update].apply(
        to_numeric)

    save_data(df_merged, 'municipality')


def build_regional_data():
    county_data = regional.get_profile_data("SELECT * FROM county", "all county data")

    # Aggregates summable fields and margin of error
    regional_data = regional.aggregate_data(county_data)

    save_data(regional_data, 'region')

    # Averages median/mean/pct fields and margin of error
    # county_data = regional.average_data(county_data)

    # save to db
