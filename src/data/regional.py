import logging
import math
import numpy as np
import pandas as pd
from src.db.database import get_write_engine
from .consts import ALL_VARIABLES_COMBINED_VALUES

log = logging.getLogger(__name__)

excluded_variables = {
    "geoid",
    "state",
    "county",
    "co_name",
    "buffer_bbox"
}

non_aggregatable_variables = {
    "median_age",
    "median_age_moe",
    "median_hh_inc",
    "median_hh_inc_moe",
    "median_family_inc",
    "median_family_inc_moe",
    "median_inc",
    "median_inc_moe",
    "mean_family_inc",
    "mean_family_inc_moe",
    "avg_family_size",
    "avg_family_size_moe",
    "avg_hh_size",
    "avg_hh_size_moe",
    "pct_ev_ldv",
    "pct_change_ev",
    "pct_change_ldv"
    "emppct50",
    "poppct50",


}

def get_county_data():
    log.info('Fetching county data...')
    engine = get_write_engine()
    try:
        county_data = pd.read_sql("SELECT * FROM county", engine)
        log.info('Succesfully fetched county data')

    except Exception as e:
        log.error('Error fetching county data')

    engine.dispose()
    return county_data


def aggregate_data(county_data: pd.DataFrame):
    aggregate_data = {}
    for variable in ALL_VARIABLES_COMBINED_VALUES:
        # summable_variables = ALL_VARIABLES_COMBINED_VALUES.copy()
        
        # for v in summable_variables:
        #     if v in excluded_variables.union(non_aggregatable_variables):
        #         summable_variables.pop(v, None)
                
        if variable not in excluded_variables.union(non_aggregatable_variables):
            if("moe" in variable):
                if(not (county_data[variable] == -555555555).any()):
                    aggregate_data[variable] = np.sqrt((county_data[variable]**2).sum())
                else:
                    print(variable)
            else:
                aggregate_data[variable] = county_data[variable].sum()


    return pd.DataFrame([aggregate_data])


def average_data(county_data):
    pass


