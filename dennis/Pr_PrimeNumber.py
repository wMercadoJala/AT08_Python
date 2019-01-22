Min = 3
Max = 100


def is_prime_number(number):
    if number in range(Min, Max):
        if number % 2 == 0:
            return str(number)+" even number, not prime."
        return is_prime_odd_number(number)
    return "Out of range."


def is_prime_odd_number(number):
    limit = number // 2
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return str(number) + " not prime."
    return str(number) + " prime."


print(is_prime_number(103))
print(is_prime_number(46))
print(is_prime_number(7))
print(is_prime_number(97))
print(is_prime_number(38))
print(is_prime_number(15))
