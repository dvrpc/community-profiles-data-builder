from dotenv import load_dotenv
from .const import ACS_VARIABLES, ACS_VARIABLES_FORMATTED, PA_FIPS, PA_FIPS_FORMATTED, NJ_FIPS, NJ_FIPS_FORMATTED, STATE_FIPS
import requests
import os
import logging
import pandas as pd

log = logging.getLogger(__name__)
load_dotenv()
# https://api.census.gov/data/2023/acs/acs5?get=B01003_001E,B11001_001E,B19301_001E,B19013_001E,B17001_002E,B01002_001E,NAME&for=county:101,017,029,091,045&key=c79da1491746793c632c4302fedc42a637fad023&in=state:42
# https://api.census.gov/data/2023/acs/acs5?get=NAME,B01003_001E&in=state:42&for=place:*


API_KEY = os.getenv("CENSUS_API_KEY")


def format_fields(values):
    return {
        "name"
        "total_pop": values[0],
        "total_hh": values[1],
        "med_inc": values[2],
        "med_inc_hh": values[3],
        "below_pov": values[4],
        "med_age": values[5],
    }


def get_tract_data(geoid: int):
    url = f"https://api.census.gov/data/2023/acs/acs5?get={ACS_VARIABLES_FORMATTED}&ucgid=1400000US{geoid}&key={API_KEY}"

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        log.error(
            f"Failed to fetch ACS tract data for {geoid}: {e.response.text}")

    return format_fields(r.json()[1])


def get_muni_data():

    def fetch_data(county_codes, state_code):
        url = f"https://api.census.gov/data/2023/acs/acs5?get={ACS_VARIABLES_FORMATTED},NAME&for=county%20subdivision:*&in=county:{county_codes}&in=state:{state_code}&key={API_KEY}"
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            log.error(
                f"Failed to fetch ACS county data for {state_code}: {county_codes}: {e.response.text}")

        return r.json()

    pa_data = fetch_data(PA_FIPS_FORMATTED, 42)
    nj_data = fetch_data(NJ_FIPS_FORMATTED, 34)
    combined_data = pa_data[1:] + nj_data[1:]

    columns = []
    for field in pa_data[0]:
        if field in ACS_VARIABLES:
            columns.append(ACS_VARIABLES[field])
        else:
            columns.append(field)

    df = pd.DataFrame(combined_data, columns=columns)
    df['geoid'] = df['state'] + df['county'] + df['county subdivision']
    df['state'].replace(STATE_FIPS, inplace=True)
    df['county'].replace(PA_FIPS | NJ_FIPS, inplace=True)
    df['mun_name'] = df['NAME'].str.split(',').str[0].str.title()

    df_cols = df.columns.to_list()
    reordered_cols = ['geoid', 'mun_name', 'county', 'state'] + df_cols[:-6]
    return df[reordered_cols]


def get_county_data():

    def fetch_data(county_codes, state_code):
        url = f"https://api.census.gov/data/2023/acs/acs5?get={ACS_VARIABLES_FORMATTED}&for=county:{county_codes}&in=state:{state_code}&key={API_KEY}"
        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            log.error(
                f"Failed to fetch ACS county data for {state_code}: {county_codes}: {e.response.text}")

        return r.json()

    pa_data = fetch_data(PA_FIPS_FORMATTED, 42)
    nj_data = fetch_data(NJ_FIPS_FORMATTED, 34)
    combined_data = pa_data[1:] + nj_data[1:]

    columns = []
    for field in pa_data[0]:
        if field in ACS_VARIABLES:
            columns.append(ACS_VARIABLES[field])
        else:
            columns.append(field)

    df = pd.DataFrame(combined_data, columns=columns)
    df['fips'] = df['state'] + df['county']
    df['state'].replace(STATE_FIPS, inplace=True)
    df['county'].replace(PA_FIPS | NJ_FIPS, inplace=True)

    df_cols = df.columns.to_list()
    reordered_cols = ['fips', 'county', 'state'] + df_cols[:-3]
    return df[reordered_cols]
