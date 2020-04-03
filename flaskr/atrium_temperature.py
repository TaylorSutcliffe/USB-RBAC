import requests



def atrium_temperature():
    data = requests.get('https://api.usb.urbanobservatory.ac.uk/api/v2.0a/sensors/entity?meta:roomNumber=G.062&metric="room temperature"')
    obj = data.json()
    #print(obj['items'][0]['feed'][0]['timeseries'][0]['timeseriesId'])
    timeseriesid = str(obj['items'][0]['feed'][0]['timeseries'][0]['timeseriesId'])

    url = 'https://api.usb.urbanobservatory.ac.uk/api/v2/sensors/timeseries/'+timeseriesid+'/historic?startTime=2020-03-20T13:00:00Z&endTime=2020-03-27T13:00:00Z'
    data2 = requests.get(url)
    obj2 = data2.json()
    obj3 = obj2['historic']['values']

    times = []
    durations = []
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


    
    return date,time,durations,values
