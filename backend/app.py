
from flask import Flask
from pymongo import MongoClient
import os

app = Flask(__name__)

# Fix env name mismatch also (see below)
mongo_url = os.environ.get("MONGO_URI", "mongodb://admin:adminpassword@mongo:27017/nuel_db?authSource=admin")
client = MongoClient(mongo_url)
db = client["nuelbank"]

@app.route("/")
def home():
    return "✅ NUEL BANK APPLICATION IS RUNNING SUCCESSFULLY!"

@app.route("/health")
def health():
    return {"status": "OK", "service": "Nuel Bank"}

if _name_ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

