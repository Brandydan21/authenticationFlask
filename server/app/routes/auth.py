from . import auth_routes_bp
from ..controllers import get_private_user, login
from ..middleware import token_required

@auth_routes_bp.route('/', methods=(['GET']))
@token_required
def get_private_user_routes():
    return get_private_user()

@auth_routes_bp.route('/login', methods=(['POST']))
def login_route():
    return login()