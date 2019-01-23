dictionary = {}


def dict_creation():
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
    print(dictionary.keys())


def dict_print_values():
    print(dictionary.values())


def dict_print():
    print(dictionary)


def dict_is_existing_key(key):
    print("The key is existing") if key in dictionary else print("The key is not existing")


def dict_is_existing_value(value):
    print("The value is existing") if value in dictionary else print("The value is not existing")


dict_creation()
dict_print()
dict_print_keys()
dict_print_values()
dict_is_existing_key("hola")
dict_is_existing_value(1)
