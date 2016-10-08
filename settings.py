import os 

SECRET_KEY = 'ekjwfnekjhfkewg'
DEBUG = True 
DB_USERNAME = 'root'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'blind_chat'
DB_HOST = 'localhost'
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True 