import time, uuid, code

def create_unique_id(data = None):
    """
    Creates a unique 8 digit hexidecimal.
    Args:
        data: A dictionary of objects where each object has a 'unique_id' key
    Returns the unique 8 digit hexidecimal
    """
    while True:
        new_id = uuid.uuid4().hex[:8]

        if data is None:
            return new_id

        exists = any(data.get('unique_id') == new_id for data in player_profile.values())
        if not exists:
            return new_id

print(create_unique_id())

pauses = {
    ",": .2,
    ":": .2,
    ";": .2,
    ".": .4,
    "!": .4,
    "?": .4
}

def thinking(dots):
    for i in range(dots):
        print(".", end = "", flush=True)
        time.sleep(pauses.get("."))
    if dots != 0:
        print()

def typing(text, str = ""):
    time.sleep(.4)
    for char in text + str:   
        print(char, end="", flush=True)
        time.sleep(pauses.get(char, .1))

def typed_print(text, dots = 3):
    thinking(dots)
    typing(text)
    print()

def typed_input(text, dots = 3):
    thinking(dots)
    typing(text, "\n> ")
    return input()

def yes_or_no(question):
    commands = ["yes", "no"]
    user_input = None
    while user_input not in commands:
        user_input = typed_input(question).lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            typed_print(f'"{user_input}" is not valid option, "Yes" or "No")')