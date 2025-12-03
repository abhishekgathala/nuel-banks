from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from models import users, create_user, find_user_by_email
from utils import hash_password, verify_password
from bson.objectid import ObjectId


bp = Blueprint('bp', name)


@bp.route('/')
def home():
return render_template('home.html')


@bp.route('/services')
def services():
return render_template('services.html')


@bp.route('/about')
def about():
return render_template('about.html')


@bp.route('/profile')
def profile():
user_id = session.get('user_id')
if not user_id:
return redirect(url_for('bp.home'))
user = users.find_one({'_id': ObjectId(user_id)})
return render_template('profile.html', user=user)


# Auth APIs
@bp.route('/api/register', methods=['POST'])
def api_register():
data = request.json or request.form
if find_user_by_email(data.get('email')):
return jsonify({'error': 'User exists'}), 400
user = {
'name': data.get('name'),
'email': data.get('email'),
'password': hash_password(data.get('password')),
'balance': 0,
'created_at': None,
}
res = users.insert_one(user)
session['user_id'] = str(res.inserted_id)
return jsonify({'ok': True, 'id': str(res.inserted_id)})


@bp.route('/api/login', methods=['POST'])
def api_login():
data = request.json or request.form
user = find_user_by_email(data.get('email'))
if not user:
return jsonify({'error': 'Invalid credentials'}), 401
if not verify_password(user['password'], data.get('password')):
return jsonify({'error': 'Invalid credentials'}), 401
session['user_id'] = str(user['_id'])
return jsonify({'ok': True})


@bp.route('/api/logout')
def api_logout():
session.pop('user_id', None)
return redirect(url_for('bp.home'))
