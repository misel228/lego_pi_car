console.log("scripts.js loaded")

var ws = new WebSocket("ws://192.168.22.145:5678/");
var socket_connected = false;
var interval_callback;


ws.onmessage = function (event) {
	var messages = document.getElementsByTagName('ul')[0],
		message = document.createElement('li'),
		content = document.createTextNode(event.data);
	message.appendChild(content);
	messages.appendChild(message);
};

ws.onopen = function (event) {
	ws.send("First message");
	socket_connected = true;
	interval_callback = window.setInterval(loop, 33)
};


// callback-Funktion wird gerufen, wenn ein Fehler auftritt
ws.onerror = function (errorEvent) {
    console.log("Error! Die Verbindung wurde unerwartet geschlossen");
};

ws.onclose = function (closeEvent) {
    console.log('Die Verbindung wurde geschlossen --- Code: ' + closeEvent.code + ' --- Grund: ' + closeEvent.reason);
	console.log(closeEvent)
	clearInterval(interval_callback)
};

var send_message = function(message) {
	if(socket_connected == false) {
		console.log("socket not connected")
		return;
	}

	var message = document.getElementById('message').value;
	ws.send(message)
}

// KEYBOARD HANDLING

// true = pressed
var key_pressed_states = {
	37: false,
	38: false,
	39: false,
	40: false
}

var key_labels = {
	37: 'left',
	38: 'up',
	39: 'right',
	40: 'down'

}

//detecting arrow key presses
document.addEventListener('keydown', function(e) {
    switch (e.keyCode) {
        case 37:
        case 38:
        case 39:
        case 40:
            //console.log(key_labels[e.keyCode] + ' down');
			key_pressed_states[e.keyCode] = true;
            break;
    }
});

//detecting arrow key leave
document.addEventListener('keyup', function(e) {
    switch (e.keyCode) {
        case 37:
        case 38:
        case 39:
        case 40:
            //console.log(key_labels[e.keyCode] + ' up');
			key_pressed_states[e.keyCode] = false;
            break;
    }
});

var start_loop = function() {
	while(ws.readyState == OPEN) {
		loop();
	}
	console.log('WebSocket not open')
}

var test_loop = function() {
	console.log(loop());
}

//speed will be made variable with joystick input later
var speed = 1;

// store last command to avoid resending the same stuff all the time
var last_command = '';
var loop = function() {
	var command = get_command();
	if(command == last_command) {
		return;
	}
	last_command = command
	ws.send(command);
}

var get_command = function() {
	//get all key states
	var direction = get_direction();
	var turn = get_turn();

	//if no state send stop()
	if((direction + turn) == '') {
		command = 'stop()';
		return command;
	}

	//if no direction is given rotate
	if(direction == '') {
		command = 'rotate_' + turn + '(' + speed + ')';
		return command;
	}

	//if no turn given drive in one direction
	if(turn == '') {
		command = direction + '(' + speed + ')';
		return command;
	}

	//otherwise make a moving turn
	command = direction + '_' + turn + '(' + speed + ',' + speed + ')';
	return command;
}

//make sure to never drive forwards and backwards at the same time
var get_direction = function () {
	if(key_pressed_states[38]) {
		return 'forward';
	}
	if(key_pressed_states[40]) {
		return 'backward';
	}
	return false;
}

//make sure to never drive left and right at the same time
var get_turn = function () {
	if(key_pressed_states[37]) {
		return 'left';
	}
	if(key_pressed_states[39]) {
		return 'right';
	}
	return false;
}
