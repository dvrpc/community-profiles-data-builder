## community-profiles-data-builder

CRON service to build community profile data layers

# Setup

1. Activate venv

```
python -m venv .venv
source .venv/bin/activate
# Windows .venv\Scripts\activate
```

2. Install requirements `pip install -r requirements.txt`
3. Create a local postgres DB
4. Get a [census api token](https://api.census.gov/data/key_signup.html) to place in .env in next step
5. Create .env file and fill contents from env_sample. GIS_DB refers to the DVRPC GIS Postgres DB, WRITE_DB refers to your newly created local postgres DB
6. Run app

```
python run.py
```

This will take some time to build, primarily because of large spatial queries.

Sample test data
muni = 4201704976
county = 42101
