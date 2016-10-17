from flask import jsonify 
from flask_socketio import emit, join_room, leave_room 

from application import socketio
from user.models import User


@socketio.on('connect')
def connect():
	print("Client connected")
	emit('Connected')

@socketio.on('disconnect')
def disconnect():
	print("Client disconnected")

@socketio.on('connectUser')
def connect_user(user):
	print("Connecting user")
	users = User.query.all()
	print("User " + str(user))
	users_json = [user.serialize() for user in users]
	print("Users json " + str(users_json))
	emit("userList", users_json, json=True)

@socketio.on('chatMessage')
def handle_message(message, user):
	print("Received message " + str(message))
	# TODO: Save message to db
	# The message will be emmited as a dictionary object
	emit("newChatMessage", {"message": message, "user": user}, broadcast=True)


# Rooms

@socketio.on('join')
def on_join(data):
	room = data["room"]
	print("Attempting to join room " + str(room))
	join_room(room)
	emit({"room": str(room)}, room=room)

@socketio.on('leave')
def on_leave(data):
	room = data["room"]
	print("Attempting to leave room " + str(room))
	leave_room(room)
	emit({"room": str(room)}, room=room)

@socketio.on('room_message')
def handle_room_message(data):
	room = data["room"]
	message = data["message"]
	emit("new_room_message", {"message": message}, room=room)





