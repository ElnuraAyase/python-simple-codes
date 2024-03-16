
from flask import Flask, render_template  # Import the Flask class and render_template fUNCTION

app = Flask(__name__)   # Create a Flask application instance

# Define a route for the hmpage
@app.route('/')  
def index():
    return 'Welcome to the homepage!'   # simple string 
# ROUTE PAGE FOR ABOUT
@app.route('/about')
def about():
    return 'This is the about page.'
# ROUTE FOR CONTACT
@app.route('/contact')
def contact():
    return 'Contact us at example@example.com.'
# Define a route that takes a parameter and greets the user with that name
@app.route 
@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'
# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html>
<head>
    <title>Homepage</title>
</head>
<body>
    <h1>Welcome to the homepage!</h1>
</body>
</html>



from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')
  

