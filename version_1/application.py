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
    #1. Simple statement to print sentence
    #return "Hello, Shiva im a Flask Application"

    #2. look at the http request and look for argument called "name"
    #second argument is the default value
    name = request.args.get("name", "Default Value")

    #2. return a template html file called index.html
    return render_template("index.html", name=name)

    #for 2, if i add /?name=Shiva, i will see name=Shiva in my index html file