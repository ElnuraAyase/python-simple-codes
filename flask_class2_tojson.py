from flask import Flask, request, jsonify  # Import Flask, request, and jsonify from Flask framework

app = Flask(__name__)  # Create a Flask application instance

# Define a route for '/api/add' that handles POST requests
@app.route('/api/add', methods=['POST'])
def add_numbers():
    # Extract the JSON data from the request
    data = request.json
    # Check if 'num1' and 'num2' are provided in the JSON data
    if 'num1' in data and 'num2' in data:
        # Calculate the sum of 'num1' and 'num2'
        result = data['num1'] + data['num2']
        # Return the result as a JSON response
        return jsonify({'result': result}), 200

    else:
        # If 'num1' or 'num2' is missing, return an error message
        return jsonify({'error': 'Please provide both num1 and num2.'}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode if the script is executed directly
