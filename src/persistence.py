import json, os
from .dictionary import Dictionary
from .classes import MindPalace


def load_data(file_name: str, path: str):
    if not file_name.endswith('.json'):
        file_name += '.json'
    file_path = os.path.join(path, file_name)

    try: # The try/except handles the error if there is no file
        with open(file_path, 'r') as file:
            return json.load(file) # Return file so other functions can use it
    except FileNotFoundError:
        return None
    

def save_data(file_name: str, data: dict, path: str): 
    if not file_name.endswith('.json'):
        file_name += '.json'

    file_path = os.path.join(path, file_name)

    if not os.path.exists(path):
        os.makedirs(path)

    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"System says: {e}")


def load_dictionary():
    data = load_data('dictionary.json', 'data')
    return Dictionary(data)


def save_dictionary(dictionary_data):
    return save_data('dictionary.json', dictionary_data, 'data')


def load_mind_palace(mind_palace_name):
    data = load_data(mind_palace_name, 'data/saves')
    return MindPalace(data)


def save_mind_palace(mind_palace):
    return save_data(mind_palace['name'], mind_palace, 'data/saves')


def create_mind_palace(mind_palace_name):
        data = MindPalace.create_mind_palace(mind_palace_name)
        save_data(mind_palace_name, data, 'data/saves')
        return MindPalace(data)
