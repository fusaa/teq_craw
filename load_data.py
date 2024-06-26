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
        fly_from                          VARCHAR(10),
        fly_to                            VARCHAR(10),
        city_from                         VARCHAR(90),
        city_code_from                    VARCHAR(10),
        city_to                           VARCHAR(90),
        city_code_to                      VARCHAR(10),
        local_departure	                  TIMESTAMP,
        utc_departure                     TIMESTAMP,
        local_arrival                     TIMESTAMP,
        utc_arrival                       TIMESTAMP,
        nights_in_dest                    INTEGER,
        quality                           INTEGER,
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
    
    query_create_schema_head = """
    CREATE TABLE student.fu_flight_project_head(
        search_id	                      VARCHAR(60),
        currency                          VARCHAR(10),
        fx_rate                           FLOAT,
        results                           INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    
    conn.execute(query_create_schema)
    conn.execute(query_create_schema_head)
    return None


def create_schema_routes():
    conn = create_engine(endpoint)
    
    query_create_schema_routes = """
    CREATE TABLE student.fu_flight_project_routes(
    id                       TEXT,
    combination_id           TEXT,
    fly_from                 VARCHAR(10),
    fly_to                   VARCHAR(10),
    city_from                 VARCHAR(90),
    city_code_from             VARCHAR(10),
    city_to                  VARCHAR(90),
    city_code_to            VARCHAR(10),
    local_departure          TIMESTAMP,
    utc_departure            TIMESTAMP,
    local_arrival            TIMESTAMP,
    utc_arrival              TIMESTAMP,
    airline                  TEXT,
    flight_no                INTEGER,
    operating_carrier        TEXT,
    operating_flight_no      TEXT,
    fare_basis               TEXT,
    fare_category            TEXT,
    fare_classes             TEXT,
    return                   INTEGER,
    bags_recheck_required    BOOLEAN,
    vi_connection            BOOLEAN,
    guarantee                BOOLEAN,
    equipment                TEXT,
    vehicle_type             TEXT,
    search_id                VARCHAR(60)  
    )
    
    """
    
    return conn.execute(query_create_schema_routes)


def write_server(data_frame, data_frame_head):
    conn = create_engine(endpoint)
    code_data = data_frame.to_sql( 'fu_flight_project', schema = 'student', con=conn, if_exists='append', index=False )
    code_head = data_frame_head.to_sql( 'fu_flight_project_head', schema = 'student', con=conn, if_exists='append', index=False )
    return code_data, code_head
    
def alter_table_bug_fix():
    conn = create_engine(endpoint)
    query = """
    ALTER TABLE student.fu_flight_project ALTER COLUMN id TYPE TEXT
    """
    ret = conn.execute(query)
    return ret

def write_server_routes(data_frame):
    conn = create_engine(endpoint)
    code = data_frame.to_sql( 'fu_flight_project_routes', schema = 'student', con=conn, if_exists='append', index=False )
    return code

# create_schema()
# alter_table_bug_fix()
# create_schema_routes()
