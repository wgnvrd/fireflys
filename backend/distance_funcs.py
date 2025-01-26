import requests, json, os, math
from dotenv import load_dotenv
load_dotenv()

access_key = os.getenv('FLIGHTAWARE_KEY')
"""
api_url = "https://aeroapi.flightaware.com/aeroapi"
us_bounding = {"query": '-latlong "50 -130 20 -60"'}

AeroAPI = requests.Session()
AeroAPI.headers.update({"x-apikey": access_key})

result = AeroAPI.get(f"{api_url}/flights/search", params=us_bounding)
print(result)
bounded_flights = result.json()

with open("backend/bounded_flights.json", 'w', encoding='utf-8') as f:
    json.dump(bounded_flights, f, ensure_ascii=False, indent=4) 
"""
def update_json(lat1, long1, lat2, long2):
    api_url = "https://aeroapi.flightaware.com/aeroapi"
    lat_long_string = '-latlong "' + str(lat1) + ' ' + str(long1) + ' ' + str(lat2) + ' ' + str(long2) + '"'
    print(lat_long_string)
    us_bounding = {"query":lat_long_string}

    AeroAPI = requests.Session()
    AeroAPI.headers.update({"x-apikey": access_key})

    result = AeroAPI.get(f"{api_url}/flights/search", params=us_bounding)
    bounded_flights = result.json()

    with open("backend/bounded_flights.json", 'w', encoding='utf-8') as f:
        json.dump(bounded_flights, f, ensure_ascii=False, indent=4) 

update_json(46, -124, 41, -116)

def find_closest_flight(fire_lat, fire_long): 
    #pythagorian theorum for flight with closest lat/long
    with open("backend/bounded_flights.json", 'r', encoding='utf-8') as r:
        bounded_flights = json.load(r)
    closest_flight = min(bounded_flights["flights"], key = lambda x: math.sqrt(abs(fire_lat - x["last_position"]["latitude"])**2 + abs(fire_long - x["last_position"]["longitude"])**2))
    return closest_flight["last_position"]["latitude"], closest_flight["last_position"]["longitude"], closest_flight["last_position"]["heading"], closest_flight["ident"]

def find_all_flights(fire_lat, fire_long):
    with open("backend/bounded_flights.json", 'r', encoding='utf-8') as r:
        bounded_flights = json.load(r)
    a, b, closest_ident = find_closest_flight(fire_lat, fire_long)

    all_lat_long_heading = [[x["last_position"]["latitude"], x["last_position"]["longitude"], x["last_position"]["heading"], x["ident"], (x["ident"] == closest_ident)] for x in bounded_flights["flights"]]
    #lat, long, heading, ident, is_closest

    return all_lat_long_heading

def next_x_waypoints(x_points: int, flight, get_all = False):
    packaged_waypoints = [flight["waypoints"][i:i+2] for i in range(0, len(flight["waypoints"]), 2)]

    if len(flight["waypoints"]) == 0:
        print("No waypoints available for flight " + flight["ident"])
    elif get_all:
        return packaged_waypoints
    else: 
        current_position = flight["last_position"]["latitude"], flight["last_position"]["longitude"]
        #in the list of alternating lat, long, lat, long, find the pair that's physically closest to the current position by pythagorian
        min_distance = float('inf')
        closest_waypoint = None
        closest_index = -1
        for i in range(len(packaged_waypoints)):
            lat, long = packaged_waypoints[i]
            distance = math.sqrt((lat-current_position[0])**2+(long-current_position[1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_waypoint = (lat, long)
                closest_index = 1

        print("current position: " + str(current_position))
        return closest_waypoint

def find_closest_route(fire_lat, fire_long):
    flight_with_closest_waypoint = 2
    ident = 2
    return ident

if __name__ == "__main__": 
    
    update_json(46, -124, 41, -116)
    """
    print(json.dumps(find_closest_flight(35.09, -90.88), indent=4))

    all_flights = find_all_flights(33, -92)
    print(all_flights)

    #print(find_closest_flight(35, -90))
    #example_flight = us_flights["flights"][2]
    #next_x_waypoints(5, example_flight)
    """
    fire_lat = 40
    fire_long = -100
    lat, long, heading, ident = find_closest_flight(fire_lat, fire_long)
    print(lat)
    with open("backend/bounded_flights.json", 'r', encoding='utf-8') as r:
        bounded_flights = json.load(r)

    print(len(bounded_flights["flights"]))
