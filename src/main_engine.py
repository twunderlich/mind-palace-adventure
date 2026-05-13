from .persistence import load_dictionary, load_mind_palace, save_dictionary, save_mind_palace
from .dictionary import Dictionary
from .classes import MindPalace, Location
from .utility import typed_print, typed_input, create_unique_id, yes_or_no
import code

class MainEngine:
    def __init__(self):
        self.running = False
        self.dictionary = load_dictionary()
        self.mind_palace = {}
        self.mind_palace = load_mind_palace('Main')
        self.commands = {
            "quit": self.quit,
            "save": self.save,
            "reset": self.reset,
            "console": self.console

        }

    def console(self):
        return code.interact("DEVELOPER PAUSE", local={'engine': self}) 

    def save(self):
        pass

    def reset(self):
        pass    

    def quit(self):
        user_input = yes_or_no("Would you like to quit?",)

        if user_input == "yes":
            typed_print("Thanks for exploring Mind Palace Adventure")
            typed_print("Goodbye")
            save_mind_palace(self.mind_palace.to_dictionary())
            save_dictionary(self.dictionary.to_dictionary())
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
