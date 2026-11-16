from flask import Flask

app = Flask(__name__)

# Home Module
@app.route('/')
def home():
    return """
    <h1>My Web Application</h1>
    <p>Welcome to my Flask application.</p>
    <a href="/about">About</a><br>
    <a href="/contact">Contact</a>
    """

# About Module
@app.route('/about')
def about():
    return """
    <h1>About Us</h1>
    <p>This is a simple Flask web application.</p>
    <a href="/">Home</a>
    """

# Contact Module
@app.route('/contact')
def contact():
    return """
    <h1>Contact</h1>
    <p>Email: student@example.com</p>
    <p>Phone: 9876543210</p>
    <a href="/">Home</a>
    """

if __name__ == '__main__':
    app.run()
