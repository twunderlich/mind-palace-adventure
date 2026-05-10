from .utility import typed_input
from .utility import typed_print

def yes_or_no(question):
    commands = ["yes", "no"]
    user_input = None
    while user_input not in commands:
        user_input = typed_input(question).lower()
        if user_input == "yes":
            return "yes"
        elif user_input == "no":
            return "no"
        else:
            typed_print(f'"{user_input}" is not valid option, "Yes" or "No")')