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
            game_details.insert_one(details) #save user to db
            return True  
        except Exception as e:
            print(e)
            return False