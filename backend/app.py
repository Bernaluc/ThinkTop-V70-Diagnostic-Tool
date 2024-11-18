import json
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# Define IO State file
IO_STATE_FILE = 'io_state.json'

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app) #enable CORS

# Define route for API
@app.route('/api')
def api():
    return jsonify({'message': 'Hello from the API!'})

# Define route for default path
@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')

# Define a route for the Status data
@app.route('/api/status', methods=['GET'])
def get_status():
    print('Get Status..........')
    # Example data structure for status; replace with actual values as needed
    status = read_io_state()
    status_data = {
        "SV1": status[0],       # Main Valve input from PLC
        "SV2": status[1],      # Upper Seat input from PLC
        "SV3": status[2],       # Lower Seat input from PLC
        "EN":  status[3],
        "USL": status[4],
        "LSP": status[5]
    }
    return jsonify(status_data)

# Read IO state from JSON file
def read_io_state():
    try:
        with open(IO_STATE_FILE, "r") as file:
            state = json.load(file)
            # Assuming state has keys "inputs" and "outputs"
            return state.get("inputs", [0, 0, 0])
    except (FileNotFoundError, json.JSONDecodeError):
        # Return default inputs in case of errors
        return [0, 0, 0]


##### End of app.py #####
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')