import requests
from keys import TEQ_API_KEY

def search_flight(ori, dest, date_from, date_to, min_nights, max_nights, currency):
    api_url = f'https://tequila-api.kiwi.com/v2/search?fly_from={ori}&fly_to={dest}&dateFrom={date_from}&dateTo={date_to}&nights_in_dst_from={min_nights}&nights_in_dst_to={max_nights}&curr={currency}'
    resp = requests.get(url=api_url, headers = TEQ_API_KEY)
    return resp.json()

# test = search_flight('LON', 'MAD', '22/03/2024', '30/03/2024', 4 , 6, 'GBP')
# print(test)
