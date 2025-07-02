ACS_VARIABLES = {
    "B01003_001E": "total_pop",  # Total Population
    "B11001_001E": "total_hh",  # Total Households
    "B19301_001E": "median_inc",  # Median Income (Per Capita Income)
    "B19013_001E": "median_hh_inc",  # Median Household Income
    "B17001_002E": "median_pov_level",  # Below poverty level
    "B01002_001E": "median_age"  # Median age
}
ACS_VARIABLES_FORMATTED = ','.join([*ACS_VARIABLES])

PA_FIPS = {
    "017": "Bucks",
    "029": "Chester",
    "045": "Delaware",
    "091": "Montgomery",
    "101": "Philadelphia"
}
PA_FIPS_FORMATTED = ','.join(*[PA_FIPS])

NJ_FIPS = {
    "005": "Burlington",
    "007": "Camden",
    "015": "Gloucester",
    "021": "Mercer",
}
NJ_FIPS_FORMATTED = ','.join(*[NJ_FIPS])

STATE_FIPS = {
    "34": "New Jersey",
    "42": "Pennsylvania"
}
