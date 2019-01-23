my_dictionary = {1: 'lorem', 2: 'ipsum', 3: 'dolor', 4: 'sit', 5: 'amet', 6: 'consectetur'}


def get_size():
    size = 0
    for element in my_dictionary:
        size += 1
    return size


def get_keys():
    return sorted(my_dictionary.keys())


def get_values():
    return sorted(my_dictionary.values())


def print_dictionary():
    return str(my_dictionary)


def another_print():
    for key in my_dictionary:
        print(key, ':', my_dictionary[key])
    return


def is_key(key):
    return key in my_dictionary.keys()


def is_value(value):
    return value in my_dictionary.values()


print(get_size())
print(get_keys())
print(get_values())
print(print_dictionary())
another_print()
print(is_key(3))
print(is_value('vinchi'))
