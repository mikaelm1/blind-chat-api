from flask import Flask, jsonify  

app = Flask(__name__)


@app.route('/')
def root():
	return jsonify({"result": {"message": "You have reached the root"}})


if __name__ == '__main__':
	app.run()