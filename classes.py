class Location:
    def __init__(self, location): # {new_loc:{}}
        self.location = location
        self.name = location.get("name", "Unknown")
        self.description = location.get("description", "Unknown")
        self.exits = location.get("exits", [])
        
    def change_name(self,new_name):
        self.location["name"] = new_name
        print(f"Location now named: {new_name}.")

    def change_description(self,new_description):
        self.description = new_description

    def add_exit(self, exit):
        self.exits.append(exit)

    