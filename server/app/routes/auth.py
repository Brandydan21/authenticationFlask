from . import auth_routes_bp
from ..controllers import get_private_user

@auth_routes_bp.route('/', methods=(['GET']))
def get_private_user_routes():
    return get_private_user()