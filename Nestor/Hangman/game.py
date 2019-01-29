# Game
import re
import sys

import wordOnPhrase

hangman = ['o', "\\", '/', '|', '/', "\\"]


def print_message(message):
    print('[]==========[]')
    print(f'| {message} |')
    print('[]==========[]')


class Game:
    def __init__(self):
        self.words = wordOnPhrase.WordOnPhrase()
        self.guess_word = self.words.get_word()
        self.shadow_word = '_' * len(self.guess_word)
        self.hangman = []
        self.fail_attempt = 0

    def change_char_at(self, positions, char):
        if len(positions) == 0:
            self.hangman.append(hangman[self.fail_attempt])
            self.fail_attempt += 1
        else:
            guess = list(self.shadow_word)
            for index in positions:
                guess[index] = char
            self.shadow_word = "".join(guess)

    def print_guess(self):
        print(self.shadow_word)

    def try_guess_letter(self, letter):
        if self.fail_attempt == 6:
            print_message('You lose!!')
            sys.exit()
        self.change_char_at([m.start() for m in re.finditer(letter, self.guess_word)], letter)
        if self.guess_word == self.shadow_word:
            print_message('You WIN!!')
            sys.exit()

    def print_hangman(self):
        print(self.hangman)
