
from datetime import datetime
from flask import render_template
from flask import request
from G import app
from G import validate
from G import db

@app.route('/')
@app.route('/game')
def game():
    return render_template(
        'player_home.html',
    )

@app.route('/game',methods = ["POST"])
def play_game():
    game_code = dict(request.form)
    if(db.is_game_active(game_code) == True):
        return render_template(
            'player_details.html'
        )
    return "The Game Code You Entered is In-Active, Please Enter correct One"




