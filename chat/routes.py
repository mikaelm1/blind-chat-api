from flask import jsonify 
from flask_socketio import emit 

from application import socketio

users = ["user1", "user2", "user3"]

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


