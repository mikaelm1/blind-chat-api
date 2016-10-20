import os, sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest 
from flask_sqlalchemy import SQLAlchemy 

from application import app, db 
from user.models import User 


class UserTest(unittest.TestCase):

	def setUp(self):
		db_username = app.config["DB_USERNAME"]
		db_password = app.config["DB_PASSWORD"]
		db_host = app.config["DB_HOST"]
		self.db_uri = "mysql+pymysql://%s:%s@%s/" % (db_username, db_password, db_host)
		app.config["TESTING"] = True 
		app.config["BLOG_DATABASE_NAME"] = "test_chatdb"
		app.config["SQLALCHEMY_DATABASE_URI"] = self.db_uri + app.config["BLOG_DATABASE_NAME"]
		engine = sqlalchemy.create_engine(self.db_uri)
		conn = engine.connect()
		conn.execute("commit")
		conn.execute("CREATE DATABASE " + app.config["BLOG_DATABASE_NAME"])
		db.create_all()
		conn.close()
		self.app = app.test_client()

	def tearDown(self):
		db.session.remove()
		engine = sqlalchemy.create_engine(self.db_uri)
		conn = engine.connect()
		conn.execute("commit")
		conn.execute("DROP DATABASE " + app.config["BLOG_DATABASE_NAME"])
		conn.close()



if __name__ == '__main__':
	unittest.main()