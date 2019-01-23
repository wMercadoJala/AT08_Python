def char_count(string):
    char_dictionary = {}
    phrase = "".join(string.split(" ")).lower()
    for letter in phrase:
        char_dictionary[letter] = phrase.count(letter)
    return sorted(char_dictionary.items())


print(char_count("thiS is String with Upper and lower case Letters"))
print(char_count("Hola mi nombre es Rodrigo Menacho"))
