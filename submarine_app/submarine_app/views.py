from submarine_app import app
from flask import render_template, redirect, request, current_app, session, flash, url_for
@app.route('/')
def index():
    return render_template('index.html')
