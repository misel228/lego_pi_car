# Lego Pi Car - Low Level Control
# https://github.com/misel228/lego_pi_car
# Author: Stefan Misch

# Low level control of the car using a
# "Snekboard" controller (https://www.crowdsupply.com/keith-packard/snekboard)

# Neo pixel brightness
brightness = 0.1

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
    if(power > 0.3):
        return 0.3
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

# turning means only one motor is actually moving
def turn_left(power):
    set_pixels(colors["red"], colors["green"])
    talkto(M1)
    off()
    setpower(power)
    talkto(M3)
    setright()
    on()
    setpower(power)

# turning means only one motor is actually moving
def turn_right(power):
    set_pixels(colors["green"], colors["red"])
    talkto(M1)
    on()
    setpower(power)
    talkto(M3)
    off()
    setpower(power)

# move forward until the sensor says no ;)
def auto_forward():
    while True:
        power = read(A1)
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