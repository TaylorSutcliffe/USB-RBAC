import requests
import simplejson as json
import numpy as np

def occupancy_3015():
    data= requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?meta:roomNumber=3.015&metric=occupancy')
    obj = data.json()
    #print(obj['items'][0]['feed'][0]['timeseries'][0]['timeseriesId'])
    timeseriesid = str(obj['items'][0]['feed'][0]['timeseries'][0]['timeseriesId'])

    url = 'https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/timeseries/'+timeseriesid+'/historic?startTime=2020-02-20T13:00:00Z&endTime=2020-02-27T13:00:00Z'
    data2 = requests.get(url)
    obj2 = data2.json()
    obj3 = obj2['historic']['values']    
    #print(obj3)    
    times = []
    durations =[]
    values = []


    for val in obj3:
        times.append(val['time'])
        durations.append(val['duration'])
        values.append(val['value'])
    
    #print(times)
    #print(durations)
    #print(values)

    date=[i[:10] for i in times]
    time=[i[11:19]for i in times]
    #print(date)
    #print(time)


    np.savetxt("3.015_occupancy_date.csv",date,delimiter=',',fmt='%s')
    np.savetxt("3.015_occupancy_time.csv",time,delimiter=',',fmt='%s')
    np.savetxt("3.015_occupancy_duration.csv",durations,delimiter=',',fmt='%s')
    np.savetxt("3.015_occupancy_values.csv",values,delimiter=',',fmt='%s')
