# Game

import wordOnPhrase


class Game:
    def __init__(self):
        self.words = wordOnPhrase.WordOnPhrase()
        self.guess_word = self.words.get_word()
        self.shadow_word = '_' * len(self.guess_word)
        self.hangman = []

    def change_char_at(self, index, char):
        guess = list(self.shadow_word)
        guess[index] = char
        self.shadow_word = "".join(guess)

    def print_guess(self):
        print(self.shadow_word)

    def try_guess_letter(self, letter):
        guess = self.guess_word.find(letter)
        self.change_char_at(guess, self.guess_word[guess]) if guess > -1 else self.hangman.append('x')

    def print_word(self):
        print(self.words.get_word())

    def print_hangman(self):
        print(self.hangman)

# Me falto
# - Cambiar todas las ocurrencias encontradas.
# - Colocar los char del hangman correspodientes.
# - La clase main para hacer el juego interactivo.

game = Game()
game.print_guess()
game.try_guess_letter('o')
game.print_guess()
game.print_hangman()
game.try_guess_letter('r')
game.print_guess()
game.print_hangman()
game.try_guess_letter('l')
game.print_guess()
game.print_hangman()
game.try_guess_letter('m')
game.print_guess()
game.print_hangman()
game.try_guess_letter('e')
game.print_guess()
game.print_hangman()
