"""
Practice 1.
1. Function to create the dictionary, the Function should ask for the length of the dictionary
According the length defined should ask to the user for the key and for the value.
2. Function to print the dictionary keys
3. Function to print the dictionary values
4. Function to print the dictionary
5. Function to define is a key inserted by the user, exists on the dictionary.
6. Function to define is a value inserted by the user, exists on the dictionary.
7. Use the dictionary as a Global variable to be used in all functions
"""

user_dict = {}


def create_dictionary():
    """
    Method for create and fill a dictionary from keyboard.
    :return: new dictionary.
    """
    size = input("Insert number of elements in the dictionary: ")
    global users_dict
    for i in range(int(size)):
        key = input("  Insert key {0}: ".format(str(i + 1)))
        user_dict[key] = input("Insert value {0}: ".format(str(i + 1)))
    return user_dict


def print_dictionary_keys(my_dictionary):
    """
    Method for print in console a list with dictionary keys.
    :param my_dictionary: set a dictionary.
    """
    print("The dictionary keys -> ", list(my_dictionary.keys()))


def print_dictionary_values(my_dictionary):
    """
    Method for print in console a list with dictionary values.
    :param my_dictionary: set a dictionary.
    """
    print("The dictionary values -> ", list(my_dictionary.values()))


def print_dictionary(my_dictionary):
    """
    Method for show and print in console a dictionary.
    :param my_dictionary: set a dictionary.
    """
    print("The dictionary -> ", my_dictionary)
    for key in my_dictionary:
        print(key, ":", my_dictionary[key])


def this_key_exist(my_dictionary):
    """
    Method for define if a key exist in a dictionary.
    :param my_dictionary: set a dictionary.
    :return: boolean value.
    """
    key = input("Search key: ")
    return True if key in my_dictionary.keys() else False


def this_value_exist(user_dictionary):
    """
    Method for define if a value exist in a dictionary.
    :param user_dictionary: set a dictionary.
    :return: boolean value.
    """
    value = input("Search value: ")
    return True if value in user_dictionary.values() else False


create_dictionary()
print_dictionary(users_dict)
print_dictionary_keys(users_dict)
print_dictionary_values(users_dict)
print(this_key_exist(users_dict))
print(this_value_exist(users_dict))
