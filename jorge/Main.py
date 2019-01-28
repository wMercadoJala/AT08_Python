from jorge.Game import *

game = Game()


def star(phrase):
    global game
    game.set_value_phrase(phrase)


def add_character(character):
    global game
    game.exits_character(character)
    game.print_image()
    game.print_characters_of_phrase()


star("holao")
add_character("1")
add_character("2")
add_character("3")
add_character("4")
add_character("5")
add_character("6")
add_character("7")
add_character("8")

star("hello word")
add_character("e")
add_character("o")
add_character("r")
add_character("d")
add_character("5")
add_character("6")
add_character("l")
add_character("w")
add_character("h")

star("api")
add_character("a")
add_character("p")
add_character("i")

