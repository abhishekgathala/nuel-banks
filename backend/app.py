<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import os

app = Flask(_name_)
app.secret_key = "nuelbankkey"

# Mongo connection
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://admin:adminpassword@mongo:27017/")
client = MongoClient(MONGO_URI)
db = client['nuelbank']
users = db['users']

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if users.find_one({"email": email}):
            flash("User already exists!")
            return redirect(url_for('register'))

        users.insert_one({
            "name": name,
            "email": email,
            "password": password,
            "status": "Active Customer"
        })

        flash("Registration successful! Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        user = users.find_one({"email": email, "password": password})

        if user:
            # Save data in session
            session['user_email'] = user['email']
            session['user_name'] = user['name']
            session['status'] = user['status']

            # ✅ THIS IS THE FIX
            return redirect(url_for('profile'))

        else:
            flash("Invalid credentials!")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/profile')
def profile():
    if 'user_email' not in session:
        return redirect(url_for('login'))

    user_data = {
        "name": session.get('user_name'),
        "email": session.get('user_email'),
        "status": session.get('status')
    }

    return render_template('profile.html', user=user_data)


@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for('login'))


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)
kyc-aakr-cvq
=======
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

if name == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
>>>>>>> e7efddb1d22f2c716d0ee4040db22c3f19f86003
