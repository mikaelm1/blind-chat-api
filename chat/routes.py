from flask import jsonify 
from flask_socketio import emit 

from application import socketio
from user.models import User 

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
	users = User.query.all()
	print("User " + str(user))
	users_json = [user.serialize() for user in users]
	print("Users json " + str(users_json))
	emit("userList", users_json, json=True)


