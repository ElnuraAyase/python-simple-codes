from flask import Flask, jsonify  # Import the Flask framework and jsonify function

app = Flask(__name__)  # Create a Flask application instance

# Define a route for '/api/hello' that handles GET requests
@app.route('/api/hello', methods=['GET'])

def hello():
    return jsonify({'message': 'Hello, World!'})  # Return a JSON response with a message

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
