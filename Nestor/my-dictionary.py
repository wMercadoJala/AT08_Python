my_dictionary = {1: 'lorem', 2: 'ipsum', 3: 'dolor', 4: 'sit', 5: 'amet', 6: 'consectetur'}

"""
This method return dictionary size.
:return: type int
"""
def get_size():
    size = 0
    for element in my_dictionary:
        size += 1
    return size


"""
This method return a list sorted from dictionary keys.
:return: type ordered list
"""
def get_keys():
    return sorted(my_dictionary.keys())


"""
This method return a list sorted from dictionary values.
:return: type ordered list
"""
def get_values():
    return sorted(my_dictionary.values())


"""
This method return a string from dictionary { key: value } format.
:return: type string with format
"""
def print_dictionary():
    return str(my_dictionary)


"""
This method print ever single pairs key: value.
"""
def another_print():
    for key in my_dictionary:
        print(key, ':', my_dictionary[key])
    return


"""
This method return True if key exists in dictionary, False if not.
:return: type boolean
"""
def is_key(key):
    return key in my_dictionary.keys()


"""
This method return True if value exists in dictionary, False if not.
:return: type boolean
"""
def is_value(value):
    return value in my_dictionary.values()


print(get_size())
print(get_keys())
print(get_values())
print(print_dictionary())
another_print()
print(is_key(3))
print(is_value('vinchi'))
