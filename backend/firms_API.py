from dotenv import load_dotenv
import os
import pandas as pd
import distance_funcs as dist

load_dotenv()

def firms_API(W = -125.0 , S = 25.0, E = -64.0, N = 50.0, confLwrBnd = 50.0, confUpperBnd = 100.0):
    MAP_KEY = os.getenv('FIRMS_MAP_KEY')

    url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + str(MAP_KEY) + '/MODIS_NRT/'+ str(W) + ',' + str(S) + ',' + str(E) + ',' + str(N) +'/10' #url and filter bounds for contigous US


    dat = pd.read_csv(url) # data from url

    #confLwrBnd = 50.0
    #confUpperBnd = 100.0
    # print(dat)

    det = dat.sort_values(by='confidence' , ascending=False)

    det = det[det["confidence"] >= confLwrBnd] # detected fires of concern
    det = det[det['confidence'] <= confUpperBnd] #filter out confirmed fires

    lat = det["latitude"].to_numpy()
    lon = det["longitude"].to_numpy()

    
    # return [{"id": id_num, "lat": lat, "lon": lon} for (id_num, (lat, lon)) in enumerate(zip(lat, lon))]
    return [{"lat": lat, "lon": lon} for (lat, lon) in zip(lat, lon)]





















