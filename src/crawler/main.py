import importlib
import sys
import time

import ccxt
import pymongo

CLIENT = pymongo.MongoClient(host='localhost', port=27017)
DB = CLIENT['spots']


def load_to_mongo(coll: str, data: dict):
    DB[coll].insert_one(document=data)


def prepare_data(data: dict) -> dict:
    info = data['info']
    return {
        'last': info['last'],
        'low24hr': info['low24hr'],
        'high24hr': info['high24hr'],
        'lowestAsk': info['lowestAsk'],
        'highestBid': info['highestBid'],
        'timestamp': time.time()
    }


def get_market_data(exchange: ccxt.Exchange):
    markets = exchange.load_markets(reload=True)
    for symbol in markets:
        data = prepare_data(data=markets[symbol])
        load_to_mongo(coll=symbol, data=data)


def repeat(delay: int, action):
    while True:
        time.sleep(delay)
        action()


def main():
    try:
        exchange = sys.argv[1]
    except IndexError:
        raise Exception('specify exchange to crawl')
    if exchange not in ccxt.exchanges:
        raise ValueError(f'{exchange} not found')

    exchange = getattr(importlib.import_module(f'ccxt.{exchange}'), exchange)
    repeat(delay=60, action=lambda: get_market_data(exchange=exchange))


if __name__ == '__main__':
    main()
