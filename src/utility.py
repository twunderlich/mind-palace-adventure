import time
import uuid

def create_unique_id():
        return uuid.uuid4().hex[:8]

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

def typing(text, str = None):
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
