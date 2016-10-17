from flask import Flask, jsonify  
from flask_socketio import SocketIO 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
import eventlet

app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, async_mode='eventlet')

from user import routes 
from chat import routes 
