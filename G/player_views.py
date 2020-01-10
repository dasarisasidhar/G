from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from G import app
from G import validate
from G import db

@app.route('/')
def welcome():
    return ("Welcome Page")

@app.route('/game')
def game():
    return render_template('player_home.html')

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
    details = dict(request.form)
    details["start_date"] = datetime.now()
    db.game.add_players(details)
    player_name = details["name"]
    return redirect(url_for('players_dashboard', 
                            code = details["code"], 
                            player_name = player_name))

@app.route('/play_game/<code>/<player_name>/<qn>')
def play_game(code, player_name, qn):
    data = db.game.display_questions_and_options(code, qn)
    if(int(qn)<6):
        if(data == False):
            return render_template(
                'play_game.html',
                 error = "Ask Your admin to start the game or error in db"
            )
        return render_template(
                'play_game.html',
                 q = data[0],
                 o = data[1],
                 code = code,
                 date_time = datetime.now(),
                 player_name = player_name,
                 qn = qn
            )
    return redirect(url_for('leader_board', 
                            code = code))
                            
