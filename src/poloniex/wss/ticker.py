import asyncio
import websockets
from poloniex.wss.utils import *

__channel_id = 1002


async def subscribe(websocket):
    await websocket.send(subscribe_msg(channel_id=__channel_id))
    response = await websocket.recv()
    if response == '[1002,1]':
        print(f'successfully subscribed to ticker channel ({__channel_id})')


async def unsubscribe(websocket):
    await websocket.send(unsubscribe_msg(channel_id=__channel_id))
    print(f'unsubscribed from ticker channel ({__channel_id})')


async def main():
    try:
        async with websockets.connect(poloniex_wss_url) as ws:
            await subscribe(websocket=ws)

            async for msg in ws:
                print(f'<<< {msg}')
    except:
        await unsubscribe(websocket=ws)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    asyncio.get_event_loop().run_forever()
