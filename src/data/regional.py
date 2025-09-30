import logging
import math
import pandas as pd
from src.db.database import get_write_engine
from .consts import ALL_VARIABLES_COMBINED_VALUES, non_aggregatable_variables

log = logging.getLogger(__name__)

excluded_variables = {
    "geoid",
    "state",
    "county",
    "co_name",
    "buffer_bbox"
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
    aggregate_data = pd.DataFrame()

    for variable in ALL_VARIABLES_COMBINED_VALUES:
        if variable not in excluded_variables.union(non_aggregatable_variables):
            aggregate_data[variable] = county_data[variable].sum()

            moe_variable = f"${variable}_moe"

            try:
                aggregate_data[moe_variable] = sum_moe(
                    county_data[moe_variable].to_list())
            except KeyError:
                log.info(f"${moe_variable} not present in database")

    return aggregate_data


def average_data(county_data):
    pass


def sum_moe(county_moe):
    sum_square = [moe ** 2 for moe in county_moe]
    return math.sqrt(sum_square)
