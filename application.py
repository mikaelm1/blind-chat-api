from flask import Flask, jsonify  
from flask_socketio import SocketIO 
from flask_sqlalchemy import SQLAlchemy 
import eventlet

app = Flask(__name__)
app.config.from_object('settings')
socketio = SocketIO(app, async_mode='eventlet')
db = SQLAlchemy(app)

from user import routes 
from chat import routes 
