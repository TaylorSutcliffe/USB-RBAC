from flask import Flask
import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import db
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        datab = db.get_db()

        user = datab.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
            ).fetchone()

        if user and password == user['password']:
            session['username'] = user['username']
            return redirect(url_for('index'))
        else: 
            flash('login failed')

     return render_template('login.html')