import functools, json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')
users = json.load(open('users.json'))

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        users = json.load(open('users.json'))

        username = request.form['username']
        password = request.form['password']

        for user in users["users"]:
            if username == user['username'] and password == user['password']:
                session['username'] = username
                return redirect(url_for('index', room = 'G.062'))
        


    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    users = json.load(open('users.json'))
    username = session.get('username')

    if username is None:
        g.user = None
    else:
        for user in users["users"]:
            if username == user['username']:
                g.user = user

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index', room = 'G.062'))