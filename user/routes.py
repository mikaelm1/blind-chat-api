from flask import jsonify, request  
from sqlalchemy.exc import IntegrityError
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
		try:
			user = User(username.lower(), email.lower(), password.lower())
			db.session.add(user)
			db.session.commit()
			return jsonify({"response": {"success": "User created"}}), 200
		except IntegrityError as e:
			return jsonify({"response": {"failure": "User already exists"}}), 400
		except Exception as e:
			print("ERROR: " + str(e))
			return jsonify({"response": {"failure": "Error creating user"}}), 404
	else:
		return "Error", 404
