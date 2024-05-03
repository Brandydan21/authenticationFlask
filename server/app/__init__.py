from flask import Flask
from .extensions import db, migrate
from os import environ



def get_settings():
    return environ.get('SETTINGS')



def create_app():

    app = Flask(__name__)
    
    app.config.from_object(get_settings())

    db.init_app(app)

        
    migrate.init_app(app, db)
    
    #this is looking for the models module within the app module

    from . import models
    from .routes import view_routes_bp, auth_routes_bp

    app.register_blueprint(view_routes_bp, url_prefix= '/user')
    app.register_blueprint(auth_routes_bp, url_prefix= '/auth')


    return app
