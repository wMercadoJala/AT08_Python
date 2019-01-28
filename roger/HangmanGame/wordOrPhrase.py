import random


class WordOrPhrase:

    def __init__(self):
        self.word = {1: 'HOLA', 2: 'MUNDO LOCO', 3: 'INVIERNO',
                     4: 'MAQUINAS MORTALES', 5: 'AMANECER', 6: 'FUNDACION JALA'}

    def get_word(self):
        return random.choice(list(self.word.values()))
