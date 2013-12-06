from submarine_app import app
from flask import render_template, redirect, request, current_app, session, flash, url_for

@app.route('/', methods=["GET","POST"])
def index(function=None):
    error = []
    return render_template('index.html', error=error)

@app.route('/up')
def up():
    error = []
    print "up was processed."
    return render_template('index.html', error=error)

@app.route('/down')
def down():
    error = []
    print "down was processed"
    return render_template('index.html', error=error)

@app.route('/left')
def left():
    error = []
    print "left was processed"
    return render_template('index.html', error=error)

@app.route('/right')
def right():
    error = []
    print "right was processed"
    return render_template('index.html', error=error)
