from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    #render the index page to get what the user ate for breakfast
    return render_template("index.html")

@app.route("/sendbreakfast", methods = ["GET", "POST"])


def results():

    #store the data from the form as the username

    username = dict(request.form)

    breakfast = username['breakfast']
    #print the userdata to the console so that I can see the dictionary
    print("####"*10, username)
    #store and print the value of the breakfast to the console so that I can see it
    #print(username['name'])

    #send the value of breakfast to the results.html page
    return render_template('results.html', breakfast = breakfast)
