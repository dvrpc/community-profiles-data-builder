ACS_VARIABLES = {
    # DEMOGRAPHICS
    # ---- Demographic Summary
    "B01003_001E": "total_pop",  # Total Population
    "B01001_002E": "male_pop",  # Male population
    "B01001_026E": "female_pop",  # Female population
    "B01002_001E": "median_age",  # Median age
    "B05003_003E": "18_pop",  # Under 18 yrs age
    "B26108_010E": "65_pop",  # Population 65 years and over

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
    "B08006_017E": "wfh", # Worked from home

    # ---- Sex by employment status, required addition
    "B23001_005E": "male_armed_forces_16_19", # Male armed_forces - 16-19
    "B23001_012E": "male_armed_forces_20_21", # Male armed_forces - 20-21 
    "B23001_019E": "male_armed_forces_22_24", # Male armed_forces - 22-24
    "B23001_026E": "male_armed_forces_25_29", # Male armed_forces - 25-29
    "B23001_033E": "male_armed_forces_30_34", # Male armed_forces - 30-34
    "B23001_040E": "male_armed_forces_35_44", # Male armed_forces - 35-44
    "B23001_047E": "male_armed_forces_45_54", # Male armed_forces - 45-54
    "B23001_054E": "male_armed_forces_55_59", # Male armed_forces - 55-59
    "B23001_061E": "male_armed_forces_60_61", # Male armed_forces - 60-61
    "B23001_068E": "male_armed_forces_62_64", # Male armed_forces - 62-64

    "B23001_007E": "male_employed_16_19", # Male employed - 16-19
    "B23001_014E": "male_employed_20_21", # Male employed - 20-21 
    "B23001_021E": "male_employed_22_24", # Male employed - 22-24
    "B23001_028E": "male_employed_25_29", # Male employed - 25-29
    "B23001_035E": "male_employed_30_34", # Male employed - 30-34
    "B23001_042E": "male_employed_35_44", # Male employed - 35-44
    "B23001_049E": "male_employed_45_54", # Male employed - 45-54
    "B23001_056E": "male_employed_55_59", # Male employed - 55-59
    "B23001_063E": "male_employed_60_61", # Male employed - 60-61
    "B23001_070E": "male_employed_62_64", # Male employed - 62-64
    "B23001_075E": "male_employed_65_69", # Male employed - 65-69
    "B23001_080E": "male_employed_70_74", # Male employed - 70-74
    "B23001_085E": "male_employed_75", # Male employed - 75+

    "B23001_008E": "male_unemployed_16_19", # Male unemployed - 16-19
    "B23001_015E": "male_unemployed_20_21", # Male unemployed - 20-21 
    "B23001_022E": "male_unemployed_22_24", # Male unemployed - 22-24
    "B23001_029E": "male_unemployed_25_29", # Male unemployed - 25-29
    "B23001_036E": "male_unemployed_30_34", # Male unemployed - 30-34
    "B23001_043E": "male_unemployed_35_44", # Male unemployed - 35-44
    "B23001_050E": "male_unemployed_45_54", # Male unemployed - 45-54
    "B23001_057E": "male_unemployed_55_59", # Male unemployed - 55-59
    "B23001_064E": "male_unemployed_60_61", # Male unemployed - 60-61
    "B23001_071E": "male_unemployed_62_64", # Male unemployed - 62-64
    "B23001_076E": "male_unemployed_65_69", # Male unemployed - 65-69
    "B23001_081E": "male_unemployed_70_74", # Male unemployed - 70-74
    "B23001_086E": "male_unemployed_75", # Male unemployed - 75+

    "B23001_009E": "male_not_in_labor_force_16_19", # Male not_in_labor_force - 16-19
    "B23001_016E": "male_not_in_labor_force_20_21", # Male not_in_labor_force - 20-21 
    "B23001_023E": "male_not_in_labor_force_22_24", # Male not_in_labor_force - 22-24
    "B23001_030E": "male_not_in_labor_force_25_29", # Male not_in_labor_force - 25-29
    "B23001_037E": "male_not_in_labor_force_30_34", # Male not_in_labor_force - 30-34
    "B23001_044E": "male_not_in_labor_force_35_44", # Male not_in_labor_force - 35-44
    "B23001_051E": "male_not_in_labor_force_45_54", # Male not_in_labor_force - 45-54
    "B23001_058E": "male_not_in_labor_force_55_59", # Male not_in_labor_force - 55-59
    "B23001_065E": "male_not_in_labor_force_60_61", # Male not_in_labor_force - 60-61
    "B23001_072E": "male_not_in_labor_force_62_64", # Male not_in_labor_force - 62-64
    "B23001_077E": "male_not_in_labor_force_65_69", # Male not_in_labor_force - 65-69
    "B23001_082E": "male_not_in_labor_force_70_74", # Male not_in_labor_force - 70-74
    "B23001_087E": "male_not_in_labor_force_75", # Male not_in_labor_force - 75+

    "B23001_091E": "female_armed_forces_16_19", # female armed_forces - 16-19
    "B23001_098E": "female_armed_forces_20_21", # female armed_forces - 20-21 
    "B23001_105E": "female_armed_forces_22_24", # female armed_forces - 22-24
    "B23001_112E": "female_armed_forces_25_29", # female armed_forces - 25-29
    "B23001_119E": "female_armed_forces_30_34", # female armed_forces - 30-34
    "B23001_126E": "female_armed_forces_35_44", # female armed_forces - 35-44
    "B23001_133E": "female_armed_forces_45_54", # female armed_forces - 45-54
    "B23001_140E": "female_armed_forces_55_59", # female armed_forces - 55-59
    "B23001_147E": "female_armed_forces_60_61", # female armed_forces - 60-61
    "B23001_153E": "female_armed_forces_62_64", # female armed_forces - 62-64

    "B23001_093E": "female_employed_16_19", # female employed - 16-19
    "B23001_100E": "female_employed_20_21", # female employed - 20-21 
    "B23001_107E": "female_employed_22_24", # female employed - 22-24
    "B23001_114E": "female_employed_25_29", # female employed - 25-29
    "B23001_121E": "female_employed_30_34", # female employed - 30-34
    "B23001_128E": "female_employed_35_44", # female employed - 35-44
    "B23001_135E": "female_employed_45_54", # female employed - 45-54
    "B23001_142E": "female_employed_55_59", # female employed - 55-59
    "B23001_149E": "female_employed_60_61", # female employed - 60-61
    "B23001_156E": "female_employed_62_64", # female employed - 62-64
    "B23001_161E": "female_employed_65_69", # female employed - 65-69
    "B23001_166E": "female_employed_70_74", # female employed - 70-74
    "B23001_171E": "female_employed_75", # female employed - 75+

    "B23001_094E": "female_unemployed_16_19", # female unemployed - 16-19
    "B23001_101E": "female_unemployed_20_21", # female unemployed - 20-21 
    "B23001_108E": "female_unemployed_22_24", # female unemployed - 22-24
    "B23001_115E": "female_unemployed_25_29", # female unemployed - 25-29
    "B23001_122E": "female_unemployed_30_34", # female unemployed - 30-34
    "B23001_129E": "female_unemployed_35_44", # female unemployed - 35-44
    "B23001_136E": "female_unemployed_45_54", # female unemployed - 45-54
    "B23001_143E": "female_unemployed_55_59", # female unemployed - 55-59
    "B23001_150E": "female_unemployed_60_61", # female unemployed - 60-61
    "B23001_157E": "female_unemployed_62_64", # female unemployed - 62-64
    "B23001_162E": "female_unemployed_65_69", # female unemployed - 65-69
    "B23001_167E": "female_unemployed_70_74", # female unemployed - 70-74
    "B23001_172E": "female_unemployed_75", # female unemployed - 75+

    "B23001_095E": "female_not_in_labor_force_16_19", # female not_in_labor_force - 16-19
    "B23001_102E": "female_not_in_labor_force_20_21", # female not_in_labor_force - 20-21 
    "B23001_109E": "female_not_in_labor_force_22_24", # female not_in_labor_force - 22-24
    "B23001_116E": "female_not_in_labor_force_25_29", # female not_in_labor_force - 25-29
    "B23001_123E": "female_not_in_labor_force_30_34", # female not_in_labor_force - 30-34
    "B23001_130E": "female_not_in_labor_force_35_44", # female not_in_labor_force - 35-44
    "B23001_137E": "female_not_in_labor_force_45_54", # female not_in_labor_force - 45-54
    "B23001_144E": "female_not_in_labor_force_55_59", # female not_in_labor_force - 55-59
    "B23001_151E": "female_not_in_labor_force_60_61", # female not_in_labor_force - 60-61
    "B23001_158E": "female_not_in_labor_force_62_64", # female not_in_labor_force - 62-64
    "B23001_163E": "female_not_in_labor_force_65_69", # female not_in_labor_force - 65-69
    "B23001_168E": "female_not_in_labor_force_70_74", # female not_in_labor_force - 70-74
    "B23001_173E": "female_not_in_labor_force_75", # female not_in_labor_force - 75+

    # ---- Household Income
    "B19001_002E": "hh_inc_10k", # Household Income Less than $10,0000
    "B19001_003E": "hh_inc_10k_15k", # Household Income $10,000 to $14,999
    "B19001_004E": "hh_inc_15k_20k", # Household Income $15,000 to $19,999
    "B19001_005E": "hh_inc_20k_25k", # Household Income $20,000 to $24,999
    "B19001_006E": "hh_inc_25k_30k", # Household Income $25,000 to $29,999
    "B19001_007E": "hh_inc_30k_35k", # Household Income $30,000 to $34,999
    "B19001_008E": "hh_inc_35k_40k", # Household Income $35,000 to $39,999
    "B19001_009E": "hh_inc_40k_45k", # Household Income $40,000 to $44,999
    "B19001_010E": "hh_inc_45k_50k", # Household Income $45,000 to $49,999
    "B19001_011E": "hh_inc_50k_60k", # Household Income $50,000 to $59,999
    "B19001_012E": "hh_inc_60k_75k", # Household Income $60,000 to $74,999
    "B19001_013E": "hh_inc_75k_100k", # Household Income $75,000 to $99,999
    "B19001_014E": "hh_inc_100k_125k", # Household Income $100,000 to $124,999
    "B19001_015E": "hh_inc_125k_150k", # Household Income $120,000 to $149,999
    "B19001_016E": "hh_inc_150k_200k", # Household Income $150,000 to $199,999
    "B19001_017E": "hh_inc_200k", # Household Income $200,000 and more

    # ---- Vehicle Availability
    "B25044_003E": "owner_no_vehicle", # Owner occupied, no vehicle
    "B25044_004E": "owner_1_vehicle", # Owner occupied, 1 vehicle
    "B25044_005E": "owner_2_vehicle", # Owner occupied, 2 vehicles
    "B25044_006E": "owner_3_vehicle", # Owner occupied, 3 vehicles
    "B25044_007E": "owner_4_vehicle", # Owner occupied, 4 vehicles
    "B25044_008E": "owner_5_vehicle", # Owner occupied, 5+ vehicles
    "B25044_010E": "renter_no_vehicle", # renter occupied, no vehicle
    "B25044_011E": "renter_1_vehicle", # renter occupied, 1 vehicle
    "B25044_012E": "renter_2_vehicle", # renter occupied, 2 vehicles
    "B25044_013E": "renter_3_vehicle", # renter occupied, 3 vehicles
    "B25044_014E": "renter_4_vehicle", # renter occupied, 4 vehicles
    "B25044_015E": "renter_5_vehicle", # renter occupied, 5+ vehicles

    # ---- Social Summary
    "B11001_002E": "family_hh", # family households
    "B11001_007E": "nonfamily_hh", # nonfamily households
    "B25010_001E": "avg_hh_size", # average household size

    # ---- Educational Attainment
    "B06009_002E": "less_hs", # Less than a high school graduate
    "B06009_003E": "hs_no_college", # High school graduate (includes equivalency)
    "B06009_004E": "some_college", # Some college or associate's degree
    "B06009_005E": "bachelors_degree", # Bachelor's degree
    "B06009_006E": "graduate_degree", # Graduate or professional degree

}

GROUPED_ACS_VARIABLES = [ACS_VARIABLES[i:i + 50] for i in range(0, len(ACS_VARIABLES), 50)]

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
    # ---- Economic Summary
    "S1701_C01_002E": "under_18_pov_level", # Under 18 below poverty level
    "S1701_C01_010E": "over_65_pov_level", # Over 65 below poverty level
    "S1901_C01_013E": "mean_hh_inc", # mean household income
    "S1901_C02_013E": "mean_family_inc", # mean family income

    # ---- Social Summary
    "S1101_C01_004E": "avg_family_size", #average family size
    

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
