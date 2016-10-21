from functools import wraps
from flask import session, request, redirect 


def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if session.get("username"):
			return f(*args, **kwargs)
		print("Not logged in")
	return decorated_function