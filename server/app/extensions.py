from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app, request, jsonify, session
import jwt
from datetime import datetime, timedelta
from functools import wraps


db = SQLAlchemy()
migrate = Migrate()