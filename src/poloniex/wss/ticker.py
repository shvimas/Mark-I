import asyncio
import websockets
from poloniex.wss.utils import *

__channel_id = 1002


async def subscribe(websocket):
    await websocket.send(subscribe_msg(channel_id=__channel_id))
    response = await websocket.recv()
    if response == '[1002,1]':
        print(f'successfully subscribed to ticker channel ({__channel_id})')
    else:
        raise RuntimeError(f'unexpected response: {response}')


async def unsubscribe(websocket):
    await websocket.send(unsubscribe_msg(channel_id=__channel_id))
    print(f'unsubscribed from ticker channel ({__channel_id})')


async def main():
    try:
        info = {}
        async with websockets.connect(poloniex_wss_url) as ws:
            await subscribe(websocket=ws)

            async for response in ws:
                ccy_pair, data = parse_ticker_response(response)
                info[ccy_pair] = data
    finally:
        await unsubscribe(websocket=ws)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
