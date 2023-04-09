"""
Utils package

"""

import os
import logging
from dotenv import load_dotenv
from sqlalchemy import text

# Environment Variables
load_dotenv()

# app config
IS_DEBUG = os.getenv("DEBUG", 0)
POSTGRESQL_URI = os.getenv("POSTGRES_URL", None)
CLEAN_START = os.getenv("CLEAN_START", False)

# logging config
logging.basicConfig(
    level=logging.DEBUG if IS_DEBUG else logging.INFO
)
# logger
logger = logging.Logger("app")


def add_function(db):
    """
    Add the database function if not exist

    :return:
    """
    query = """
    CREATE OR REPLACE FUNCTION public.WithinRadius (
      p1 POINT,
      p2 POINT,
        radius_km double precision ) RETURNS BOOLEAN
    -- important to define the language
    LANGUAGE plpgsql
    IMMUTABLE
    AS $$
    DECLARE
        -- Here we write the variables in calculation
      delta_lat double precision; -- distance from lat2 to lat1
      delta_lon double precision; -- distrance from lon
      a double precision; -- chrod length
      c double precision; -- angular distance
    
      -- here we multiple 2 beforehand to cut costs.
      -- radius_e double precision := 6371; -- radius of the earth (in km)
      twice_radius_e double precision := 12742; -- 6371*2;
    
      distance double precision; -- required distance
    
    BEGIN
      delta_lat := radians( p2[0] - p1[0] ); -- we will use radians() function from postgres
      delta_lon := radians( p2[1] - p1[1] );
    
        -- we use the haversine formula here
        a :=	sin(delta_lat / 2)^2
                + cos(radians(p1[0]))
            * cos(radians(p2[0]))
            * sin(delta_lon /2)^2;
    
      -- we multiply (2*radius_e) directly to cut multiplication cost
      c := asin(sqrt(a));
    
      distance := twice_radius_e * c;
    
      -- check if distance is less than required distance. then return true
      RETURN distance <= radius_km;
    END
    $$;
    """
    db.session.execute(text(query))
