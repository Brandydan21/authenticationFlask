from ..models import User


def get_user():
    user = User.query.get(1).username

    return user