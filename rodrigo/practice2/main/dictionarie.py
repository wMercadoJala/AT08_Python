dictionary = {}


def dict_creation():
    """
    This method fill a dictionary asking for the key and the value to the user by console.
    :return: The dictionary filled.
    """
    dictionary_length = 0
    try:
        dictionary_length = int(input("Please enter the length for the dictionary-> "))
    except ValueError:
        print("Please enter a numeric value")

    for item in range(dictionary_length):
        key = input("Please enter the key {0}-> ".format(item))
        dictionary[key] = input("Please enter the value {0}-> ".format(item))
    return dictionary


def dict_print_keys():
    """
    This method print all the keys of the dictionary.
    :return: The keys of the dictionary.
    """
    print(dictionary.keys())


def dict_print_values():
    """
    This method print all the values of the dictionary.
    :return: The values of the dictionary.
    """
    print(dictionary.values())


def dict_print():
    """
    This method print all the dictionary.
    :return: The dictionary.
    """
    print(dictionary)


def dict_is_existing_key(key):
    """
    This method ask if the key is existing.
    :param key: Input key.
    :return: Print with the information.
    """
    print("The key is existing") if key in dictionary else print("The key is not existing")


def dict_is_existing_value(value):
    """
    This method ask if the value is existing.
    :param key: Input value.
    :return: Print with the information.
        """
    print("The value is existing") if value in dictionary else print("The value is not existing")


dict_creation()
dict_print()
dict_print_keys()
dict_print_values()
dict_is_existing_key("hola")
dict_is_existing_value(1)
