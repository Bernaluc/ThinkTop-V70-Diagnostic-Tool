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

if __name__ == '__main__':
    app.run(debug=True)
