import requests
import json


__url_public = 'https://poloniex.com/public'


def get_ticks():
    response = requests.get(url=__url_public, params={'command': 'returnTicker'})
    return response.json()


def main():
    ticks = get_ticks()
    print(json.dumps(ticks, indent=4))


if __name__ == '__main__':
    main()