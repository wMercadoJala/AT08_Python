def letters_of_the_alphabet(word):
    container =filter(str.isalpha, sorted(word.lower().replace(" ", "")))
    wordArray = {}
    for letter in container:
        if letter in wordArray:
            wordArray[letter] += 1
        else:
            wordArray[letter] = 1
    print(wordArray)

letters_of_the_alphabet("murc #$% i %23456789&/ el /& ago () ma ( ñan #$& ero ¡?¡")