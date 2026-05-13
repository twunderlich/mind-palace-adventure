class MindPalace:
    def __init__(self, mind_palace_data):
        self.name = mind_palace_data.get("name", "Unknown")
        self.current_id = mind_palace_data.get("current_id", "Unknown")
        self.rooms = mind_palace_data.get("rooms", {})

    def create_mind_palace(self, name):
        return {
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

    