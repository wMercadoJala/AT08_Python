def even_or_odd(number):
    """
    Method for determine is a number is odd or even.
    :param number: Integer number Maxim number of the range
    :return: String with a list of number odd and even.
    """
    return "The number " + str(number) + " is even" if number % 2 == 0 else "The number " + str(number) + " is odd"


print(even_or_odd(1))
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(4))
