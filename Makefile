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
stream_pid_file := stream.pid
socket_pid := $(shell cat ${socket_pid_file})
web_pid := $(shell cat ${web_pid_file})
stream_pid := $(shell cat ${stream_pid_file})


start: start_service start_website start_stream

start_service:
	python high_level_control/hl_control.py & echo "$$!" > ${socket_pid_file}

start_website:
	python3 -m http.server 8000 --directory web_interface & echo "$$!" > ${web_pid_file}

start_stream:
	#raspivid --bitrate 100000 --timeout 0 -l --output tcp://0.0.0.0:5555 & echo "$$!" > ${stream_pid_file}
	#raspivid -o - -t 0 -w 800 -h 600 -fps 12  | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8080/}' :demux=h264H & echo "$$!" > ${stream_pid_file}
	#low latency version here
	#raspivid -t 0 -w 1280 -h 720 -o - | nc 192.168.22.151 5555

stop: stop_service stop_website stop_stream

stop_service:
	kill -9 ${socket_pid}
	rm -f ${socket_pid_file}

stop_website:
	kill -9 ${web_pid}
	rm -f ${web_pid_file}

stop_stream:
	kill -9 ${stream_pid}
	rm -f ${stream_pid_file}
