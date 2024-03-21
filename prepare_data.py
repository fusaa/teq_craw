import json
import pandas as pd
from pandas.io.json import json_normalize

def flatten_data(json_data):
    return pd.DataFrame(json_normalize(json_data))

def check_columns(dataframe):
    return dataframe

def rename_columns(dataframe_flights):
    columns_names = {
        'id'                           : 'id',
        'flyFrom'                      : 'fly_from',
        'flyTo'                        : 'fly_to',
        'cityFrom'                     : 'city_from',
        'cityCodeFrom'                 : 'city_code_from',
        'cityTo'                       : 'city_to',
        'cityCodeTo'                   : 'city_code_to',
        'local_departure'              : 'local_departure',
        'utc_departure'                : 'utc_departure',
        'local_arrival'                : 'local_arrival',
        'utc_arrival'                  : 'utc_arrival',
        'nightsInDest'                 : 'nights_in_dest',
        'quality'                      : 'quality',
        'distance'                     : 'distance',
        'price'                        : 'price',
        'airlines'                     : 'airlines',
        'route'                        : 'route',
        'booking_token'                : 'booking_token',
        'facilitated_booking_available': 'facilitated_booking_available',
        'pnr_count'                    : 'pnr_count',
        'has_airport_change'           : 'has_airport_change',
        'technical_stops'              : 'technical_stops',
        'throw_away_ticketing'         : 'throw_away_ticketing',
        'hidden_city_ticketing'        : 'hidden_city_ticketing',
        'virtual_interlining'          : 'virtual_interlining',
        'countryFrom.code'             : 'country_from_code',
        'countryFrom.name'             : 'country_from_name',
        'countryTo.code'               : 'country_to_code',
        'countryTo.name'               : 'country_to_name',
        'duration.departure'           : 'duration_departure',
        'duration.return'              : 'duration_return',
        'duration.total'               : 'duration_total',
        'conversion.EUR'               : 'conversion_eur',
        'conversion.GBP'               : 'conversion_gbp',
        'fare.adults'                  : 'fare_adults',
        'fare.children'                : 'fare_children',
        'fare.infants'                 : 'fare_infants',
        'price_dropdown.base_fare'     : 'price_dropdown_base_fare',
        'price_dropdown.fees'          : 'price_dropdown_fees',
        'bags_price.1'                 : 'bags_price_1',
        'baglimit.hand_height'         : 'baglimit_hand_height',
        'baglimit.hand_length'         : 'baglimit_hand_length',
        'baglimit.hand_weight'         : 'baglimit_hand_weight',
        'baglimit.hand_width'          : 'baglimit_hand_width',
        'baglimit.hold_dimensions_sum' : 'baglimit_hold_dimensions_sum',
        'baglimit.hold_height'         : 'baglimit_hold_height',
        'baglimit.hold_length'         : 'baglimit_hold_length',
        'baglimit.hold_weight'         : 'baglimit_hold_weight',
        'baglimit.hold_width'          : 'baglimit_hold_width',
        'baglimit.personal_item_height': 'baglimit_personal_item_height',
        'baglimit.personal_item_length': 'baglimit_personal_item_length',
        'baglimit.personal_item_weight': 'baglimit_personal_item_weight',
        'baglimit.personal_item_width' : 'baglimit_personal_item_width',
        'availability.seats'           : 'availability_seats',
        'bags_price.2'                 : 'bags_price_2',
        'search_id'                    : 'search_id'
        }

    return dataframe_flights.rename(columns=columns_names)

def rename_columns_head(dataframe_flights_head):
    columns_names = {
        'id'                           : 'id',
        'currency'                     : 'currency',
        'fx_rate'                      : 'fx_rate',
        '_results'                     : 'results'
        }
    return dataframe_flights_head.rename(columns=columns_names)


def insert_search_id(dataframe_pre, dataframe_flights):
    dataframe_flights['search_id'] = dataframe_pre.loc[0]['search_id']
    return dataframe_flights

def remove_data_column(dataframe_pre):
    return dataframe_pre.drop(columns='data')

def do_json_dump_columns(dataframe_flights):
    dataframe_flights['route'] = dataframe_flights['route'].apply(json.dumps)
    return dataframe_flights