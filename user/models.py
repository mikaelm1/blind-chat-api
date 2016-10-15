from application import db 

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), unique=True)
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password


	def __repr__(self):
		return "<User %r>" % self.username 


	def serialize(self):
		return {
			"username": self.username,
			"email": self.email 
		}