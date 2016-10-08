from flask import jsonify 

from application import app

@app.route('/')
def root():
	print("Hitting the root")
	return jsonify({"result": {"message": "You have reached the root"}})