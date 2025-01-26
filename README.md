# fireflys

You would not believe your eyes..

Reads in data from NASA's FIRMS API used to detect forest fires worldwide, and coordinates with flight data from FlightAware's AeroAPI to find a plane heading in the direction of high likelyhood forest fires to capture better imagery. 

Inspired by a proposal to equip commercial airliners with imaging equipment to obtain enhanced imagery and data about remote wildfires.

Main: gets data from the NASA FIRMS API, filters reports with low confidence out, and produces the coordinates of possible forest fires with high confidence levels.

flightaware_test.py: Gets plane data from the FlightAware AeroAPI to find a plane with coordinates near the fire, who's waypoints (coordinates that track the planes path of flight) are close to the fire. 

The fire could then be reported to the pilots aboard the plane who could choose to fly over the fire equipped with a camera to provide an enhanced imagery to assist in response, and prevent tragedies like those plaguing LA currently.

Uses React with the Leaflet module to load in API data and display on a map, as well as provide a GUI to allow users to adjust desired confidence intervals for possible detected fires.