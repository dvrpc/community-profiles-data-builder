from .data import acs, gis, ckan


def exec():
    build_county_data()
    # build_muni_data()
    pass


def build_county_data():
    # Fetch ACS data
    # acs_data = acs.get_county_data()
    # print(acs_data)
    # Fetch GIS data
    gis_data = gis.get_county_layers()
    print(gis_data)
    # Fetch CKAN data
    ckan_data = ckan.get_county_data()
    print(ckan_data)
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
