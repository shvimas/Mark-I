import json

from poloniex.ccy_pairs_id_list import ccy_pairs_id_list


poloniex_wss_url = 'wss://api2.poloniex.com'


def subscribe_msg(channel_id: int) -> str:
    return __mk_msg(channel_id=channel_id, cmd='subscribe')


def unsubscribe_msg(channel_id: int) -> str:
    return __mk_msg(channel_id=channel_id, cmd='unsubscribe')


def __mk_msg(channel_id: int, cmd: str) -> str:
    return json.dumps({'channel': channel_id, 'command': cmd})


__ticker_response_fields = ['ccy pair id', 'last trade price', 'lowest ask', 'highest bid', '% change in 24h',
                            'base ccy volume in 24 hours', 'quote currency volume in 24h', 'is frozen',
                            'highest price in 24h', 'lowest price in 24 hours']


def parse_ticker_response(response: str) -> (str, list):
    parsed = json.loads(response)
    assert len(parsed) == 3, ValueError('expected that ticker response is a list of 3 items')
    raw_data = parsed[2]
    data = raw_data[0:1] + list(map(lambda s: float(s), raw_data[1:]))
    assert len(data) == len(__ticker_response_fields), \
        ValueError(f'unexpected number of fields ({len(data)}) in response ({response})')
    ccy_pair_id = str(data[0])
    try:
        ccy_pair = ccy_pairs_id_list[ccy_pair_id]
    except KeyError:
        raise ValueError(f'unexpected currency pair id: {ccy_pair_id}')
    return ccy_pair, dict(zip(__ticker_response_fields, data))
