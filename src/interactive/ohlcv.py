import argparse

import ccxt
import pandas as pd


# noinspection PyUnresolvedReferences
def get_ohlcv(exchange: ccxt.Exchange, symbol: str, timeframe: str) -> pd.DataFrame:
    # Check if fetching of OHLC Data is supported
    if not exchange.has["fetchOHLCV"]:
        raise ValueError('{} does not support fetching OHLC data. Please use another exchange'.format(exchange))

    # Check requested timeframe is available. If not return a helpful error.
    if timeframe not in exchange.timeframes:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('The requested timeframe ({}) is not available from {}\n'.format(args.timeframe, args.exchange))
        print('Available timeframes are:')
        for key in exchange.timeframes.keys():
            print('  - ' + key)
        raise ValueError

    # Check if the symbol is available on the Exchange
    exchange.load_markets()
    if symbol not in exchange.symbols:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('The requested symbol ({}) is not available from {}\n'.format(symbol, exchange))
        print('Available symbols are:')
        for key in exchange.symbols:
            print('  - ' + key)
        print('-' * 80)
        raise ValueError

    # Get data
    data = exchange.fetch_ohlcv(symbol, timeframe)
    header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    return pd.DataFrame(data, columns=header)


def parse_args():
    parser = argparse.ArgumentParser(description='CCXT Market Data Downloader')

    parser.add_argument('-s', '--symbol',
                        type=str,
                        required=True,
                        help='The Symbol of the Instrument/Currency Pair To Download')

    parser.add_argument('-e', '--exchange',
                        type=str,
                        required=True,
                        help='The exchange to download from')

    parser.add_argument('-t', '--timeframe',
                        type=str,
                        default='1d',
                        choices=['1m', '5m', '15m', '30m', '1h', '2h', '3h', '4h', '6h', '12h', '1d', '1M', '1y'],
                        help='The timeframe to download')

    parser.add_argument('--debug',
                        action='store_true',
                        help='Print Sizer Debugs')

    return parser.parse_args()


def main():
    # Get our arguments
    args = parse_args()

    # Get our Exchange
    try:
        exchange = getattr(ccxt, args.exchange)()
    except AttributeError:
        print('-' * 36, ' ERROR ', '-' * 35)
        print('Exchange "{}" not found. Please check the exchange is supported.'.format(args.exchange))
        print('-' * 80)
        return

    df = get_ohlcv(exchange=exchange, symbol=args.symbol, timeframe=args.timeframe)

    # Save it
    symbol_out = args.symbol.replace("/", "")
    filename = '{}-{}-{}.csv'.format(args.exchange, symbol_out, args.timeframe)
    df.to_csv(filename)


if __name__ == '__main__':
    main()
