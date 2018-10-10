import requests


BASE_URL = 'https://api.binance.com/'


def server_time():
    path = 'api/v1/time'
    response = requests.get(url=BASE_URL + path)
    if response.status_code != 200:
        raise RuntimeError(f'failed to reach {path}: {response.status_code}')
    return response.json()['serverTime']


def exchange_info():
    path = 'api/v1/exchangeInfo'
    response = requests.get(url=BASE_URL + path)
    if response.status_code != 200:
        raise RuntimeError(f'failed to reach {path}: {response.status_code}')
    return response.json()
