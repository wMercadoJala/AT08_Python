class Game:

    phrases = ""

    def __init__(self, phrase):
        global phrases
        phrases = phrase

    def exits_character(self, new_character):
        resp = False
        global phrases
        if phrases.find(new_character)>0:
            resp = True
        return resp

    def print_characters_of_phrase(self):
        global phrases
        print(phrases)

    def print_intentos(self):


