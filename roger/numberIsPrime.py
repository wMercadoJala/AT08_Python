def range_numbers_primes(limit_low, limit_max):
    """
    Method for identify if the number is prime or not, in a list of values between a Min and Max range, .
    :param limit_low: Lower number of the range.
    :param limit_max: Maxim number of the range.
    :return: string with the numbers prime and not primes.
    """
    range_numbers = ""
    for value in range(limit_low, limit_max + 1):
        if is_prime(value):
            range_numbers += str(value) + " is prime\n"
        else:
            range_numbers += str(value) + " is not prime\n"
    return range_numbers


def is_prime(number):
    """
    Method for determinate if a number is prime.
    :param number: Integer number.
    :return: boolean.
    """
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            return False
    return True


print(range_numbers_primes(1, 20))
