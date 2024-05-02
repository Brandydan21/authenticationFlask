from . import routes_bp

@routes_bp.route('/', methods=(['GET']))
def get_users():
    return 'hi'
