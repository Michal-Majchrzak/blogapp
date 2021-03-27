from blog import app
from flask import render_template


@app.route('/')
def print_hello():
    return render_template('base.html')
