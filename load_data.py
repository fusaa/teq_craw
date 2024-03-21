import keys
from sqlalchemy import create_engine

host = keys.PAGILA_HOST
port = 5432
database ='pagila'
user = keys.PAGILA_USER
pwd = keys.PAGILA_PWD
endpoint = f'postgresql://{user}:{pwd}@{host}:{port}/{database}'

def create_schema():
    conn = create_engine(endpoint)


    query_create_schema = """
    CREATE TABLE student.fu_flight_project(

        id	                              VARCHAR(90),
        fly_from	                      VARCHAR(10),
        fly_to	                          VARCHAR(10),
        city_from	                      VARCHAR(90),
        city_code_from	                  VARCHAR(10),
        city_to	                          VARCHAR(90),
        city_code_to	                  VARCHAR(10),
        local_departure	                  TIMESTAMP,
        utc_departure	                  TIMESTAMP,
        local_arrival	                  TIMESTAMP,
        utc_arrival	                      TIMESTAMP,
        nights_in_dest	                  INTEGER,
        quality	                          INTEGER,
        distance	                      INTEGER,
        price	                          INTEGER,
        airlines	                      VARCHAR(90),
        route	                          TEXT,
        booking_token	                  TEXT,
        facilitated_booking_available	  BOOLEAN,
        pnr_count	                      VARCHAR(4),
        has_airport_change	              BOOLEAN,
        technical_stops	                  VARCHAR(4),
        throw_away_ticketing	          BOOLEAN,
        hidden_city_ticketing	          BOOLEAN,
        virtual_interlining	              BOOLEAN,
        country_from_code	              VARCHAR(10),
        country_from_name	              VARCHAR(90),
        country_to_code	                  VARCHAR(10),
        country_to_name	                  VARCHAR(90),
        duration_departure	              INTEGER,
        duration_return	                  INTEGER,
        duration_total	                  INTEGER,
        conversion_eur	                  REAL,
        conversion_gbp	                  INTEGER,
        fare_adults	                      INTEGER,
        fare_children	                  INTEGER,
        fare_infants	                  INTEGER,
        price_dropdown_base_fare	      INTEGER,
        price_dropdown_fees	              FLOAT,
        bags_price_1	                  INTEGER,
        baglimit_hand_height	          INTEGER,
        baglimit_hand_length	          INTEGER,
        baglimit_hand_weight	          INTEGER,
        baglimit_hand_width	              INTEGER,
        baglimit_hold_dimensions_sum	  INTEGER,
        baglimit_hold_height	          INTEGER,
        baglimit_hold_length	          INTEGER,
        baglimit_hold_weight	          INTEGER,
        baglimit_hold_width	              INTEGER,
        baglimit_personal_item_height	  INTEGER,
        baglimit_personal_item_length	  INTEGER,
        baglimit_personal_item_weight	  INTEGER,
        baglimit_personal_item_width	  INTEGER,
        availability_seats	              INTEGER,
        bags_price_2	                  FLOAT,
        search_id	                      VARCHAR(60)
        )"""
    
    conn.execute(query_create_schema)

create_schema()
    
