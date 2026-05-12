from .persistence import load_data, save_data
from .dictionary import Dictionary
from .classes import PlayerProfile, Player, Location
from .utility import typed_print, typed_input, create_unique_id, yes_or_no
from . import narrator

class MainEngine:
    def __init__(self):
        self.running = False
        self.dictionary = self.load_dictionary()
        self.player_profile = self.load_player_profile()
        self.player = self.load_player()
        self.commands = {
            "quit": self.quit,
        }      

    def load_dictionary(self):
        data = load_data('dictionary.json', 'data')

        if data is None:
            data = {
                "quit": {"word": "quit", "type": "verb", "phrase_with":[], "synonym": []}
            }

        return Dictionary(data)

    def load_player_profile(self):
        data = load_data('player_profile.json', 'data')

        if data is None:
            data = PlayerProfile.create_player_profile()
            save_data('player_profile', data, 'data')

        return PlayerProfile(data)

    def load_player(self, username = 'Guest'):
        if not username:
            username = 'Guest'

        player_data = self.player_profile.get_player(username)

        if player_data is None:
            player_id = create_unique_id(self.player_profile.player_profile)
            player_data = Player.create_player(player_id, username)
            self.player_profile.player_profile[username] = player_data
            save_data('player_profile', self.player_profile.player_profile,'data') 

        return Player(player_data)

    def load_mind_place(self, mindpalace):
        pass

    def quit(self):
        user_input = yes_or_no("Would you like to quit?",)
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
