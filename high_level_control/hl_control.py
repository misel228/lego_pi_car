#!/usr/bin/env python

# open a websocket, listen for commands, validate them,
# and send them to the bot

import asyncio
import websockets
import time
import serial

def send(ser, command):
    cmd = command + "\n"
    cmd = cmd.encode()
    ser.write(cmd)

ser = serial.Serial('/dev/ttyACM0')

def filter(command):
    #TODO add command filters
    return command

# websocket wait
async def loop(websocket, path):
    while True:
        command = await websocket.recv()
        print("< received {}".format(command))

        await websocket.send(command)
        print("> {}".format(command))
        
        command = filter(command)
        send(ser, command)
        
        # send the bot commands to the socket
        bytes = ser.in_waiting
        # there are always two bytes in the buffer (like \r\n)
        if(ser.in_waiting > 2):
            print("Reading feed back")
            x=ser.readline()
            await websocket.send(x)
            print(x)

try:

    start_server = websockets.serve(loop, port = 5678)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
finally:
    print("end")
