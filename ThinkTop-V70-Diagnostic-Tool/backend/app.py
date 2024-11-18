from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

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
    # Example data structure for status; replace with actual values as needed
    status_data = {
        "SV1": True,       # Main Valve input from PLC
        "SV2": False,      # Upper Seat input from PLC
        "SV3": True,       # Lower Seat input from PLC
        "EN": True,        # Main Valve feedback
        "USL": False,      # Upper Seat feedback
        "LSP": True        # Lower Seat feedback
    }
    return jsonify(status_data)



##### End of app.py #####
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')