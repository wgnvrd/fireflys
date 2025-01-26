import requests, json, os
from dotenv import load_dotenv
load_dotenv()



id = "UAL1234-1234567890-airline-0123" #example

access_key = os.getenv('FLIGHTAWARE_KEY')
print(access_key)
 
api_url = "https://aeroapi.flightaware.com/aeroapi"
params = {"query":'-latlong "50 -130 25 -60"'}

AeroAPI = requests.Session()
AeroAPI.headers.update({"x-apikey": access_key})

result = AeroAPI.get(f"{api_url}/flights/search", params=params)
us_flights = result.json()
with open("us_flights.json", 'w', encoding='utf-8') as f:
    json.dump(us_flights, f, ensure_ascii=False, indent=4) 
