from flask import jsonify 
from flask_socketio import emit, join_room, leave_room 

from application import socketio, db 
from user.models import User
from .models import Message 


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
	room_messages= Message.query.filter_by(room=room)
	room_messages_json = [msg.serialize() for msg in room_messages]
	emit("room_messages", {"room": room, "messages": room_messages_json}, room=room)


@socketio.on('leave')
def on_leave(data):
	room = data["room"]
	print("Attempting to leave room " + str(room))
	leave_room(room)
	emit({"room": str(room)}, room=room)


@socketio.on('room_message')
def handle_room_message(data):
	room = data["room"]
	content = data["message"]
	username = data["user"]
	if room and content and username:
		user = User.query.filter_by(username=username).first()
		if user:
			message_to_save = Message(content=content, author=user, room=room)
			db.session.add(message_to_save)
			db.session.commit()
		emit("new_room_message", {"message": content}, room=room)





