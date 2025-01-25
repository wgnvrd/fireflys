MAP_KEY = blah #insert key here

import pandas as pd

url = 'https://firms.modaps.eosdis.nasa.gov/mapserver/mapkey_status/?MAP_KEY=' + MAP_KEY + '/MODIS_NRT/-125,25,-64,50' #url and filter bounds for contigous US

dat = pd.read_csv(url) # data from url

det = dat[dat["confidence"] >= 50.0] # detected fires of concern

det.describe() # debug and verify confidence is above 50

det.sort_values(by = 'confidence')









