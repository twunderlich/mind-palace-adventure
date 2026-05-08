import json
      
def new_world():
    name = input("What is the name of your Mind Palace?> ")
    return {
        "name": name,
        "current_id":"Entrance",
        "locations": {}, 
        }

def load_world():
    try: # The try/except handles the error if there is no file
        with open('world.json', 'r') as file:
            return json.load(file) # Return the world so other functions can use it
    except FileNotFoundError:
        return None

def save_world(current_world):
    with open('world.json', 'w') as file:
        json.dump(current_world, file, indent=4)