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
