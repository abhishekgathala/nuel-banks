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
