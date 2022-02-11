#!/usr/bin/env python

import asyncio
import websockets


async def loop(websocket, path):
    while True:
        name = await websocket.recv()
        print("< {}".format(name))

        greeting = "Hello {}!".format(name)
        await websocket.send(greeting)
        print("> {}".format(greeting))

try:

    start_server = websockets.serve(loop, port = 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
finally:
    print("end")
