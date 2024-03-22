from get_data import *
from prepare_data import *
from load_data import *

def main(dest):
    # get_data
    call_result = search_flight('LON', dest, '22/03/2024', '25/04/2024', 4 , 9, 'GBP')

    # prepare_data
    data_head = flatten_data(call_result)

    data = flatten_data(call_result['data'])
    data = rename_columns(data)
    data = insert_search_id(data_head, data)
    data = do_json_dump_columns(data)

    data_head = rename_columns_head(data_head)
    data_head = remove_data_column(data_head)

    # load_data
    print(write_server(data, data_head))

destinations = ['AMS','CDG','FRA','MAD','BCN','FCO','MUC','LIS','DUB']  # testing w/ more destinations
#  FRA issues,  table columns width

if __name__ == "__main__":
    for dest in destinations:
        print('Doing ' + dest)
        main(dest)

