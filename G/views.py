"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from G import app
from G import validate
from G import db

@app.route('/')
@app.route('/play')
def play():
    return render_template(
        'game_home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/play',methods = ["POST"])
def play_game():
    return render_template(
        'player_details.html',
        title='Game Page',
        year=datetime.now().year,
    )

@app.route('/create_game')
def create_game():
    """Renders the home page."""
    return render_template(
        'create_game.html',
        title='create your game',
        year=datetime.now().year,
    )
@app.route('/start_game')
def start_game():
    """Renders the home page."""
    return render_template(
        'start_game.html',
        title='create your game',
        year=datetime.now().year,
    )

@app.route('/create_game', methods = ["POST"])
def create_game_post():
    details = dict(request.form)
    code = validate.create_gamecode()
    details["code"] = code
    details["start"] = False
    db.game.save(details)
    return render_template(
        'game_code.html',
        title='Game Code',
        year=datetime.now().year,
        code = code
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Sasidhar D.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
