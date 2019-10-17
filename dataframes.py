import numpy as np
import pandas as pd
core = pd.read_csv('pitchdata2019.csv',header=0)

zone = pd.DataFrame()
zone['Target']=core['description']
zone['PitchVert']=core['plate_z']
zone['PitchHor']=core['plate_x']

null_zone = zone[zone.isnull().any(axis=1)] #stores null rows in separate dataframe
zone = zone.dropna()  #removes nulls from dataframe