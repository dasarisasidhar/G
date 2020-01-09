from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from G import app
from G import validate
from G import db

@app.route('/')
@app.route('/game')
def game():
    return render_template(
        'player_home.html',
    )

@app.route('/verify_gamecode', methods = ["POST"])
def verify_gamecode():
    game_code = request.form
    if(db.game.is_game_active(game_code["code"]) == True):
        return render_template(
            'get_player_details.html',
            code = str(game_code["code"])
        )
    return "The Game Code You Entered is In-Active, Please Enter correct One"

@app.route('/save_player',  methods = ["POST"])
def save_player():
    details = request.form
    db.game.add_players(dict(details))
    return redirect(url_for('players_dashboard', code = details["code"]))

@app.route('/play_game/<code>')
def play_game(code):
    data = db.game.display_questions_and_options(code)
    if(data == False):
        return render_template(
            'play_game.html',
             error = "Ask Your admin to start the game"
        )
    return render_template(
            'play_game.html',
             q = data[0],
             o = data[1],
             code = code
        )
