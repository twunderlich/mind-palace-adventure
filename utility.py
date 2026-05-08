import time

pauses = {
    ",": .2,
    ":": .2,
    ";": .2,
    ".": .4,
    "!": .4,
    "?": .4
}

def thinking(text=None):
    if text is None:
        text = ""
    dots = max(3, min(12, round(len(text) // 10)))
    for i in range(dots):
        print(".", end = "", flush=True)
        time.sleep(pauses.get("."))
    print()

def typing(text):
    time.sleep(.4)
    for char in text:   
        print(char, end="", flush=True)
        time.sleep(pauses.get(char, .1))

def typed_print(text):
    thinking(text)
    typing(text)
    print()

def typed_input(text):
    thinking(text)
    typing(text)
    return input()
    
