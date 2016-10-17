from application import db 
from datetime import datetime

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(250))
	created = db.Column(db.DateTime)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __init__(self, content, author):
		self.content = content 
		self.author_id = author.id 
		self.created = datetime.utcnow()

	def __repr__(self):
		return "<Message %r>" % self.content