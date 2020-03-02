from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('dash', __name__)

@bp.route('/')
def redr():
    return redirect(url_for('dash.index', room = 'G.062'))

@bp.route('/<string:room>/')
def index(room):
    #check if user has permission to be on room page

    #if so generate appropriate visulisation 

    #add variable to return with the visulisations and then
    #modify the index.html to display this 
    return render_template('dash/index.html', room=room)