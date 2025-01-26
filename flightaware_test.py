import requests, json, os, math
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
    #pythagorian theorum for flight with closest lat/long
    closest_flight = min(us_flights["flights"], key = lambda x: math.sqrt(abs(fire_lat - x["last_position"]["latitude"])^2 + abs(fire_long - x["last_position"]["longitude"])^2))
    return closest_flight["last_position"]["latitude"], closest_flight["last_position"]["longitude"]

def next_x_waypoints(x_points, flight):
    if len(flight["waypoints"]) == 0:
        print("No waypoints available for flight " + flight["ident"])
    else: 
        current_position = flight["last_position"]["latitude"], flight["last_position"]["longitude"]
        for i in range(0, len(flight["waypoints"]), 2):
                
            

def find_closest_route(fire_lat, fire_long):
    flight_with_closest_waypoint = 2


if __name__ == "__main__": 
    with open("us_flights.json", 'w', encoding='utf-8') as f:
        json.dump(us_flights, f, ensure_ascii=False, indent=4) 
    #print(json.dumps(find_closest(35, -90), indent=4))
    #print(find_closest(35, -90))
    example_flight = us_flights["flights"][2]
    next_x_waypoints(10, example_flight)