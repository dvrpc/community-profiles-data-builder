from .data import acs


def exec():
    build_county_data()
    build_muni_data()
    pass


def build_county_data():
    # Fetch ACS data
    acs_data = acs.get_county_data()
    print(acs_data)
    # Fetch GIS data

    # Fetch CKAN data

    # Construct table

    # Save to db
    pass


def build_muni_data():
    # Fetch ACS data
    acs_data = acs.get_muni_data()
    print(acs_data)
    # Fetch GIS data

    # Fetch CKAN data

    # Construct table

    # Save to db
    pass
