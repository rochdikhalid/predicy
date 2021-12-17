from flask import Flask



# Flask initiation
app = Flask(__name__)
# To secure configuration
app.config['SECRET_KEY'] = 'Hard to guess who I am'

from core import routes
