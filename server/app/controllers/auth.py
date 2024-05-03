from ..extensions import current_app, request, jsonify, session, jwt, datetime, timedelta

from ..models import User

def get_private_user():
    return 'you are logged in'

def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if not user:
         return jsonify({'error': 'User not found'}), 404
    
    if user.password != password:
        return jsonify({'error': 'Incorrect password'}), 401

    session['logged_in'] = True

    token = jwt.encode({
            'user': username,
            'expiration': str(datetime.now() + timedelta(minutes=50))
        }, current_app.config['SECRET_KEY'])
    
    return jsonify({'token': token})
