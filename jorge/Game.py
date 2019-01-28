from jorge.WordOrPhrase import *


class Game:

    def __init__(self):
        self.phrases = WordOrPhrase()
        self.attempts = 0
        self.body = {
            0: "",
            1: " o\n",
            2: " o\n/\n",
            3: " o\n/T\n",
            4: " o\n/T\\\n",
            5: " o\n/T\\\n/\n",
            6: " o\n/T\\\n/ \\\n"
        }

    def set_value_phrase(self, new_phrase):
        self.phrases.set_phrase(new_phrase)
        self.attempts = 0

    def exits_character(self, new_character):
        if int(self.phrases.get_phrase().find(new_character.upper())) >= 0 and self.attempts < 7:
            self.phrases.replace_phrase(new_character)
        else:
            self.attempts += 1

    def print_characters_of_phrase(self):
        aux = ""
        for character in self.phrases.get_phrase():
            if character.islower():
                aux += character
            elif character.isspace():
                aux += " "
            else:
                aux += "_"
        print(aux)

    def print_image(self):
        if int(self.attempts) > 6:
            print("YOU ARE DEAD")
        elif self.phrases.get_phrase().islower():
            print("COMPLETED")
        else:
            nano = self.body[int(self.attempts)]
            print(nano + "\n" + str(self.attempts) + " failed attemps of 6\n")
