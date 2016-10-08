from flask import jsonify 

from application import socketio

users = {"user1": "Mike", "user2": "Ashley", "user3": "Becca"}

@socketio.on('connect')
def connect():
	print("Client connected")
	emit('Connected')

@socketio.on('disconnect')
def disconnect():
	print("Client disconnected")

def ack():
	print("Message received")

@socketio.on('connectUser')
def connect_user(user):
	print("Connecting user")
	emit("userList", users)


