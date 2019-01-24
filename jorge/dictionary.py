from urllib3.connectionpool import xrange

wordArray = {}

def create_a_new_dictionary(long):
    for i in xrange(long):
        wordArray[str(i)] = None
    wordArray.clear()

def set_key_and_value(keys, value):
    wordArray.update({keys : value})


def print_keys():
    print(wordArray.keys())


def print_values():
    print(wordArray.values())


def print_dictionary():
    for key in wordArray:
        print(key + " : " + wordArray.get(key))


def exist_key(key):
    return wordArray.__contains__(key)


def exist_values(values):
    resp = False
    for key in wordArray:
        if wordArray.get(key) == values:
            resp = True
            break

    return resp



create_a_new_dictionary(8)

set_key_and_value("lapiz", "material que permite escribit en cualquier material dependiendo del material con que se escribio")
set_key_and_value("celular", "dispositivo electronico con la finalidad principal de comunicarse entre personas o maquinas")

# print_keys()
# print_values()
print_dictionary()

print(exist_key("celular"))
print(exist_values("dispositivo electronico con la finalidad principal de comunicarse entre personas o maquinas"))