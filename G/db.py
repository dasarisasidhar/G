from pymongo import MongoClient
import datetime
client = MongoClient()
client = MongoClient('localhost', 27017) #mongo_db uses local host to store data
db = client['game']
game_details = db['game_details']
player_details = db['player_details']

class game:
    def __init__(self):
        pass

    def save(details):
        try:
            game_details.insert_one(details) #save game to db
            return True  
        except Exception as e:
            print(e)
            return False

    def is_game_active(game_code):
        try:
            game_details_by_code = game_details.find_one({"code":str(game_code)})
            if(game_details_by_code["code"] == game_code):
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def is_game_started(game_code):
        try:
            game_details_by_code = game_details.find_one({"code":str(game_code)})
            if(game_details_by_code["start"] == True):
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def start_game(details):
          try:
            game_details_by_code = game_details.find_one({"code":str(details["code"])})
            if(game_details_by_code["code"] == details["code"] and game_details_by_code["p"] == details["p"]):
                game_details.find_one_and_update({'code': game_details_by_code["code"]}, {'$set': {'start': True}})
                return True
            return False
          except Exception as e:
            print(e)
            return False
       
    def add_players(details):
        try:
           player_details.insert_one(details)
           return True
        except Exception as e:
            print(e)
            return False

    def display_players(game_code):
        try:
            player_names = []
            players = player_details.find({"code":str(game_code)})
            for player in players:
                player_names.append(player["name"])
            return player_names
        except Exception as e:
            print(e)
            return False
        
    def display_questions_and_options(code):
        try:
            game_details_by_code = game_details.find_one({"code":str(code)})
            if(game_details_by_code["start"] == True):
                q = game_details_by_code["q1"]
                o = tuple()
                o = (game_details_by_code["o1"], game_details_by_code["o2"],
                         game_details_by_code["o3"], game_details_by_code["o4"])
                return (q, o)
            return False
        except Exception as e:
            print(e)
            return False

    def check_ans(code, q, o):
        try:
            data = game_details.find_one({"code":str(code)})
            if(data["start"] == True):
                if(o == data["ans"]):
                    return True
            return False
        except Exception as e:
            print(e)
            return False