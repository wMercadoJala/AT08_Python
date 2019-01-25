from jorge.user import user

container = {}
id_user = 0
def set_user(id_usr, name, age):
    global id_user
    id_user = id_usr
    if 101 > id_user > 0 and 9 > len(name.lower()) > 1:
        container.update({id_user: user(id_user)})
        container.get(id_user).fill_date_user(name.lower(), age)


def print_keys():
    print(container.keys())


def print_values():
    for key in container:
        print("ID USER: " + str(container.get(key).get_nickname()) + " NAME: " +
              str(container.get(key).get_name()) + " AGE: " + str(container.get(key).get_age()))

def exist_key(key):
    return container.__contains__(key)

def find_user_with_one_digit(digit):
    container_find = []
    for key in container:
        if str (key)[0]==str(digit):
            container_find.append(key)
    return container_find


def exist_values(values):
    resp = False
    for key in container:
        if container.get(key) == values:
            resp = True
            break

    return resp


set_user(42, "JORGELEO", 15)
set_user(43, "jorge2", 16)
set_user(44, "jorge3", 17)
set_user(100, "jorge4", 19)
print_keys()
print_values()
print(find_user_with_one_digit(4))
print(exist_key(42))