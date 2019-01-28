from jorge.Game import *
from jorge.WordOrPhrase import *



def star(phrase, character):
    game = Game(WordOrPhrase(phrase).get_phrase())
    game.exits_character(character)
    game.print_characters_of_phrase()


star("hola", "o")



