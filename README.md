# Lego Pi Car
A tracked vehicle out of Lego bricks controlled with a Raspberry Pi Zero

## Low level control
The motors are directly conntected to a [Snekboard](https://www.crowdsupply.com/keith-packard/snekboard). Which is programmed in MikroPython and talks to the Raspberry Pi over a serial connection via USB.

## High level control
The Pi Zero runs a small Apache plus PHP environment to connect the user and the low level controls. It also provides a camera feed.

## Web interface
The web interface is a Javascript application that displays the camera feed and interprets joysticks movements as commands to the vehicle.
