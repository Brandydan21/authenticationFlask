from . import view_routes_bp
from ..controllers import get_user

@view_routes_bp.route('/', methods=(['GET']))
def get_users_routes():
    return get_user()