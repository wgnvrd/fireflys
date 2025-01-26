from dotenv import load_dotenv
import os
import pandas as pd
import distance_funcs as dist

load_dotenv()

def firms_API(W = -125.0 , S = 25.0, E = -64.0, N = 50.0, confLwrBnd = 50.0, confUpperBnd = 100.0):
    MAP_KEY = os.getenv('FIRMS_MAP_KEY')


    url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + str(MAP_KEY) + '/MODIS_NRT/'+ str(W) + str(S) + str(E) + str(N) +'/10' #url and filter bounds for contigous US


    dat = pd.read_csv(url) # data from url

    #confLwrBnd = 50.0
    #confUpperBnd = 100.0

    det = dat.sort_values(by='confidence' , ascending=False)

    det = det[det["confidence"] >= confLwrBnd] # detected fires of concern
    det = det[det['confidence'] <= confUpperBnd] #filter out confirmed fires

    lat = det["latitude"].to_numpy()
    lon = det["longitude"].to_numpy()

    
    return dist.find_closest(float(lat), float(long))




















