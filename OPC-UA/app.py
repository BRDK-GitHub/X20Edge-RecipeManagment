from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/call_function', methods=['POST'])
def call_function():
    data = request.get_json()
    if data is None:
        return jsonify(error="No JSON data")
    
    # Access a specific element from the JSON data
    input_recipe = data.get('recipe')
    if input_recipe is None:
        return jsonify(error="No 'recipe' field in JSON data")
    
    # Convert the nested JSON to a 2-dimensional array
    result = json_to_2d_array(input_recipe)
    
    return jsonify(result)

def json_to_2d_array(json_data):
    array = []
    for key, value in json_data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                array.append([key, sub_key, sub_value])
        else:
            array.append([key, value])
    print(array, flush=True)
    return array

if __name__ == '__main__':
    app.run(host='0.0.0.0')