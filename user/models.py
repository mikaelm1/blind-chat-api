import bcrypt 

from application import db 


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, email, password):
		self.username = username.lower()
		self.email = email.lower()
		self.password = self.hash_password(password)


	def __repr__(self):
		return "<User %r>" % self.username 

	def hash_password(self, password):
		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		return hashed 

	def authenticated(self, passed_password):
		'''Returns true if the passed in password matches the password saved in the database'''
		if bcrypt.checkpw(passed_password.encode('utf-8'), self.password.encode('utf-8')):
			return True 
		return False 

	def serialize(self):
		return {
			"username": self.username,
			"email": self.email 
		}