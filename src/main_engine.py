from .persistence import load_data, save_data, list_players
from .classes import PublicSaves, PlayerProfile, Player, Location
from .utility import typed_print, typed_input, create_unique_id
from . import narrator

class MainEngine:
    def __init__(self):
        self.running = False
        self.public_saves = self.load_public_saves()
        self.b = self.load_player_profile()
        self.players = list_players()
        self.player = None
        self.commands = {
            "quit": self.quit,
        }      

    def load_public_saves(self):
        data = load_data("public_saves.json", "data")
        if data is None:
            data = PublicSaves.create_public_saves()
        return PublicSaves(data)

    def load_player_profile(self):
        data = load_data("b.json", "data")
        if data is None:
            data = PlayerProfile.create_player_profile()
        return PlayerProfile(data)

    def load_player(self, username):
        if username not in self.players:
            player_id = create_unique_id()
            self.player = Player.create_player(player_id, username) 
            save_data(username, self.player.to_dictionary()) 

        self.player = Player()

    def load_mind_place(self, mindpalace):
        pass

    def quit(self):
        user_input = narrator.yes_or_no("Would you like to quit?",)
        print(user_input)
        if user_input == "yes":
            typed_print("Thanks for exploring Mind Palace Adventure")
            typed_print("Goodbye")
            self.running = False

    def start(self):
        self.running = True

        print(f"""
{"~" * 75}
{" " * 25}Mind Palace Adventures
{"~" * 75}
            """)

        while self.running:
            user_input = input("> ").lower()
            if user_input in self.commands:
                self.commands[user_input]()
            else:
                typed_print(f'"{user_input}" is not a valid option')
