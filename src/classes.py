class PlayerProfile:
    def __init__(self, data):
        self.player_profile = data 

    def create_player_profile():
        return {
            "Guest":{
                "unique_id": "4b546a9f",
                "username": "Guest",
                "mind_palaces": {}
            }
        }
    
    def get_player_profile(self):
        return self.player_profile

    def get_player(self, username):
        return self.player_profile.get(username)
        
class Player:
    def __init__(self, player_data):
        self.player_data = player_data
        self.unique_id = player_data['unique_id']
        self.username = player_data['username']
        self.mind_palaces = player_data["mind_palaces"]


    @staticmethod
    def create_player(unique_id, username):
        return{
             "unique_id": unique_id,
             "username": username,
             "mind_palaces":{}
         }

    def to_dictionary(self):
        return(vars(self))

class MindPalace:
    def __init__(self, mind_palace_data):
        self.unique_id = mind_palace_data.get("unique_id", "unknown")
        self.name = mind_palace_data.get("name", "Unknown")
        self.current_id = mind_palace_data.get("current_id", "Unknown")
        self.rooms = mind_palace_data.get("rooms", {})

    def create_mind_palace(self, unique_id, name):
        return {
        "unique_id": unique_id,
        "name": name,
        "current_id": "Entrance",
        "rooms": {}, 
        }

    def to_dictionary(self):
        return(vars(self))

class Location:
    def __init__(self, location): # {new_loc:{}}
        self.location = location
        self.name = location.get("name", "Unknown")
        self.description = location.get("description", "Unknown")
        self.exits = location.get("exits", [])

    def to_dictionary(self):
        return(vars(self))
        
    def change_name(self,new_name):
        self.location["name"] = new_name
        print(f"Location now named: {new_name}.")

    def change_description(self,new_description):
        self.description = new_description

    def add_exit(self, exit):
        self.exits.append(exit)

    