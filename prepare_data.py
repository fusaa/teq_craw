import pandas as pd
from pandas.io.json import json_normalize

def flatten_data(json_data):
    return pd.DataFrame(json_normalize(json_data))

def check_columns(dataframe):
    pass

def insert_search_id(dataframe_pre, dataframe_flights):
    dataframe_flights['search_id'] = dataframe_pre.loc[0]['search_id']
    return dataframe_flights

def remove_data_column(dataframe_pre):
    return dataframe_pre.drop(columns='data')

