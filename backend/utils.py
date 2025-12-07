from pymongo import MongoClient
from config import MONGO_URI


client = MongoClient(MONGO_URI)
db = client.get_default_database()


users = db.users


# helper functions


def create_user(user):
return users.insert_one(user).inserted_id


def find_user_by_email(email):
return users.find_one({'email': email})


def get_user_by_id(uid):
return users.find_one({'_id': uid})
backend/models.py
from werkzeug.security import generate_password_hash, check_password_hash




def hash_password(password: str) -> str:
return generate_password_hash(password)




def verify_password(hash_pw: str, password: str) -> bool:
return check_password_hash(hash_pw, password)


