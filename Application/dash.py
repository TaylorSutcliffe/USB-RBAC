from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import json
from flask_sqlalchemy import SQLAlchemy
#import db


app = Flask(__name__)
users = json.load(open('users.json'))
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in users["users"]:
            if username == user['username'] and password == user['password']:
                #session['username'] = username
                return redirect(url_for('index'))
            else: 
                flash('login failed')

        #if user and password == user.password:
        #    session['username'] = user.username
        #    return redirect(url_for('index'))
        #else: 
        #    flash('login failed')
     return render_template('login.html')



if __name__ == '__main__':
	app.run()
