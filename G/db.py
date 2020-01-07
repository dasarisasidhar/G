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
            game_details_by_code = game_details.find_one({code:str(game_code)})
            if(game_details_by_code["code"] == code):
                return True
            return False
        except Exception as e:
            print(e)
            return False

    def start_game(details):
          try:
            game_details_by_code = game_details.find_one({code:str(details["code"])})
            if(game_details_by_code["code"] == details["code"] and game_details_by_code["pid"] == details["pid"]):
                game_details.find_one_and_update({'code': game_details_by_code["code"]}, {"start": True})
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
            players = player_details.find({code:str(game_code)})
        except Exception as e:
            print(e)
            return False
        
