from game_engine import gameEngine
from persistance_manager import load_world, new_world, save_world

def start():
    current_world = load_world()
    if current_world == None:
        current_world = new_world()

    game = gameEngine(current_world)

    #this try/finally will save the game even in the event of a crash
    try:
        game.run()
    finally:
        save_world(current_world)
        print("Goodbye")

#__name__ is a hidden variable in every file
#__main__ this name is given to the starting point of executiong
#this means start() is only called if when desired and not if it's imported elsewhere
if __name__ == "__main__":
    start()