from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
#from . import vis
#from vis import generateVis

import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import lightlevel_3015,occupancy_3015,humidity_6025,occupancy_4005,CO2_4005,atrium_temperature 
 


bp = Blueprint('dash', __name__)

@bp.route('/')
def redr():
    return redirect(url_for('dash.index', room = 'G.062'))

@bp.route('/<string:room>/')
def index(room):
    #check if user has permission to be on room page

    #if so generate appropriate visulisation 
    plot1 = generateVis()

    #add array to variable with plots
    #modify the index.html to display this 
    return render_template('dash/index.html', room=room, plot=plot1)


def generateVis():
    #example visulisation replace with appropriate
    lightlevel_3015.lightlevel_3015()
    date,time,durations,values = lightlevel_3015.lightlevel_3015()
    print(date)
    occupancy_3015.occupancy_3015()
    humidity_6025.humidity_6025()
    occupancy_4005.occupancy_4005()
    CO2_4005.CO2_4005()
    atrium_temperature.atrium.temperature()
    
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(range(5), range(5), "ro-")

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)


    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

