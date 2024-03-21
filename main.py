import get_data
import prepare_data

test = search_flight('LON', 'MAD', '22/03/2024', '30/03/2024', 4 , 6, 'GBP')
flatten_data(test)
