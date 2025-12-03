import os


MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/nuel_db')
SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this')
