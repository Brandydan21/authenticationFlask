from . import auth_routes_bp
from ..controllers import get_private_user
from ..middleware import token_required

@auth_routes_bp.route('/', methods=(['GET']))
@token_required
def get_private_user_routes():
    return get_private_user()