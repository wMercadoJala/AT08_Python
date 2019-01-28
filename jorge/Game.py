class Game:

    phrases = ""
    attempts = 0
    def __init__(self, phrase):
        global phrases
        phrases = phrase

    def exits_character(self, new_character):
        resp = False
        global phrases
        if phrases.find(new_character) > 0:
            phrases.replace(new_character, new_character.lower())
            resp = True
        return resp

    def print_characters_of_phrase(self):
        global attempts
        attempts += 1
        global phrases
        aux = ""
        if attempts<7:
            for character in phrases:
                if character.islower():
                    aux += character
                else:
                    aux += "_"
        else:
            aux = "YOU ARE DEAD"
        print(aux)

    def print_intentos(self):
        global attempts
        print(attempts)


