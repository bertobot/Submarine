from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig

app = Flask(__name__,static_folder='static',template_folder='templates')
app.config.update(dict(
#        USERNAME='admin',
#        PASSWORD='default'
))
    #print dir(Bootstrap)
    #APP CONFIG need to move to a config file
app.config['SECRET_KEY'] = 'devkey'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

import submarine_app.views

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
