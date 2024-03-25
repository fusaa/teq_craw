import requests
from keys import TEQ_API_KEY
from datetime import datetime, timedelta


def search_flight(ori, dest, date_from, date_to, min_nights, max_nights, currency):
    api_url = f'https://tequila-api.kiwi.com/v2/search?fly_from={ori}&fly_to={dest}&dateFrom={date_from}&dateTo={date_to}&nights_in_dst_from={min_nights}&nights_in_dst_to={max_nights}&curr={currency}'
    resp = requests.get(url=api_url, headers = TEQ_API_KEY)
    return resp.json()


def dates_from_to():  # returns date_from, date_to
    date_from = datetime.now() + timedelta(days=1)
    date_to =  datetime.now() + timedelta(days=14)
    return str(date_from.strftime('%d/%m/%Y')), str(date_to.strftime('%d/%m/%Y'))


