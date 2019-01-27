def char_count(string):
    """
    This method count the character a-z of a string and count each one how many times its used.
    :param string: Input string
    :return: List of chars counted
    """
    char_dictionary = {}
    phrase = "".join(string.split(" ")).lower()
    for letter in phrase:
        char_dictionary[letter] = phrase.count(letter)
    return sorted(char_dictionary.items())


print(char_count("thiS is String with Upper and lower case Letters"))
print(char_count("Hola mi nombre es Rodrigo Menacho"))
