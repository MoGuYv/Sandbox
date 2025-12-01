from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage view."""
    return '<h1>Welcome to the Flask App!</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Greet the user."""
    if name:
        return f'<h1>Hello, {name}!</h1>'
    return '<h1>Hello!</h1>'

@app.route('/convert/<celsius>')
def convert(celsius):
    """Convert Celsius to Fahrenheit."""
    try:
        celsius = float(celsius)
        fahrenheit = celsius * 9.0 / 5.0 + 32
        return f'<h1>{celsius}°C is {fahrenheit:.1f}°F</h1>'
    except ValueError:
        return '<h1>Invalid temperature value. Please enter a number.</h1>'

if __name__ == '__main__':
    app.run(debug=True)
