from dotenv import load_dotenv
from .consts import GROUPED_ACS_VARIABLES, GROUPED_ACS_SUBJECT_VARIABLES, PA_FIPS, PA_FIPS_FORMATTED, NJ_FIPS, NJ_FIPS_FORMATTED, STATE_FIPS, ACS_VARIABLES_COMBINED, ACS_SUBJECT_VARIABLE_KEYS
import requests
import os
import logging
import pandas as pd

log = logging.getLogger(__name__)
load_dotenv()

API_KEY = os.getenv("CENSUS_API_KEY")


def fetch_data(variable_group, county_codes, state_code, geo, is_subject):
    formatted_variables = ','.join([*variable_group])

    url = ''
    if geo == 'county':
        url = f"https://api.census.gov/data/2023/acs/acs5{'/subject' if is_subject else ''}?get={formatted_variables}&for=county:{county_codes}&in=state:{state_code}&key={API_KEY}"
    else:
        url = f"https://api.census.gov/data/2023/acs/acs5{'/subject' if is_subject else ''}?get={formatted_variables},NAME&for=county%20subdivision:*&in=county:{county_codes}&in=state:{state_code}&key={API_KEY}"

    try:
        r = requests.get(url)
        r.raise_for_status()

    except requests.exceptions.HTTPError as e:
        log.error(
            f"Failed to fetch ACS {geo} data for {state_code}: {county_codes}: {e.response.text}")

    return r.json()


def get_mapped_columns(columns):
    output_columns = []
    for field in columns:
        if field in ACS_VARIABLES_COMBINED:
            output_columns.append(ACS_VARIABLES_COMBINED[field])
        else:
            output_columns.append(field)
    return output_columns


def build_dataframe(variable_group, first, geo, is_subject=False):

    def clean_muni_dataframe(df):
        df['geoid'] = df['state'] + df['county'] + df['county subdivision']

        if (first):
            df['state'] = df['state'].replace(STATE_FIPS)
            df['county'] = df['county'].replace(PA_FIPS | NJ_FIPS)
            df['mun_name'] = df['NAME'].str.split(',').str[0].str.title()
            df = df.drop(columns=['NAME', 'county subdivision'], axis=1)

        else:
            df = df.drop(columns=['state', 'county',
                         'NAME', 'county subdivision'], axis=1)

        return df

    def clean_county_dataframe(df):
        df['fips'] = df['state'] + df['county']

        if (first):
            df['state'] = df['state'].replace(STATE_FIPS)
            df['county'] = df['county'].replace(PA_FIPS | NJ_FIPS)
        else:
            df = df.drop(columns=['state', 'county'], axis=1)

        return df

    pa_data = fetch_data(
        variable_group, PA_FIPS_FORMATTED, 42, geo, is_subject)
    nj_data = fetch_data(
        variable_group, NJ_FIPS_FORMATTED, 34, geo, is_subject)

    combined_data = pa_data[1:] + nj_data[1:]

    columns = get_mapped_columns(pa_data[0])
    df = pd.DataFrame(combined_data, columns=columns)

    if geo == 'county':
        df = clean_county_dataframe(df)
    else:
        df = clean_muni_dataframe(df)

    return df


def aggregate_dataframes(merge_key, geo):
    data = pd.DataFrame()
    first = True

    # Necessary for ACS 50 variable limit
    def build_variable_group(variable_group, is_subject):
        nonlocal data
        nonlocal first

        for variable_group in variable_group:
            df = build_dataframe(variable_group, first, geo, is_subject)

            if (data.empty):
                data = df
                first = False
            else:
                data = data.merge(df, on=merge_key)
        return data

    build_variable_group(GROUPED_ACS_VARIABLES, is_subject=False)
    build_variable_group(GROUPED_ACS_SUBJECT_VARIABLES, is_subject=True)

    return data


def get_muni_data():
    log.info('Getting ACS municipality data...')
    muni_data = aggregate_dataframes('geoid', 'muni')
    cols_to_move = ['geoid', 'mun_name',
                    'county', 'state']
    muni_data = muni_data[cols_to_move +
                          [x for x in muni_data.columns if x not in cols_to_move]]
    log.info(f'Retrieved ACS data for {len(muni_data)} municipalities')
    return muni_data


def get_county_data():
    log.info('Getting ACS county data...')
    county_data = aggregate_dataframes('fips', 'county')
    cols_to_move = ['fips', 'state', 'county']
    county_data = county_data[cols_to_move +
                              [x for x in county_data.columns if x not in cols_to_move]]
    log.info(f'Retrieved ACS data for {len(county_data)} counties')
    return county_data
