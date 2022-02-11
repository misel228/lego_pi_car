all:
	echo "foo"

setup: setup_serial setup_vlc setup_websockets

setup_vlc:
	sudo apt install vlc
	sudo modprobe bcm2835-v4l2


setup_serial:
	sudo apt install python3-serial

setup_websockets:
	sudo pip install websockets

#some pid file handling to allow for starting and stopping services in the background
socket_pid_file := socket.pid
web_pid_file := web.pid
socket_pid := $(shell cat ${socket_pid_file})
web_pid := $(shell cat ${web_pid_file})


start: start_service start_website

start_service:
	python high_level_control/websocket_server.py & echo "$$!" > ${socket_pid_file}

start_website:
	python3 -m http.server 8000 --directory web_interface & echo "$$!" > ${web_pid_file}

stop: stop_service stop_website

stop_service:
	kill -9 ${socket_pid}
	rm -f ${socket_pid_file}

stop_website:
	kill -9 ${web_pid}
	rm -f ${web_pid_file}
