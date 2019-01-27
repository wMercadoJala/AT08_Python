def equals(a, b):
    """
    This method ask if both number are equal.
    :param a: Input number a
    :param b: Input number b
    :return: Message of equal
    """
    print("Both numbers are equals") if a == b else print("Both numbers are not equals")


def not_equals(a, b):
    """
    This method ask if both number are not equal.
    :param a: Input number a
    :param b: Input number b
    :return: Message of not equal
    """
    print("Both numbers are not equals") if a != b else print("Both number are equals")


def greater(a, b):
    """
    This method ask if a its greater than b.
    :param a: Input number a
    :param b: Input number b
    :return: Message of greater
    """
    print("A it's greater than B") if a > b else print("A itsn't greater than B")


def smaller(a, b):
    """
    This method ask if a its smaller than b.
    :param a: Input number a
    :param b: Input number b
    :return: Message of not equal
    """
    print("A it's smaller than B") if a < b else print("A itsn't smaller than B")


def greater_equal(a, b):
    """
    This method ask if a its greater than or equal to b.
    :param a: Input number a
    :param b: Input number b
    :return: Message of not equal
    """
    print("A it's greater than or equal to B") if a >= b else print("A itsn't greater than or equal to B")


def smaller_equal(a, b):
    """
    This method ask if a its smaller than or equal to b.
    :param a: Input number a
    :param b: Input number b
    :return: Message of not equal
    """
    print("A it's smaller than or equal to B") if a <= b else print("A itsn't smaller than or equal to B")


def operate(symbol, number_a, number_b):
    """
    This method makes the operation between two number.
    :param symbol: Operation to do.
    :param number_a: Input number a.
    :param number_b: Input number b.
    :return: Message with the operation.
    """
    if symbol is "+":
        print(number_a + number_b, "The sum")
    if symbol is "-":
        print(number_a - number_b, "The substraction")
    if symbol is "*":
        print(number_a * number_b, "The multiplication")
    if symbol is "/":
        print(number_a / number_b, "The division")
    if symbol == "**":
        print(number_a ** number_b, "The power")
    if symbol == "//":
        print(number_a // number_b, "The floor division")
