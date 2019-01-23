_dictionary_ = {}


def create():
    print("input the length of the dictionary")
    length_dict = int(input("input length "))

    for value in range(0, length_dict):
        _dictionary_[value] = int(input("add value"))
    return _dictionary_


def print_keys():
    print(_dictionary_.keys())


def print_values():
    print(_dictionary_.values())


def print_dictionary():
    print(_dictionary_)


def exist_value():
    return "value exist in dic" if int(input("input valor int")) in _dictionary_.values() else "value don't exist"


create()

print_dictionary()

print(exist_value())

print_values()

print_keys()
