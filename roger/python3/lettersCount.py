def letters_count(sentence):
    """
    Method for count letters of sentence.
    :param sentence: string sentence.
    :return: a table of the letters of the alphabet in alphabetical order.
    """
    my_dict = {}
    only_letters = sorted(sentence.lower().replace(" ", ""))
    for letter in only_letters:
        my_dict[letter] = only_letters.count(letter)
    show_dictionary(my_dict)
    return my_dict


def show_dictionary(my_dictionary):
    """
    Method for show and print in console a dictionary.
    """
    for key in my_dictionary:
        print(key, ":", my_dictionary[key])


letters_count("ThiS is String with Upper and lower case Letters")
