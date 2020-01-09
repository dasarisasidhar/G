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
    quiz_details = dict()
    quiz_details["start_date"] = datetime.now()
    details = dict(request.form)
    for i in range(1,6):
        quiz_details["q"+str(i)] = details["q"+str(i)]
        quiz_details["o"+str(i)] = [details["o"+str(i)+"1"], 
                                                         details["o"+str(i)+"2"],
                                                         details["o"+str(i)+"3"],
                                                         details["o"+str(i)+"4"]]
                                                         
        quiz_details["ans"+str(i)] = details["ans"+str(i)]
    code = random.randint(0,9999999)
    quiz_details["p"] = details["p"]
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
        return "Game Started Lets Play"
    else:
        return "Please provide valid details"

@app.route('/players_dashboard/<code>/<player_name>')
def players_dashboard(code, player_name):
    players = db.game.display_players(code)
    return render_template(
            'display_players_joined.html',
            players = players,
            code = code,
            player_name = player_name
        )

@app.route('/validate', methods = ["POST"])
def validate():
    ans = ""
    quiz_details = dict(request.form)
    qn = int(quiz_details["qn"])
    time_to_solve = ""
    code = quiz_details["code"]
    if(db.game.check_ans(code, qn, quiz_details["o"]) == True):
         question_date_time = datetime.fromisoformat(quiz_details["date_time"])
         time_to_solve = datetime.now()-question_date_time
         ans = db.game.save_player_results(code, qn, time_to_solve, quiz_details["player_name"], is_correct = True)
    else:
        ans = db.game.save_player_results(code, qn, time_to_solve, quiz_details["player_name"], is_correct = False)
    return render_template(
        'results.html',
         ans = ans,
         time_to_solve = time_to_solve,
         player_name = quiz_details["player_name"],
         code = code,
         qn = qn+1
    )

@app.route('/leader_board/<code>')
def leader_board(code):
    players = db.game.get_winners(code)
    return render_template(
        'leading_board.html',
         code = code,
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
