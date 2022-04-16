"""
Before running this, we need to set an environment variable
>>>export FLASK_APP=application.py

This will set the environment variable FLASK_APP to application.py
temporarily (until user ends the session)

if you want a permanent variable, need to set bash profile

if you want to check what the environment variable is set as
>>>echo $FLASK_APP

Also remember to activate flask conda environment
>>> conda activate flask
"""

from flask import Flask, render_template, request

#This command says that turn this file is my web application
app = Flask(__name__)

#i want to build an app that has a route listening for slash 
@app.route("/")
#whenever you see a request from some user, call this function (index)
def index():

    return render_template("index.html")

#i want to build an app that has a route listening for "/register"
@app.route("/register", methods=["POST"])
#whenever you see a request from some user, call this function (index)
def register():
    #for POST requests, its request.form.get() - normally it is request.args.get for GET requests
    first_name = request.form.get("First Name")
    last_name = request.form.get("Last Name")
    email = request.form.get("email")
    tier = request.form.get("Tier")

    if not first_name or not last_name or not email:
        return render_template("failure.html")
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        return render_template("failure.html")
    if '@' not in email:
        return render_template("failure.html")
        
    return render_template("success.html",first_name=first_name, last_name=last_name, email=email, tier=tier)