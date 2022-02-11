console.log("scripts.js loaded")

var ws = new WebSocket("ws://192.168.22.145:5678/");
var socket_connected = false;

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
};


// callback-Funktion wird gerufen, wenn ein Fehler auftritt
ws.onerror = function (errorEvent) {
    console.log("Error! Die Verbindung wurde unerwartet geschlossen");
};

ws.onclose = function (closeEvent) {
    console.log('Die Verbindung wurde geschlossen --- Code: ' + closeEvent.code + ' --- Grund: ' + closeEvent.reason);
	console.log(closeEvent)
};

var send_message = function(message) {
	if(socket_connected == false) {
		console.log("socket not connected")
		return;
	}
	
	var message = document.getElementById('message').value;
	ws.send(message)
}


