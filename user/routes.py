from flask import jsonify, request  
from sqlalchemy.exc import IntegrityError
from application import app, db 
from user.models import User

@app.route('/')
def root():
	print("Hitting the root")
	return jsonify({"result": {"message": "You have reached the root"}})


@app.route('/login', methods=['GET', 'POST'])
def login():
	print("Request in login route: " + str(request.form))
	username = request.form.get('username')
	password = request.form.get('password')
	if username and password:
		user = User.query.filter_by(username=username).first()
		if user and user.username == username and user.password == password:
			return jsonify({"response": "Successfully logged in"}), 200
		else:
			return 404 
	return 500



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
