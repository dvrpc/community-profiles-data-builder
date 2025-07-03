ACS_VARIABLES = {
    # DEMOGRAPHICS
    # ---- Demographic Summary
    "B01003_001E": "total_pop",  # Total Population
    "B01001_002E": "male_pop",  # Male population
    "B01001_026E": "female_pop",  # Female population
    "B01002_001E": "median_age",  # Median age
    "B05003_003E": "under_18_pop",  # Under 18 yrs age
    "B26108_010E": "65_over_pop",  # Population 65 years and over

    # ---- Race
    "B03002_003E": "white_alone_pop",  # White alone population
    "B03002_004E": "black_alone_pop", # Black or African American alone pop
    "B03002_005E": "am_indian_alone_pop", # American Indian and Alaska Native alone
    "B03002_006E": "asian_alone_pop", # Asian alone
    "B03002_007E": "haw_pac_alone_pop", # Native Hawaiian and Other Pacific Islander alone
    "B03002_008E": "other_alone_pop", # Some other race alone
    "B02008_001E": "white_alone_pop",  # White alone or in Combination With One or More Other Races
    "B02009_001E": "black_alone_pop", # Black or African American alone or in Combination With One or More Other Races
    "B02010_001E": "am_indian_alone_pop", # American Indian and Alaska Native alone or in Combination With One or More Other Races
    "B02011_001E": "asian_alone_pop", # Asian alone or in Combination With One or More Other Races
    "B02012_001E": "haw_pac_alone_pop", # Native Hawaiian and Other Pacific Islander alone or in Combination With One or More Other Races
    "B02013_001E": "other_alone_pop", # Some other race alone or in Combination With One or More Other Races

    # ECONOMIC
    # ---- Economic Summary
    "B11001_001E": "total_hh",  # Total Households
    "B19013_001E": "median_hh_inc",  # Median Household Income
    "B19113_001E": "median_family_inc", # Median Family Income
    "B19301_001E": "median_inc",  # Median Income (Per Capita Income)
    "B17001_002E": "pov_level",  # Below poverty level
    "B23025_002E": "labor_force", # Over 16 in labor force

    # ---- Commute
    "B08006_002E": "comm_drive", # Over 16 drove to work
    "B08006_003E": "comm_drive_alone", # Over 16 drove to work
    "B08006_004E": "comm_pool", # Over 16 carpooled to work
    "B08006_008E": "comm_trans", # Over 16 took public transit to work
    "B08006_009E": "comm_bus", # Over 16 took the bus to work
    "B08006_010E": "comm_subway", # Over 16 took subway or elevated rail to work
    "B08006_011E": "comm_rail", # Over 16 took commuter rail to work
    "B08006_012E": "comm_light_rail", # Over 16 light rail / street car to work
    "B08006_013E": "comm_ferry", # Over 16 took ferry to work
    "B08006_015E": "comm_walk", # Over 16 drove to work
    "B08006_014E": "comm_bike", # Over 16 drove to work
    "B08006_016E": "comm_taxi_motor_other", # Taxi, motorcycle, or other
    "B08006_017E": "wfh" # Worked from home

}
ACS_VARIABLES_FORMATTED = ','.join([*ACS_VARIABLES])

ACS_SUBJECT_VARIABLES = {
        # ---- Age
    "S0101_C01_002E": "under_5_pop", # Under 5 years 
    "S0101_C01_003E": "5_to_9_pop", # 5 to 9 years 
    "S0101_C01_004E": "10_to_14_pop", # 10 to 4 years 
    "S0101_C01_005E": "15_to_19_pop", # 15 to 19 years 
    "S0101_C01_006E": "20_to_24_pop", # 20 to 24 years 
    "S0101_C01_007E": "25_to_29_pop", # 25 to 29 years 
    "S0101_C01_008E": "30_to_34_pop", # 30 to 34 years 
    "S0101_C01_009E": "35_to_39_pop", # 35 to 39 years 
    "S0101_C01_010E": "40_to_44_pop", # 40 to 44 years 
    "S0101_C01_011E": "45_to_49_pop", # 45 to 49 years 
    "S0101_C01_012E": "50_to_54_pop", # 50 to 54 years 
    "S0101_C01_013E": "55_to_59_pop", # 55 to 59 years 
    "S0101_C01_014E": "60_to_64_pop", # 60 to 64 years 
    "S0101_C01_015E": "65_to_69_pop", # 65 to 69 years 
    "S0101_C01_016E": "70_to_74_pop", # 70 to 74 years 
    "S0101_C01_017E": "75_to_79_pop", # 75 to 79 years 
    "S0101_C01_018E": "80_to_84_pop", # 80 to 84 years 
    "S0101_C01_019E": "85_over_pop", # 85 to 9 years

    # ECONOMIC
    "S1701_C01_002E": "under_18_pov_level", # Under 18 below poverty level
    "S1701_C01_010E": "over_65_pov_level", # Over 65 below poverty level
    "S1901_C01_013E": "mean_hh_inc", # mean household income
    "S1901_C02_013E": "mean_family_inc", # mean family income
    

}
ACS_SUBJECT_VARIABLES_FORMATTED = ','.join([*ACS_SUBJECT_VARIABLES])


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
