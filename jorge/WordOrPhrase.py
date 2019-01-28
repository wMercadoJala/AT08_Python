class WordOrPhrase:

    def __init__(self):
        self.phrase = ""

    def get_phrase(self):
        return self.phrase

    def set_phrase(self, new_phrase):
        self.phrase = new_phrase.upper()

    def replace_phrase(self, value):
        self.phrase = self.phrase.replace(str(value).upper(), str(value).lower())
