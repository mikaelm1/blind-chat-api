from flask import jsonify, request  

from application import app, db 
from user.models import User

@app.route('/')
def root():
	print("Hitting the root")
	return jsonify({"result": {"message": "You have reached the root"}})

@app.route('/register', methods=['GET', 'POST'])
def register():
	print("Request in register route: " + str(request.form))
	username = request.form.get('username')
	email = request.form.get('email')
	password = request.form.get('password')
	if username and email and  password:
		user = User(username, email, password)
		db.session.add(user)
		db.session.commit()
	return "Register route says hi"
