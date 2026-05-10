class PublicSaves:
    def __init__(self, data):
        self.public_saves = data 

    def create_public_saves():
        return {}

class PlayerProfile:
    def __init__(self, data):
        self.player_profile = data 

    def create_player_profile():
        return {}
        
class Player:
    def __init__(self, player_data):
        self.player_data = player_data
        self.unique_id = player_data['unique_id']
        self.username = player_data['username']
        self.mind_palaces = player_data["mind_palaces"]

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

    def create_mind_palace(unique_id, name):
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

    