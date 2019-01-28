import random


class WordORPlace:
    word_list = ['GUSTAVO', 'HOLA MUNDO', 'HOMERO', 'DEAD POOL', 'BATMAN']
    hangman = [' | ', ' O ', "/|7", ' | ', '/ L', 'DEAD']

    def return_word(self):
        return random.choice(self.word_list)

    def imp(self, index):
        for i in range(0, index):
            print(self.hangman[i])
