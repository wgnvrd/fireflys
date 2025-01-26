from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
import numpy as np
import firms_API as fPI
import distance_funcs as dist

app = Flask(__name__, static_folder="static")
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(f"{app.static_folder}/assets", filename)
     

@app.route('/flights', methods=['POST'])
def flights():
    data = request.json
    confidence_range = data.get('conf_ranges', [])
    f_coord = fPI.firms_API(confLwrBnd=confidence_range["low"], confUpperBnd=confidence_range["high"]) #feed in box and conf if necessary
    fire_flights = []
    for entry in f_coord:
        x, y = entry['lat'], entry['lon']
        fire_flights += [dist.find_closest_flight(x,y)]
    # print(confidence_range)
    # print(fire_flights)
    # print(bounds)
    return {
        "fireCoordinates": f_coord,
        "fireFlights": fire_flights
    }


# @app.route('/analyze', methods=['POST'])
# def analyze():
#     data = request.json
#     numbers = data.get('numbers', []) 
#     # Perform some data analysis
#     if numbers:
#         array = np.array(numbers)
#         result = {
#             'mean': np.mean(array).item(),
#             'sum': np.sum(array).item(),
#             'count': len(array),
#         }
#         print(result)
#         return jsonify(result)
#     else:
#         return jsonify({'error': 'No data provided'}), 400
#     return str(result)

if __name__ == '__main__':
    app.run(debug=True)