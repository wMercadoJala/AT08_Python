from roger.HangmanGame.game import Game


def run_game():
    game = Game()
    print(game.word)
    print(game.print_word_game())
    while not game.word_is_complete() and game.failed < 6:
        if game.exist_char(input("Adivine una letra -> ")):
            print(game.print_word_game())
        else:
            print(game.show_hangman())



run_game()
