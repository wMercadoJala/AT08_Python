import random

from roger.HangmanGame.wordOrPhrase import WordOrPhrase


class Game:

    def __init__(self):
        words = WordOrPhrase()
        self.word = words.get_word()
        self.word_game = list(self.word)
        self.new_word_game()
        self.set_help()
        self.failed = 0
        self.hangman = [" |  ", " O   Help me!!! ", "\|/  ", " |  ", "/ \ ", "IS DEAD..."]

    def exist_char(self, char):
        character = str(char).upper()
        if self.word.find(character) is not -1 or not character == ' ':
            self.set_char(character)
            return True
        else:
            self.failed += 1
            return False

    def new_word_game(self):
        pos = 0
        for letter in self.word_game:
            if letter != ' ':
                self.word_game[pos] = '_'
            pos += 1

    def set_help(self):
        for pos in range(int(len(self.word) / 2)):
            new_pos = random.randint(0, len(self.word) - 1)
            self.word_game[new_pos] = self.word[new_pos]

    def print_word_game(self):
        return '*********\nGanaste...\n*********' if self.word_is_complete() else ' '.join(self.word_game)

    def set_char(self, char):
        pos = 0
        for letter in self.word:
            if letter == char:
                self.word_game[pos] = letter
            pos += 1

    def word_is_complete(self):
        return False if '_' in self.word_game else True

    def show_hangman(self):
        for part in range(self.failed):
            print(self.hangman[part])
        message = "PERDISTE...se murio." if self.failed == 6 else "Fallaste se va morir, te queda {0} intentos."\
            .format(6 - self.failed)
        return message
