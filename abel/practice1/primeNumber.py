""""
list = [valor for valor in range(0, 7) if valor % 2 == 0]
print(list)
"""""


def is_Prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def createList(min, max):
    lista = []
    for value in range(min, max):
        if is_Prime(value):
            lista.append(str(value) + ": primo")
        else:
            lista.append(str(value) + ": no primo")
    return lista


print(createList(1, 20))
