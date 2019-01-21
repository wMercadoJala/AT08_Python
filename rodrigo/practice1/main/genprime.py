def list_values_primes(min, max):
    result = ""
    for number in range(min, max+1):
        result += "{0} is Prime?: {1} \n".format(str(number), str(isPrime(number)))
    return result


def isPrime(number):
    for num in range(2, int(number / 2) + 1):
        if number % num == 0:
            return False
    return True


print(list_values_primes(20,29))
