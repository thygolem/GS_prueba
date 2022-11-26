from ignitionSQL import Bay
import pandas as pd
import numpy as np

gs = pd.read_csv("IgnitionPrueba.csv", sep=",")

bay1 = pd.DataFrame(gs[['Time', 'Bay 1\\Chiller Status', 'Bay 1\\Temperature', 'Bay 1\\Humidity', 'Bay 1\\Power Draw']])
bay1.columns = ['time', 'chiller status', 'temp', 'hum', 'pwr']

bay2 = pd.DataFrame(gs[['Time', 'Bay 2\\Chiller Status', 'Bay 2\\Temperature', 'Bay 2\\Humidity', 'Bay 2\\Power Draw']])
bay2.columns = ['time', 'chiller status', 'temp', 'hum', 'pwr']

bay3 = pd.DataFrame(gs[['Time', 'Bay 3\\Chiller Status', 'Bay 3\\Temperature', 'Bay 3\\Humidity', 'Bay 3\\Power Draw']])
bay3.columns = ['time', 'chiller status', 'temp', 'hum', 'pwr']

bay4 = pd.DataFrame(gs[['Time', 'Bay 4\\Chiller Status', 'Bay 4\\Temperature', 'Bay 4\\Humidity', 'Bay 4\\Power Draw']])
bay4.columns = ['time', 'chiller status', 'temp', 'hum', 'pwr']




for _ in range(1, len(bay1)):
    bay1Time = bay1.iloc[_]['time']
    bay1Chiller = gs.iloc[_]['Bay 1\Chiller Status']
    bay1Temp = gs.iloc[_]['Bay 1\\Temperature']
    bay1Hum = gs.iloc[_]['Bay 1\\Humidity']
    bay1Pwr = gs.iloc[_]['Bay 1\\Power Draw']
    # print('row: ', _, '| time: ', bay1Time, '| chiller', bay1Chiller,'| temp', bay1Temp,'| hum', bay1Hum,'| pwr', bay1Pwr)
    bay1table = Bay(bay1Time, bay1Chiller, bay1Temp, bay1Hum, bay1Pwr)

print(bay1table)

