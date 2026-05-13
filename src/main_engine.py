from .persistence import load_data, save_data
from .dictionary import Dictionary
from .classes import PlayerProfile, Player, MindPalace, Location
from .utility import typed_print, typed_input, create_unique_id, yes_or_no
from . import narrator

class MainEngine:
    def __init__(self):
        self.running = False
        self.dictionary = self.load_dictionary()
        self.player_profile = self.load_player_profile()
        self.mind_palace = {}
        self.mind_palace = self.load_mind_palace('Main')
        self.player = {}
        self.player = self.load_player('Guest')
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

    def save_dictionary(self):
        data = self.dictionary.to_dictionary()

        return save_data('dictionary.json', data, 'data')

    def load_player_profile(self):
        data = load_data('player_profile.json', 'data')

        if data is None:
            data = PlayerProfile.create_player_profile()
            save_data('player_profile', data, 'data')

        return PlayerProfile(data)

    def save_player_profile(self):
        data = self.player_profile.to_dictionary()

        return save_data('player_profile', data, 'data')

    def load_mind_palace(self, mind_palace_name = 'Main'):
        if mind_palace_name == self.mind_palace.get('name'):
            return self.mind_palace

        data = load_data(mind_palace_name, 'data/saves')
        return MindPalace(data)

    def save_mind_palace(self):
        data = self.mind_palace.to_dictionary()

        return save_data(data[name], data, 'data/saves')

    def create_mind_palace(self, mind_palace_name):
            exist = load_data(mind_palace_name,'data/saves')

            if exists is None:
                data = MindPalace.create_mind_palace(mind_palace_id, mind_palace_name)
                save_data(mind_palace_name, data, 'data/saves')
                return MindPalace(data)

            return None

    def load_player(self, username = 'Guest'):
        if username == self.player.get('username'):
            return self.player
        print("test -", self.player_profile)
        data = self.player_profile.get_player(username)
        return Player(data)

    def save_player(self):
        data = self.player.to_dictionary()

        self.player_profile[data['username']] = data
        return save_player_profile()

    def create_player(self, username):
        exist = any(self.player_profile)

        if exists is False:
            data = Player.create_player(username)
            self.player_profile[username] = data
            save_data('layer_profile.json', data, 'data')

            return MindPalace(data)

        return None


    def quit(self):
        user_input = yes_or_no("Would you like to quit?",)

        if user_input == "yes":
            typed_print("Thanks for exploring Mind Palace Adventure")
            typed_print("Goodbye")
            self.save_player()
            self.save_mind_palace()
            self.save_player_profile()
            self.save_dictionary()
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
