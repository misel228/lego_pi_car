#!/usr/bin/env python
import time
import serial

def send(ser, command):
    cmd = command + "\n"
    cmd = cmd.encode()
    ser.write(cmd)

ser = serial.Serial('/dev/ttyACM0')
try:

    send(ser, "init()");
    time.sleep(1)
    send(ser, "stop()");


    while 1:
        bytes = ser.in_waiting
        # there are always two bytes in the buffer (like \r\n)
        if(ser.in_waiting > 2):
            print("Reading feed back")
            x=ser.readline()
            print(x)
        else:
            send(ser, "forward(1)")
            time.sleep(1)
            send(ser, "stop()")
            time.sleep(1)
        
        time.sleep(1)
    
finally:
    print("/nShut down - c u!/n")
    ser.write("shut_down()\n".encode())
