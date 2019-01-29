# main

import game


class Main:
    def __init__(self):
        self.game = game.Game()

    def playing(self):
        self.game.print_guess()
        while True:
            char = input()
            self.game.try_guess_letter(char)
            self.game.print_guess()
            self.game.print_hangman()


play = Main()
play.playing()
