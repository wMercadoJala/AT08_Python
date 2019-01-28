from abel.test1.WordORPhrase import WordORPlace


class game:
    instance_word = WordORPlace()
    string_pattern = instance_word.return_word()
    copy_string = string_pattern
    clone_ = []
    error_ = 0

    def generate_(self):
        for value in range(0, len(self.copy_string)):
            if value % 2 == 0:
                self.clone_ += self.copy_string[value]
            else:
                self.clone_ += '_'
        print(self.clone_)
        return self.clone_

    def input_word(self):
        word = str(input('input word please'))
        word = word.upper()
        print(word)
        index = self.copy_string.find(word)

        if index >= 0:
            self.clone_[index] = word
            self.copy_string = self.copy_string.replace(self.copy_string[index], '*', 1)
            print(self.clone_)
        else:
            self.error_ += 1

            self.instance_word.imp(self.error_)
            print(self.clone_)
        return self.clone_

    def play_(self):
        while self.error_ < 6:
            game.input_word(self)

            if self.clone_ == list(self.string_pattern):
                self.error_ = 6
                print('YOU WINN')


a = game()
a.generate_()
a.play_()
