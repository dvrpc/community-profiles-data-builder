from dotenv import load_dotenv
from sqlalchemy import create_engine
import logging
import os

host = os.getenv("DB_HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
port = os.getenv("DB_PORT")

log = logging.getLogger(__name__)
load_dotenv()

def get_engine():
    return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
