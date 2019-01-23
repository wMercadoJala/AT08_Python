def user_list():
    number = 0
    array = []
    try:
        number = int(input('Enter length of the list-> '))
    except ValueError:
        print("Please put a number")
    for item in range(number):
        message = "Please enter the item {0}-> ".format(str(item))
        array.append(input(message))
    return array


def print_list(array):
    print("Your list is:{0}".format(array))
