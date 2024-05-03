from . import current_app
def get_private_user():
    return 'private' + current_app.config['SECRET_KEY']