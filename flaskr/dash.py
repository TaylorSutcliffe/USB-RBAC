from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flaskr import lightlevel_3015, occupancy_3015, humidity_6025, humidity_6025, occupancy_4005, CO2_4005, atrium_temperature
import numpy as np
import pandas as pd
import matplotlib as mpl
import datetime
import matplotlib.ticker as ticker



bp = Blueprint('dash', __name__)

@bp.route('/')
def redr():
    return redirect(url_for('dash.index', room = 'G.062'))

@bp.route('/<string:room>/')
def index(room):
    #check if user has permission to be on room page

    #if so generate appropriate visulisation 
    plot1 = generateVis(room)

    #add array to variable with plots
    #modify the index.html to display this 
    return render_template('dash/index.html', room=room, plot=plot1)


def generateVis(room):
   
    fig = Figure(figsize=(20,10),dpi=100)
    if(room == 'G.062'):
        atrium_temperature_date,atrium_temperature_time,atrium_temperature_durations,atrium_temperature_values = atrium_temperature.atrium_temperature()
        df = dtCreate(atrium_temperature_date, atrium_temperature_time, atrium_temperature_values)
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title("Atrium Temp")
        
        axis.set_ylabel("temp (oC)")
        axis.grid() 
        
        axis.plot_date(df['x'], df['y'], xdate=True, linestyle="-")
    
    if(room == '3.015'):

        #lightlevel_3015.lightlevel_3015()
        lightlevel_3015_date,lightlevel_3015_time,lightlevel_3015_durations,lightlevel_3015_values = lightlevel_3015.lightlevel_3015()
        df5 = dtCreate(lightlevel_3015_date, lightlevel_3015_time, lightlevel_3015_values)
        
        #occupancy_3015.occupancy_3015()
        occupancy_3015_date,occupancy_3015_time,occupancy_3015_durations,occupancy_3015_values = occupancy_3015.occupancy_3015()
        df2 = dtCreate(occupancy_3015_date, occupancy_3015_time, occupancy_3015_values)
        
        ax2 = fig.add_subplot(2, 1, 1)
        ax2.set_title("occupancy 3015")
        ax2.set_xlabel("time")
        ax2.set_ylabel("occupancy")
        ax2.grid()
        tick_spacing = 1

        ax2.set_yticks([0, 1])
        ax2.plot_date(df2['x'], df2['y'], xdate=True, linestyle="-", drawstyle = "steps")

        if (g.user['role'] == 'buildingmanager'):
            ax5 = fig.add_subplot(2, 1, 2)
            ax5.set_title("lightlevel 3015")
            ax5.set_xlabel("time")
            ax5.set_ylabel("nit")
            ax5.grid()
            tick_spacing5 = 1
            ax5.plot_date(df5['x'], df5['y'], xdate=True, linestyle="-")

    if(room == '4.005'):
        #occupancy_4005.occupancy_4005()
        occupancy_4005_date,occupancy_4005_time,occupancy_4005_durations,occupancy_4005_values = occupancy_4005.occupancy_4005()
        CO2_4005_date,CO2_4005_time,CO2_4005_durations,CO2_4005_values = CO2_4005.C02_4005()
        
        df3 = dtCreate(occupancy_4005_date,occupancy_4005_time,occupancy_4005_values )
        df8 = dtCreate(CO2_4005_date,CO2_4005_time,CO2_4005_values)

        if (g.user['role'] == 'buildingmanager'):
            ax3 = fig.add_subplot(2, 1, 2)
            ax3.set_title("occupancy 4005")
            ax3.set_xlabel("time")
            ax3.set_ylabel("occupancy")
            ax3.grid()
            ax3.plot_date(df3['x'], df3['y'], xdate=True, linestyle="-", drawstyle = "steps")

        if (g.user['role'] == 'buildingmanager' or g.user['role'] =='safetyofficer'):
            ax4 = fig.add_subplot(2, 1, 1)
            ax4.set_title("CO2 4005")
            ax4.set_xlabel("time")
            ax4.set_ylabel("CO2 concentration")
            ax4.grid()
            ax4.plot_date(df8['x'], df8['y'], xdate=True, linestyle="-")
            ax4.fill_between(df8['x'], df8['y'], 1000, where = (df8['y'] > 1000), facecolor = 'r')

    if(room == '6.025'):
        humidity_6025_date,humidity_6025_time,humidity_6025_durations,humidity_6025_values = humidity_6025.humidity_6025()
        df6 = dtCreate(humidity_6025_date,humidity_6025_time,humidity_6025_values )

        ax6 = fig.add_subplot(1, 1, 1)
        ax6.set_title("humidity")
        ax6.set_xlabel("time")
        ax6.set_ylabel("cd/m2")
        ax6.grid()
        ax6.plot_date(df6['x'], df6['y'], xdate=True, linestyle="-")

    fig.tight_layout()

    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)


    FigureCanvas(fig).print_png(pngImage)

    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String


def dtCreate(dateArray, timeArray, valuesArray):
    dfd = []
    for i,j in zip(dateArray, timeArray):
        dfd.append(pd.to_datetime(f"{i}T{j}"))
    df = pd.DataFrame({'x': dfd, 'y': valuesArray})
    return df    
        