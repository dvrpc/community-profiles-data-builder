from db.database import db
import logging
import psycopg

log = logging.getLogger(__name__)

def fetch_sql(query):
    cur = db.conn.cursor()
    
    response = None
    try:   
        cur.execute(query)
        response = cur.fetchall()
    except psycopg.OperationalError as err:
        log.error(f"Connection exception executing: \n{query} \n{err}")
    except psycopg.Error as err:
        log.error(f"Other psycopg error executing: \n{query} \n{err}")
    except Exception as err:
        log.error(f"Error executing query: \n{query} \n{err}")
    
    return response

'''
Returns total miles of current and planned trails within geometry
- trail_miles
- trail_miles_planned
'''
def get_trail_miles(geoid: int):
    pass

'''
Returns total square miles of open space within geometry
- open_space_sq_miles
'''
def get_open_space_sq_miles(geoid: int):
    pass

'''
Returns total number of freight centers within geometry
- freight_centers
'''
def get_freight_centers(geoid: int):
    pass

'''
Returns total miles of freight rail within geometry
- freight_rail_miles
'''
def get_freight_rail_miles(geoid: int):
    pass

'''
Returns total miles of freight highway within geometry
- freight_highway_miles
'''
def get_freight_highway_miles(geoid: int):
    pass