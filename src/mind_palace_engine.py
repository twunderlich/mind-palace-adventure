from classes import Location
from utility import typed_input, typed_print

class gameEngine:
    def __init__(self, current_world):
        self.world = current_world
        self.running = True
        self.commands = {
            "quit": self.quit,
            "look": self.look,
            "move": self.move,
        }   
        current_id = self.world.current_id
        if current_id not in self.world['rooms']:
            self.world['rooms'][current_id] = Location()    
        current_location_raw_data = self.world["rooms"][current_id]
        self.current_location = Location(current_location_raw_data)

    def run(self):
        typed_print(f"Welcome to {self.world['name']}!")
        typed_print(f"You are in the {self.world['current_id']}")

        while self.running:
            user_input = input("> ").lower() # makes it not case sensitive

            if user_input in self.commands:
                self.commands[user_input]() # runs the command

            else:
                typed_print(f"You tried to: {user_input}")    

    def quit(self):
        typed_print("Thanks for playing!")
        self.running = False

    def look(self):
        typed_print(f"You see a {self.current_location.description}")

    def move(self):
        destination = typed_input(f"Where to?> ").lower()

        if destination not in self.world['rooms']:
            typed_print(f"Creating new area: {destination}.")
            self.world['rooms'][destination] = {
                "name": destination,
                "description": None,
                "exits": []
            }
        
        self.world["current_id"] = destination

        self.current_location = Location(self.world['rooms'][destination])
        typed_print(f"You move to the {self.current_location.name}")

