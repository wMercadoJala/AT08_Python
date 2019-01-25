def my_first_method():
    value_1 = 20
    value_2 = 20
    value_3 = 30
    print(value_1)
    print(id(value_1))
    print(id(value_2))
    print(value_3)

    if (value_1 is value_2):
        print("is id")
    else:
        print("is not id")

    if (id(value_1) is id(value_2)):
        print("is id")
    else:
        print("is not id")

    return value_1


def new_function(num1, num2, operator):
    if operator == "*":
        print (num1 * num2)
    elif operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print (num1 - num2)
    else:
        print (num1 / num2)


new_function(5, 6, "*")

def new_function_module():
    print("par") if 1 % 2 == 0 else print("impar")


new_function_module()


def method_web(url):
    value = url[url.find("//")+2:url.rfind(" ")]
    print(value)

method_web("esta es la url de: http://fundacionjala.org jajaja")


def replace_cad(cadena, char_1, char_2):
    print("".join(cadena.replace(char_1, char_2)))


replace_cad("hola como estan", "o", "O")