def replace(phrase, old, new):
    """
    This method makes a replace method similar of replace built-in python
    :param phrase: Input phrase
    :param old: Character to change
    :param new: Character will be changed
    :return: The new phrase
    """
    print(new.join(phrase.split(old)))


replace("Missisipi", "i", "o")
song = "I love spom! Spom is my favorite food. Spom, spom, yum!"
replace(song, "om", "am")
replace(song, "o", "a")
