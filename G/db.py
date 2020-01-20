from pymongo import MongoClient
from datetime import datetime
# test connection string usin cosmos db
client = MongoClient('mongodb://mongodb4plaython:FQwahfriqW1YtqGHhmRQVzoCuqVruC3vFRoa0ppDHB2J7lR266sQXhzptFDlmmiitwBMXnX80OBfPSTWrEOnfg==@mongodb4plaython.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')
#client = MongoClient('localhost', 27017) #mongo_db uses local host to store data
db = client['game']
game_details = db['game_details']
players = db['players']
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
           players.insert_one(details)
           return True
        except Exception as e:
            print(e)
            return False

    def display_players(game_code):
        try:
            player_names = []
            players_details = players.find({"code":str(game_code)})
            for player in players_details:
                player_names.append(player["name"])
            return player_names
        except Exception as e:
            print(e)
            return False
        
    def display_questions_and_options(code, qn):
        try:
            game_details_by_code = game_details.find_one({"code":str(code)})
            if(game_details_by_code["start"] == True):
                q = game_details_by_code["q"+str(qn)]
                o = tuple(game_details_by_code["o"+str(qn)])
                #o = (game_details_by_code["o"+str(qn)+"1"], game_details_by_code["o"+str(qn)+"2"],
                #         game_details_by_code["o"+str(qn)+"3"], game_details_by_code["o"+str(qn)+"4"])
                return (q, o)
            return False
        except Exception as e:
            print(e)
            return False

    def check_ans(code, qn, o):
        try:
            data = game_details.find_one({"code":str(code)})
            if(data["start"] == True):
                if(o == data["ans"+(str(qn))]):
                    return True
            return False
        except Exception as e:
            print(e)
            return False

    def save_player_results(code, qn, time_to_solve, player_name, is_correct):
        try:
            details = dict()
            game_details_by_code = game_details.find_one({"code":str(code)})
            if(int(qn) == 1 and is_correct == True):
                if(game_details_by_code["start"] == True):
                    details["code"] = code
                    time_to_save = str(time_to_solve.seconds)+":"+str(time_to_solve.microseconds)
                    details["time_to_solve"] = datetime.strptime(time_to_save, '%S:%f')
                    details["player_name"] = player_name
                    details["start_date"] = datetime.now()
                    details["q_answered"] = 1
                    player_details.insert_one(details)
                    return True
                return False
            elif(int(qn) == 1 and is_correct == False):
                if(game_details_by_code["start"] == True):
                    details["code"] = code
                    time_to_save = str(0)+":"+str(0)
                    details["time_to_solve"] = datetime.strptime(time_to_save, '%S:%f')
                    details["player_name"] = player_name
                    details["start_date"] = datetime.now()
                    details["q_answered"] = 0
                    player_details.insert_one(details)
                    return False
                return False
            elif(int(qn) > 1):
                details = player_details.find_one({"code":str(code), "player_name":player_name})
                time_to_solve = details["time_to_solve"]+time_to_solve
                q_answered = details["q_answered"]+1
                player_details.find_one_and_update({"code":str(code),"player_name":player_name},
                                                            {'$set': {'time_to_solve': time_to_solve, "q_answered":q_answered}})
                return True           
        except Exception as e:
            print(e)
            return False

    def get_winners(code):
        try:
            players = list()
            data = player_details.find({"code":str(code)}).sort("time_to_solve", 1).sort("q_answered", -1).limit(5)
            for i in data:
                players.append(i["player_name"])
            return players
        except Exception as e:
            print(e)
            return False