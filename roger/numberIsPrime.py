def range_numbers_primes(limit_low, limit_max):
    range_numbers = ""
    for value in range(limit_low, limit_max + 1):
        if is_prime(value):
            range_numbers += str(value) + " is prime\n"
        else:
            range_numbers += str(value) + " is not prime\n"
    return range_numbers


def is_prime(number):
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            return False
    return True


print(range_numbers_primes(1, 20))
