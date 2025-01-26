from dotenv import load_dotenv
import os
import pandas as pd
import distance_funcs as dist

load_dotenv()

MAP_KEY = os.getenv('FIRMS_MAP_KEY')


url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + str(MAP_KEY) + '/MODIS_NRT/-125,25,-64,50/10' #url and filter bounds for contigous US


dat = pd.read_csv(url) # data from url

confLwrBnd = 50.0
confUpperBnd = 100.0

det = dat.sort_values(by='confidence' , ascending=False)

det = det[det["confidence"] >= confLwrBnd] # detected fires of concern
det = det[det['confidence'] <= confUpperBnd] #filter out confirmed fires

lat = det["latitude"].to_numpy()
lon = det["longitude"].to_numpy()

for (x, y) in zip(lat, lon):
    print(dist.find_closest(float(x), float(y)))




















