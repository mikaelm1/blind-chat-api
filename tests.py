import os, sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest 
import sqlalchemy
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


	def user_dict(self):
		return dict(
			username="Becca",
			email="becca@example.com",
			password="testing"
			)

	def test_register_user(self):
		# basic registration
		rv = self.app.post('/register', data=self.user_dict(), follow_redirects=True)
		assert User.query.filter_by(username=self.user_dict()["username"]).count() == 1
		
		# invalid: Same user registering
		user2 = self.user_dict()
		rv = self.app.post('/register', data=user2)
		assert "user already exists" in str(rv.data).lower()


	def test_login_user(self):
		# create user
		self.app.post('/register', data=self.user_dict())
		# login
		rv = self.app.post('/login', data=dict(
			username=self.user_dict()["username"],
			password=self.user_dict()["password"]
			))
		assert "successfully logged in" in str(rv.data).lower()
		# login with wrong password
		user2 = self.user_dict()
		user2["password"] = "wrong"
		rv = self.app.post('/login', data=user2)
		assert "password or username is wrong" in str(rv.data).lower()
		



if __name__ == '__main__':
	unittest.main()