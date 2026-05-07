from world import location

class gameEngine:
    def __init__(self, current_world):
        self.world = current_world
        self.running = True
        self.commands = {
            "quit": self.quit,
            "look": self.look,
            "move": self.move,
        }   
        current_id = self.world.get('current_id')
        if current_id not in self.world['locations']:
            self.world['locations'][current_id] = {
                "name": current_id,
                "description": "Unkown",
                "exits": []
            }    
        current_location_raw_data = self.world["locations"][current_id]
        self.current_location = location(current_location_raw_data)

    def run(self):
        print(f"Welcome to {self.world['name']}!")
        print(f"You are in the {self.world['current_id']}")

        while self.running:
            user_input = input(">").lower() # makes it not case sensitive

            if user_input in self.commands:
                self.commands[user_input]() # runs the command

            else:
                print(f"You tried to: {user_input}")    

    def quit(self):
        print("Thanks for playing!")
        self.running = False

    def look(self):
        print(f"You see a {self.current_location.description}")

    def move(self):
        destination = input(f"Where to? ").lower()

        if destination not in self.world['locations']:
            print(f"Creating new area: {destination}.")
            self.world['locations'][destination] = {
                "name": destination,
                "description": None,
                "exits": []
            }
        
        self.world["current_id"] = destination

        self.current_location = location(self.world['locations'][destination])
        print(f"You move to the {self.current_location.name}")

