# WordOnPhrase

import random


class WordOnPhrase:
    def __init__(self):
        self.words = ['lorem', 'ipsum', 'dolor', 'consectetur', 'fortuna', 'fortis', 'audiubat']

    def get_word(self):
        return self.words[random.randint(0, len(self.words) - 1)]
