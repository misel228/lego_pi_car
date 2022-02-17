# Lego Pi Car - Low Level Control
# https://github.com/misel228/lego_pi_car
# Author: Stefan Misch

# Low level control of the car using a
# "Snekboard" controller (https://www.crowdsupply.com/keith-packard/snekboard)

# Neo pixel brightness
brightness = 0.1

# max power send to both motors at once
# with a regular power bank it should be no problem but
# a computer's USB port might not have enough power
# remember, if USB power is present the battery is ignored
max_power = 0.5

# color definitions (I don't like the formatting either)
colors = {
    "red": (brightness, 0,    0),
    "green": (0, brightness, 0),
    "blue": (0, 0,    brightness),
    "yellow": (brightness, brightness, 0),
    "cyan": (0, brightness, brightness),
    "magenta": (brightness, 0, brightness),
    "black": (0, 0,    0),
    "white": (brightness, brightness,    brightness)
}

# this sets the neopixels on the board
def set_pixels(color_1, color_2):
    talkto(NEOPIXEL)
    pixels = [color_1, color_2]
    neopixel(pixels)

# initialize the motors
def init():
    print("Initializing motors")
    talkto(M1)
    setleft()
    on()
    setpower(0)
    talkto(M3)
    on()
    setpower(0)
    print("Done")
    set_pixels(colors["green"], colors["green"])

# the power needs to be limited
# something is
def limit_power(power):
    print("trying to limit power")
    print(power)
    print(max_power)
    if(power > max_power):
        return max_power
    if(power < 0):
        return 0
    return power

# move forward, i.e. both motors in the same direction.
# They're mounted in a different orientation.
# that's why the different directions here
def forward(power):
    power = limit_power(power)
    set_pixels(colors["blue"], colors["blue"])
    talkto(M1)
    setleft()
    on()
    setpower(power)
    talkto(M3)
    setright()
    on()
    setpower(power)

# move backward see note to "forward()"
def backward(power):
    power = limit_power(power)
    set_pixels(colors["magenta"], colors["magenta"])
    talkto(M1)
    setright()
    on()
    setpower(power)
    talkto(M3)
    setleft()
    on()
    setpower(power)

def rotate_left(power):
    set_pixels(colors["red"], colors["green"])
    power = limit_power(power)
    talkto(M1)
    setright()
    on()
    setpower(power)
    talkto(M3)
    setright()
    on()
    setpower(power)

def rotate_right(power):
    set_pixels(colors["green"], colors["red"])
    set_pixels(colors["red"], colors["green"])
    power = limit_power(power)
    talkto(M1)
    setleft()
    on()
    setpower(power)
    talkto(M3)
    setleft()
    on()
    setpower(power)

def t():

    print("fwd")
    forward(1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("back")
    backward(1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("r l")
    rotate_left(1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("r r")
    rotate_right(1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("fwd r")
    forward_turn_right(0.3, 0.1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("fwd l")
    forward_turn_left(0.3, 0.1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("fwd r")
    backward_turn_right(0.3, 0.1)
    time.sleep(1)
    stop()
    time.sleep(1)

    print("fwd l")
    backward_turn_left(0.3, 0.1)
    time.sleep(1)
    stop()
    time.sleep(1)

# TODO
def forward_turn_right(left_power, right_power):
    set_pixels(colors["blue"], colors["blue"])
    talkto(M1)
    setleft()
    on()
    setpower(left_power)
    talkto(M3)
    setright()
    on()
    setpower(right_power)

def forward_turn_left(left_power, right_power):
    set_pixels(colors["blue"], colors["blue"])
    talkto(M1)
    setleft()
    on()
    setpower(left_power)
    talkto(M3)
    setright()
    on()
    setpower(right_power)

def backward_turn_right(left_power, right_power):
    set_pixels(colors["blue"], colors["blue"])
    talkto(M1)
    setright()
    on()
    setpower(left_power)
    talkto(M3)
    setleft()
    on()
    setpower(right_power)

def backward_turn_left(left_power, right_power):
    set_pixels(colors["blue"], colors["blue"])
    talkto(M1)
    setright()
    on()
    setpower(left_power)
    talkto(M3)
    setleft()
    on()
    setpower(right_power)

# move forward until the sensor says no ;)
def auto_forward():
    while True:
        power = read(A1)
        if(power < 0.1):
            stop()
            return
        power = limit_power(power)
        print(power)
        forward(power)
        time.sleep(1)

# turn motors off
def shut_down():
    talkto(M1)
    off()
    talkto(M3)
    off()
    set_pixels(colors["red"], colors["red"])

# set speed to zero
def stop():
    talkto(M1)
    setpower(0)
    talkto(M3)
    setpower(0)
    set_pixels(colors["yellow"], colors["yellow"])

# shortcut for stop()
def s():
    stop()

# everything starts here
set_pixels(colors["red"], colors["red"])
init()