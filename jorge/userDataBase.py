from jorge.user import user

container = {}
nickname = ""
def set_user(nicknam, name, age):
    global nickname
    nickname = nicknam
    container.update({nickname: user(nickname)})
    container.get(nickname).fill_date_user(name, age)


def print_keys():
    print(container.keys())


def print_values():
    for key in container:
        print("NICKNAME: " + container.get(key).get_nickname() + "NAME: " +
              container.get(key).get_name() + "AGE: " + container.get(key).get_age())

def exist_key(key):
    return container.__contains__(key)


def exist_values(values):
    resp = False
    for key in container:
        if container.get(key) == values:
            resp = True
            break

    return resp


set_user("jorge7421", "jorge1", "15")
set_user("jorge7422", "jorge2", "16")
set_user("jorge7423", "jorge3", "17")
set_user("jorge7424", "jorge4", "19")
print_keys()
print_values()

print(exist_key("jorge7422"))