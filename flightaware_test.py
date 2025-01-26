import requests, json, os
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv('FLIGHTAWARE_KEY')
 
api_url = "https://aeroapi.flightaware.com/aeroapi"
params = {"query":'-latlong "50 -130 25 -60"'}

AeroAPI = requests.Session()
AeroAPI.headers.update({"x-apikey": access_key})

result = AeroAPI.get(f"{api_url}/flights/search", params=params)
us_flights = result.json()

def find_closest(fire_lat, fire_long):
    closest_flight = min(us_flights["flights"], key = lambda x: abs(fire_lat - x["last_position"]["latitude"]) + abs(fire_long - x["last_position"]["longitude"]))
    return closest_flight

if __name__ == "__main__": 
    with open("us_flights.json", 'w', encoding='utf-8') as f:
        json.dump(us_flights, f, ensure_ascii=False, indent=4) 
    print(json.dumps(find_closest(35, -90), indent=4))