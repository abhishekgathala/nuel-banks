from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = "nuelbankkey"

# Mongo connection
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://admin:adminpassword@mongo:27017/")
client = MongoClient(MONGO_URI)

# Database name: nuel_bank
db = client['nuel_bank']
users = db['users']


# ---------------- HOME ----------------
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# ---------------- ABOUT ----------------
@app.route('/about')
def about():
    return render_template('about.html')


# ---------------- SERVICES ----------------
@app.route('/services')
def services():
    return render_template('services.html')


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name  = request.form.get('last_name')
        email      = request.form.get('email')
        mobile     = request.form.get('mobile')
        address    = request.form.get('address')
        password   = request.form.get('password')

        if users.find_one({"email": email}):
            flash("User already exists!")
            return redirect(url_for('register'))

        users.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "mobile": mobile,
            "address": address,
            "password": password,
            "status": "Active Customer"
        })

        flash("Registration successful! Please login.")
        return redirect(url_for('login'))

    return render_template('register.html')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = users.find_one({"email": email, "password": password})

        if user:
            # Save all data in session
            session['first_name'] = user.get('first_name')
            session['last_name'] = user.get('last_name')
            session['email'] = user.get('email')
            session['mobile'] = user.get('mobile')
            session['address'] = user.get('address')
            session['status'] = user.get('status')

            return redirect(url_for('profile'))

        else:
            flash("Invalid credentials!")
            return redirect(url_for('login'))

    return render_template('login.html')


# ---------------- PROFILE ----------------
@app.route('/profile')
def profile():

    if 'email' not in session:
        return redirect(url_for('login'))

    user_data = {
        "first_name": session.get('first_name'),
        "last_name": session.get('last_name'),
        "email": session.get('email'),
        "mobile": session.get('mobile'),
        "address": session.get('address'),
        "status": session.get('status')
    }

    return render_template('profile.html', user=user_data)


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for('login'))


# ---------------- MAIN ----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
