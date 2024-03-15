from flask import Flask, jsonify  # Import the Flask framework and jsonify function

app = Flask(__name__)  # Create a Flask application instance

# Define a route for '/api/hello' that handles GET requests
@app.route('/api/hello', methods=['GET'])
