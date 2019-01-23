from rodrigo.practice2.main.practice_age import age as msg_age
from rodrigo.practice2.main.practice_age import calculate


def write_user():
    dict_length = int(input("How much users you want to record? -> "))
    dictionary = {}
    for item in range(dict_length):
        key_user_name = input("{0}-user: ".format(item))
        try:
            dictionary[key_user_name] = int(input("{0}-age: ".format(item)))
        except ValueError:
            print("The  age value must be int")
            break
    print_characteristics(dictionary)


def print_characteristics(dictionary):
    for key in dictionary.keys():
        print("----Name of the user: {0}----".format(key))
        print(msg_age.age_identifier(dictionary[key]))
        print(calculate.age(dictionary[key]))


write_user()
