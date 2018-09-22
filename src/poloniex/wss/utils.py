import json


poloniex_wss_url = 'wss://api2.poloniex.com'


def subscribe_msg(channel_id: int) -> str:
    return __mk_msg(channel_id=channel_id, cmd='subscribe')


def unsubscribe_msg(channel_id: int) -> str:
    return __mk_msg(channel_id=channel_id, cmd='unsubscribe')


def __mk_msg(channel_id: int, cmd: str) -> str:
    return json.dumps({'channel': channel_id, 'command': cmd})


