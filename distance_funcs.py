import requests, json, os, math
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv('FLIGHTAWARE_KEY')
 


def update_json(lat1, long1, lat2, long2):
    api_url = "https://aeroapi.flightaware.com/aeroapi"
    lat_long_string = f'-latlong "{lat1} {long1} {lat2} {long2}"'
    us_bounding = {"query": lat_long_string}

    AeroAPI = requests.Session()
    AeroAPI.headers.update({"x-apikey": access_key})

    result = AeroAPI.get(f"{api_url}/flights/search", params=us_bounding)
    bounded_flights = result.json()

    with open("bounded.json", 'w', encoding='utf-8') as f:
        json.dump(bounded_flights, f, ensure_ascii=False, indent=4) 

def find_closest_flight(fire_lat, fire_long): 
    #pythagorian theorum for flight with closest lat/long
    with open("data.json", 'r', encoding='utf-8') as r:
        reloaded_json = json.load(r)
    closest_flight = min(reloaded_json["flights"], key = lambda x: math.sqrt(abs(fire_lat - x["last_position"]["latitude"])**2 + abs(fire_long - x["last_position"]["longitude"])**2))
    return closest_flight["last_position"]["latitude"], closest_flight["last_position"]["longitude"]

def next_x_waypoints(x_points: int, flight, get_all = False):
    packaged_waypoints = [flight["waypoints"][i:i+2] for i in range(0, len(flight["waypoints"]), 2)]

    if len(flight["waypoints"]) == 0:
        print("No waypoints available for flight " + flight["ident"])
    elif get_all:
        return packaged_waypoints
    else: 
        current_position = flight["last_position"]["latitude"], flight["last_position"]["longitude"]
        closest_waypoint = min(flight["waypoints"], key = lambda x: math.sqrt(abs(packaged_waypoints[x][0] - flight["last_position"]["latitude"])^2 + abs(packaged_waypoints[x][1] - flight["last_position"]["longitude"])^2))
        #^still broken, x needs to be only integers to be an index
        print("current position: " + str(current_position))
        return closest_waypoint

def find_closest_route(fire_lat, fire_long):
    flight_with_closest_waypoint = 2


if __name__ == "__main__": 

    print(json.dumps(find_closest_flight(35.09, -90.88), indent=4))
    #print(find_closest_flight(35, -90))
    #example_flight = us_flights["flights"][2]
    #next_x_waypoints(5, example_flight)