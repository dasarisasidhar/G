from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from G import app
from G import validate
from G import db
import random

@app.route('/create_game')
def create_game():
    """Renders the home page."""
    return render_template(
        'create_game.html',
        title='create your game',
        year=datetime.now().year,
    )

@app.route('/create_game', methods = ["POST"])
def create_game_post():
    quiz_details = dict(request.form)
    code = random.randint(0,9999999)
    quiz_details["code"] = str(code)
    quiz_details["start"] = False
    db.game.save(quiz_details)
    return render_template(
        'display_game_code.html',
        code = code
    )

@app.route('/start_game')
def start_game():
    return render_template(
        'start_game.html',
        title='start your game ',
        year=datetime.now().year,
    )

@app.route('/start_game', methods = ["POST"])
def start_game_post():
    game_details_to_start = dict(request.form)
    if(db.game.start_game(game_details_to_start) == True):
        return redirect(url_for('players_dashboard', code = game_details_to_start["code"]))
    else:
        return "Please provide valid details"

@app.route('/players_dashboard/<code>')
def players_dashboard(code):
    players = db.game.display_players(code)
    return render_template(
            'display_players_joined.html',
            players = players,
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

@app.route('/validate', methods = ["POST"])
def validate():
    quiz_details = dict(request.form)
    if(db.game.check_ans(quiz_details["code"], quiz_details["q"], quiz_details["o"]) == "True"):
        ans = True
    ans = False
    return render_template(
        'results.html',
         ans = ans 
    )