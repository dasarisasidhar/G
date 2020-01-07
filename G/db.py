from pymongo import MongoClient
import datetime
client = MongoClient()
client = MongoClient('localhost', 27017) #mongo_db uses local host to store data
db = client['game']
game_details = db['game_details']

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
       
    def add_players(game_code):
