from app import routes
from flask import Flask

# Initialize Flask application
app = Flask(__name__)

# Import routes from routes.py

# Ensure the app is run when this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
