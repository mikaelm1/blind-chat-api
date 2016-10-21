from application import db 
from util.common import utc_now_ts as timestamp
from user.models import User 

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(250))
	created = db.Column(db.Integer)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	room = db.Column(db.String(50))

	def __init__(self, content, author, room):
		self.content = content 
		self.author_id = author.id 
		self.created = timestamp()
		self.room = room 

	def __repr__(self):
		return "<Message %r>" % self.content

	def serialize(self):
		user = User.query.filter_by(id=self.author_id).first()
		return {
			"content": self.content,
			"room": self.room,
			"created": str(self.created),
			"username": user.username
		}

