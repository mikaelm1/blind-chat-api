from flask import Flask, jsonify  
from flask_socketio import SocketIO, emit 
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

users = ["Mike", "Ben"]

@app.route('/')
def root():
	return jsonify({"result": {"message": "You have reached the root"}})

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



if __name__ == '__main__':
	socketio.run(app, debug=True)