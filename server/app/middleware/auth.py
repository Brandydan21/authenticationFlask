from ..extensions import request, jsonify, current_app, jwt, wraps

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Invalid token'}), 403

        return func(*args, **kwargs)

    return decorated