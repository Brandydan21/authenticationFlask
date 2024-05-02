from os import path, environ

BASE_DIR = path.abspath(path.dirname(__file__))


class Config:
    SECRET_KEY = '1234'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIR, 'app.db')
    SQL_TRACK_MODIFICATIONS = False

class DevConfig:
    pass

class ProdConfig:
    pass