class WordOrPhrase:

    def __init__(self, phrase):
        self.phrase = phrase.upper()

    def get_phrase(self):
        return self.phrase

    def set_phrase(self,new_phrase):
        self.phrase = new_phrase.upper()


