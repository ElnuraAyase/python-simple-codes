from flask import Flask, request, jsonify  # Import Flask, request, and jsonify from Flask framework

app = Flask(__name__)  # Create a Flask application instance

# Define a route for '/api/add' that handles POST requests
@app.route('/api/add', methods=['POST'])
def add_numbers():
    # Extract the JSON data from the request
    data = request.json
