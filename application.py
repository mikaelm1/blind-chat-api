from flask import Flask, jsonify  
from flask_socketio import SocketIO 
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='eventlet')

from user import routes 
from chat import routes 
