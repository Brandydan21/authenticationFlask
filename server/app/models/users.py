from ..extensions import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True,autoincrement=True)
    username = db.Column("username", db.String, nullable=False)
    password = db.Column("password", db.String, nullable=False )
    
    def __init__(self, username, password):
        self.username = username
        self.password = password


