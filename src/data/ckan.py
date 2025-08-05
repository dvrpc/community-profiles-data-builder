import requests
import logging
import pandas as pd
import os
import functools as ft

from dotenv import load_dotenv

log = logging.getLogger(__name__)
load_dotenv()

dirname = os.path.dirname(__file__)

def fetch_datastore(file, geo):
    file_path = os.path.join(dirname, f'sql/datastore/{geo}/{file}.sql')
    query = open(file_path, "r").read()
    
    url = "https://catalog.dvrpc.org/api/3/action/datastore_search_sql?sql=" + query
    try:
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()['result']['records']
        return pd.DataFrame(data)

    except requests.exceptions.HTTPError as e:
        log.error(
            f"Failed to fetch {file} datastore for {geo}:\n {e}")
    

def get_county_data():
    pavement_conditions = fetch_datastore('pavement_conditions', 'county')
    bridge_conditions = fetch_datastore('bridge_conditions', 'county')
    electric_vehicles = fetch_datastore('electric_vehicles', 'county')
    housing_affordability = fetch_datastore('housing_affordability', 'county')
    
    dfs = [pavement_conditions, bridge_conditions, electric_vehicles, housing_affordability]
    county_merged = ft.reduce(lambda left, right: pd.merge(
        left, right, on='fips'), dfs)
    return county_merged
