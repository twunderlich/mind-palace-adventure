from src.engines import MainEngine

main = MainEngine()

if __name__ == "__main__":
    main.start()
# from src.game_engine import engines
# from src.persistence_manager import load_file, save_file
# from src.utility import typed_print, typed_input, create_unique_id
# from src.classes import PlayerProfile, Player, MindPalace



# def start():
#     player_profile = load_file("player_profile.json")
#     if player_profile is None:
#         player_profile = PlayerProfile.create_player_profile()
#         save_file('player_profile.json', player_profile)

#     typed_print("Welcome to Mind Palace Adventures!")

#     current_player = typed_input(f"Hello, what is your name?> ")

#     if current_player not in player_profile['players']:
#          unique_id = create_unique_id()
#          new_player = Player.create_player(unique_id, current_player)
#          player_profile['players'][current_player] = new_player
#          save_file('player_profile.json', player_profile)

#     player_data = player_profile['players'][current_player]
#     current_player = Player(player_data)

#     current_mind_palace = None
#     if len(current_player.mind_palaces) == 0:
#         typed_print(f"{current_player.username}, you have no Mind Palaces yet,")
#         user_input = None
#         while user_input != "yes":
#             user_input = typed_input("would you like to start new one?> ").lower()
#             if user_input == "yes":
#                 name = typed_input("What would you like to name it?> ")
#                 unique_id = create_unique_id()
#                 current_mind_palace = MindPalace.create_mind_palace(unique_id, name)
#             elif user_input == "no":
#                 typed_print("There is nothing else to do.")
#             else:
#                 typed_print("Yes or No, ")
#     else:
#         typed_print(f"{current_player['username']}, Welcome back,")
#         user_input = None
#         while user_input not in ["yes", "no"]:
#             user_input = typed_print("would you like to enter an existing Mind Palace? ")
#             if user_input == "yes":
#                 typed_print(f"Which one would you like to open?")
#                 options = []
#                 for each in current_player.mind_palaces:
#                     typed_print(each, 0)
#                     options + each
#                 selection = None
#                 while selection not in options:
#                     selection = typed_input("> ", 0)
#                     if selection in options:
#                         current_mind_palace = MindPalace(selection) 
#                     else:
#                         typed_print(f"{selection} is not one of the options")
#             elif user_input == "no":
#                 user_input = None
#                 while user_input != "yes":
#                     user_input = typed_input("would you like to start new one?> ").lower()
#                     if user_input == "yes":
#                         name = typed_input("What would you like to name it?> ")
#                         unique_id = create_unique_id()
#                         current_mind_palace = MindPalace.create_mind_palace(unique_id, name)
#                         save_file(current_mind_palace['name'])
#                 else:
#                     typed_print("There is notheing else to do")

#     print("line 69 - ", current_mind_palace['name'])

#     current_mind_palace = load_file(current_mind_palace['name'])
#     game = gameEngine(current_mind_palace)

# this try/finally will save the game even in the event of a crash
#     try:
#         game.run()
#     finally:
#         save_file(current_mind_palace)
#         typed_print("Mind Palace has been saved")
#         typed_print("Goodbye")

# # __name__ is a hidden variable in every file
# # __main__ this name is given to the starting point of execution
# # this means start() is only called if when desired and not if it's imported elsewhere
# if __name__ == "__main__":
#     start()