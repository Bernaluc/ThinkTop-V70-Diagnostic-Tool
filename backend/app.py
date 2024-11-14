from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='build', static_url_path='/')

# Serve the React frontend

@app.route('/')
@app.route('/<path:path>')
def serve_react(path=None):
    if path is None or not os.path.exists(os.path.join(app.static_folder, path)):
        path = 'index.html'
    return send_from_directory(app.static_folder, path)

# Define your API route
@app.route('/api/status', methods=['GET'])
def get_status():
    status_data = {
        "SV1": True,
        "SV2": False,
        "SV3": True,
        "EN": True,
        "USL": False,
        "LSP": True
    }
    return jsonify(status_data)

# Add valve control API route
@app.route('/api/control', methods=['POST'])
def control():
    data = request.get_json()
    output = data.get('output')
    value = data.get('value')
    
    # Control the valve
    print(f"Received control command: {output} -> {'ON' if value else 'OFF'}")

    # Respond with success
    return jsonify({"status": "success", "output": output, "value": value}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
