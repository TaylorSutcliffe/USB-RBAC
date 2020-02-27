from flask import Flask
from flask_sqlalchemy import SQLAlchemy


'''
db = SQLAlchemy() 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

def initialization(app):
	app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
	db.init_app(app)
    



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    role = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username'''