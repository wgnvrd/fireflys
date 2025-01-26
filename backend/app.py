from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
import firms_API as fPI
import distance_funcs as dist

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flights', methods=['POST'])
def flights():
    fCoord = fPI.firms_API() #feed in box and conf if necessary
    for (x,y) in fCoord:
        print(dist.find_closest_route(x,y))
    data = request.json
    print(data)
    bounds = data.get('bounds', [])
    print(bounds)
    return {}

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