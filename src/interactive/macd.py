import numpy as np
from bokeh.plotting import save, figure, output_file

from helpers import get_root_dir
from private.mongo import get_mongo_client
from trade.math.macd import *


def extract_bid_ask(db_val: dict) -> (float, float):
    return float(db_val['highestBid']), float(db_val['lowestAsk'])


def main():
    client = get_mongo_client(port=27018)
    db = client.spots
    symbol = 'BTC/USDT'
    coll = db[symbol]
    spots = np.array(list(map(extract_bid_ask, coll.find({})))).transpose()
    spot_filename = f"{symbol.replace('/', '-')}_spot.html"
    plots_root = f'{get_root_dir()}/plots'
    output_file(filename=f'{plots_root}/{spot_filename}')
    f = figure(title=symbol)
    xs = np.arange(spots.shape[1])
    # f.line(xs, spots[0], legend='bid', line_color='green')
    # f.line(xs, spots[1], legend='ask', line_color='red')
    df = pd.DataFrame(spots.transpose(), columns=['bid', 'ask'])
    m = macd(df, long_per=26, short_per=9)
    f.line(xs, m.bid, legend='macd bid', line_color='yellow')
    f.line(xs, m.ask, legend='macd ask', line_color='yellow')
    # print(m)
    print(save(f))


if __name__ == '__main__':
    main()
