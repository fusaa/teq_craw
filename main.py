from get_data import *
from prepare_data import *
from load_data import *


def main(dest):
    # get_data
    
    date_from, date_to = dates_from_to()

    call_result = search_flight('LON', dest, date_from, date_to, 4 , 8, 'GBP')

    # prepare_data
    data_head = flatten_data(call_result)

    data = flatten_data(call_result['data'])
    data = rename_columns(data)
    data = insert_search_id(data_head, data)
    data = do_json_dump_columns(data)

    data_head = rename_columns_head(data_head)
    data_head = remove_data_column(data_head)

    routes = routes_dataframe(data)
    routes = rename_routes_columns(routes)
    
    # load_data
    print(f'da-dh: {write_server(data, data_head)}')
    print(f'r: {write_server_routes(routes)}')


destinations = ['AMS','CDG','FRA','MAD','BCN','FCO','MUC','LIS','DUB']  # destinations


if __name__ == "__main__":

    for dest in destinations:
        print('Doing ' + dest)
        main(dest)

