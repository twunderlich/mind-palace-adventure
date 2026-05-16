from .persistence import load_data, save_data
from .dictionary import Dictionary
from .classes import MindPalace, Location
from .utility import typed_print, typed_input, create_unique_id, yes_or_no
import code

class MainEngine:
    def __init__(self):
        self.running = False
        self.dictionary = None
        self.mind_palace = None
        self.commands = {
            "quit": self.quit,
            "save": self.save,
            "reset": self.reset,
            "console": self.console            
        }

        self.dictionary = load_data('dictionary.json', 'data')
        if not self.dictionary:
            print("dictionary.json not loaded")
        self.dictionary = Dictionary(self.dictionary)

        self.mind_palace = load_data('main_menu.json', 'data/saves')
        if not self.mind_palace:
            print("main_menu.json not loaded")
        self.mind_palace = MindPalace(self.mind_palace)

    def console(self):
        return code.interact("DEVELOPER PAUSE", local={'engine': self}) 

    def save(self):
        pass

    def reset(self):
        pass    

    def quit(self):
        typed_print("Thanks for exploring Mind Palace Adventure")
        typed_print("Goodbye")
        save_data(self.mind_palace.name, self.mind_palace.to_dictionary(),'data/saves')
        save_data('dictionary', self.dictionary.to_dictionary(), 'data')
        self.running = False

    def start(self):
        self.running = True

        print(f"""
{"~" * 75}
{" " * 25}Mind Palace Adventures
{"~" * 75}
            """)
        
        typed_print(self.mind_palace.current_room['description'])

        while self.running:
            user_input = input("> ").lower()
            if user_input in self.commands:
                if yes_or_no(f"Would you like to {user_input}?"):
                    self.commands[user_input]()

        typed_print("Goodbye")
