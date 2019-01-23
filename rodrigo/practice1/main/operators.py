def equals(a, b):
    print("Both numbers are equals") if a == b else print("Both numbers are not equals")


def not_equals(a, b):
    print("Both numbers are not equals") if a != b else print("Both number are equals")


def greater(a, b):
    print("A it's greater than B") if a > b else print("A itsn't greater than B")


def smaller(a, b):
    print("A it's smaller than B") if a < b else print("A itsn't smaller than B")


def greater_equal(a, b):
    print("A it's greater than or equal to B") if a >= b else print("A itsn't greater than or equal to B")


def smaller_equal(a, b):
    print("A it's smaller than or equal to B") if a <= b else print("A itsn't smaller than or equal to B")

def operate(simbol, number_a, number_b):
    if simbol is "+":
        print(number_a + number_b, "The sum")
    if simbol is "-":
        print(number_a - number_b, "The substraction")
    if simbol is "*":
        print(number_a * number_b, "The multiplication")
    if simbol is "/":
        print(number_a / number_b, "The division")
    if simbol == "**":
        print(number_a ** number_b, "The power")
    if simbol == "//":
        print(number_a // number_b, "The floor division")
