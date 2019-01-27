def list_values_primes(min, max):
    """
    This method calculates a list of primes.
    :param min: Input min limit.
    :param max: Input max limit.
    :return: The list of primes.
    """
    result = ""
    for number in range(min, max + 1):
        result += "{0} is Prime?: {1} \n".format(str(number), str(is_prime(number)))
    return result


def is_prime(number):
    """
    This method ask if a number is prime.
    :param number: Input number.
    :return: Boolean True = Prime, False = Not prime
    """
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            return False
    return True


print(list_values_primes(20, 29))
