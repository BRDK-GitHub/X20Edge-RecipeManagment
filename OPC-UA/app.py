from flask import Flask, request, jsonify
from flask_cors import CORS
from opcua import Client, ua
import os


# -------------------------------- OPC-UA -----------------------------------------------------
# Define the OPC UA server URL
ip = os.getenv('PLC_IP')
url = "opc.tcp://"+ ip + ":4840"

# Create a client instance
client = Client(url)
def writeOPCValue(valueName, newValue):
    try:
        # Connect to the server
        client.connect()
        print("Connected to OPC UA Server")

        # Read a variable node (replace 'ns=2;i=2' with your node id)
        node = client.get_node("ns=6;s=::" + valueName)
        value = node.get_value()
        print(f"Current value of the node: {value}")

        # Read the data type of the node
        dataType = node.get_data_type_as_variant_type()
        print(f"Data type of the node: {dataType}")

        # Write a new value to the node (replace 'new_value' with the value you want to write)
        variantValue = ua.Variant(newValue, dataType)
        node.set_data_value(ua.DataValue(variantValue))
        print(f"New SINT value written to the node: {newValue}")

        # Verify the new value
        updatedValue = node.get_value()
        print(f"Updated value of the node: {updatedValue}")

    finally:
        # Disconnect from the server
        client.disconnect()
        print("Disconnected from OPC UA Server")

# ---------------------------------- Flask -----------------------------------------------------
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
            writeOPCValue("Main:recipe." + key, value)
    print(array, flush=True)
    return array

if __name__ == '__main__':
    app.run(host='0.0.0.0')