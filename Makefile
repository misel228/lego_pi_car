all: vlc

setup_vlc:
	sudo apt install vlc
	sudo modprobe bcm2835-v4l2


setup_serial:
	sudo apt install python3-serial
