import os, sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import flask 
from flask_script import Manager, Server 
from flask_migrate import MigrateCommand 
from application import app, socketio 
from settings import SERVER_HOST 

manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def run():
    socketio.run(app,
                 host=SERVER_HOST,
                 port=5000,
                 debug=True,
                 use_reloader=True)

if __name__ == '__main__':
	manager.run()