import json
import os

def list_players():
    player_list =[]
    if not os.path.exists('data/saves'):
        return player_list
    else:
        for file in os.listdir('data/saves'):
            if file.endswith('.json'):
                player_list.append(file.removesuffix('.json'))
    return player_list

def load_data(file_name: str, path: str):
    file_path = os.path.join(path, file_name)

    try: # The try/except handles the error if there is no file
        with open(file_path, 'r') as file:
            return json.load(file) # Return the world so other functions can use it
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
