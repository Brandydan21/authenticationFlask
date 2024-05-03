from . import current_app
def get_user():
    return current_app.config['SECRET_KEY']