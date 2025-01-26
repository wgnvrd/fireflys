from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

MAP_KEY = os.getenv('FIRMS_MAP_KEY')


url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' + str(MAP_KEY) + '/MODIS_NRT/-125,25,-64,50/10' #url and filter bounds for contigous US

# def get_transaction_count() :
#   count = 0
#   try:
#     df = pd.read_json(url,  typ='series')
#     count = df['current_transactions']
#   except:
#     print ("Error in our call.")
#   return count

# print(get_transaction_count())

dat = pd.read_csv(url) # data from url

confLwrBnd = 50.0
confUpperBnd = 100.0

det = dat[dat["confidence"] >= confLwrBnd] # detected fires of concern
det = det[det['confidence'] <= confUpperBnd] #filter out confirmed fires

# print(det.describe()) # debug and verify confidence filtered correctly

det = det.sort_values(by='confidence' , ascending=False)











