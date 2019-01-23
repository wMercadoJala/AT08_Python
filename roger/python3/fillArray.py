"""
Function 1:
    -No arguments defined
    -Should ask to the user the number of elements in the list
    -According the value inserted ask for each value of the array and push it in a new array
    -Return the array
Function 2
    -Should receive 1 argument (the array returned in method 1)
    -Should print the array

"""


def function_1():
    size = input("Insert number of elements in the list: ")
    user_list = []
    for i in range(int(size)):
        user_list.append(input("Insert argument {0}: ".format(str(i + 1))))
    return user_list


def function_2(list_elements):
    print("The list is:", list_elements)


function_2(function_1())
