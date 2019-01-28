from jorge.Game import *
from jorge.WordOrPhrase import *



def star(phrase, character):
    game = Game(WordOrPhrase(phrase))
    game.exits_character(character)


star("hola", "o")



