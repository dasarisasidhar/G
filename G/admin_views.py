from datetime import datetime
from flask import render_template
from flask import request
from G import app
from G import validate
from G import db

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
    code = validate.create_gamecode()
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
    if(db.start_game(game_details_to_start) == True):
        return True
   
@app.route("/players_dashboard")
def players_dashboard():
    code = code
    players = db.get_players(game_code)
    render_template(
            'active_player_details.html',
            title='game started! lets play',
            year=datetime.now().year,
            players = players
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
