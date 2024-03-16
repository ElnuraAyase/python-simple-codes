
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the homepage!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'Contact us at example@example.com.'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

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

