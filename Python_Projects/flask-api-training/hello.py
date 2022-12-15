from flask import Flask
from flask import request  # request captures the http request object
from flask import make_response  # make_response function is used to generate a response object

# that can be returned from the Flask view fuction.

application = Flask(__name__)


@application.route("/")
def home():
    return "<h1>HOME PAGE</h1>"


@application.route("/about")
def about():
    return "<h1>ABOUT PAGE</h1>"


@application.route("/user/<name>")
def user(name):
    return f"<h1>HELLO {name}!</h1>"


@application.route("/index")
def index():
    user_agent = request.headers.get('User-Agent')
    return f"<p>Your browser is {user_agent}</p>"


@application.route("/response_example")
def response_ex():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
