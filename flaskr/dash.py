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
from flaskr import lightlevel_3015
from flaskr import occupancy_3015
from flaskr import humidity_6025
from flaskr import occupancy_4005
from flaskr import CO2_4005
from flaskr import atrium_temperature 
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


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

    
    #lightlevel_3015.lightlevel_3015()
    #lightlevel_3015_date,lightlevel_3015_time,lightlevel_3015_durations,lightlevel_3015_values = lightlevel_3015.lightlevel_3015()
    
    #occupancy_3015.occupancy_3015()
    #occupancy_3015_date,occupancy_3015_time,occupancy_3015_durations,occupancy_3015_values = occupancy_3015.occupancy_3015()
   
    
    #humidity_6025.humidity_6025()
    #humidity_6025_date,humidity_6025_time,humidity_6025_durations,humidity_6025_values = humidity_6025.humidity_6025()
   
    
    #occupancy_4005.occupancy_4005()
    #occupancy_4005_date,occupancy_4005_time,occupancy_4005_durations,occupancy_4005_values = occupancy_4005.occupancy_4005()
   

    #CO2_4005.C02_4005()
    #CO2_4005_date,CO2_4005_time,CO2_4005_durations,CO2_4005_values = CO2_4005.C02_4005()
   

    #atrium_temperature.atrium_temperature()
    atrium_temperature_date,atrium_temperature_time,atrium_temperature_durations,atrium_temperature_values = atrium_temperature.atrium_temperature()

    df = pd.DataFrame({'x':atrium_temperature_date,'y':atrium_temperature_values})
    #df.plot('x','y',kind='scatter')
    
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("title")
    axis.set_xlabel("x-axis")
    axis.set_ylabel("y-axis")
    axis.grid()
    axis.plot(df['x'], df['y'], "ro-")

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)


    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String

