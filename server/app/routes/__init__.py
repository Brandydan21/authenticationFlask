from flask import Blueprint


view_routes_bp = Blueprint('view_routes_bp',__name__)
auth_routes_bp = Blueprint('auth_routes_bp',__name__)

from . import view, auth