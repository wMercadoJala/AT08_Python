# Create python script applying at least one time each one of the operators learned.
# Print the values and the condition that give you the result obtained.
import math

a = 10
b = 20
c = 30

a += b
print('a + b = c') if a == c else print('a + b is not equal to c')
a -= c
print('a - c = 0') if a != c else print('a - c is not equal to zero')

a = 10
b = 20
c = 30

c /= a
b *= a

print('c = 30, a = 10 => c /= a is:', c)
print('b = 20, a = 10 => b *= a is:', b)
b %= a
print('b = 200, a = 10 => b %= a is:', b)

# Create 1 script to determine is a number is odd or even (use single line statement if applies)

number = 51

print('number', number, 'is even') if number % 2 == 0 else print('number', number, 'is odd')

# According a list of values between a Min and Max range, identify if the number is prime or not.

max_range = 110


def primes_list(num):
    primes = []
    for possible_rime in range(2, num + 1):
        is_prime = True
        for iterate in range(2, int(possible_rime ** 0.5) + 1):
            if possible_rime % iterate == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possible_rime)

    return primes


print(primes_list(max_range))


# Write a function area_of_circle(r) which returns the area of a circle of radius r only if the radius value is
# greater of 10.

def area_of_circle(radius):
    area = math.pi * math.pow(radius, 2)
    print('Area of circle is:', area) if area > 10 else print('Area of circle is less than 10')
    return


area_of_circle(5)
area_of_circle(1)

# Write a function sum_to(n) that returns the sum of all integer numbers up to and including only until any value
# lower than 35. So sum_to(10) would be 1+2+3...+10 which would return the value 55, but if n=40 only until sum to 35
# need to be returned.


def sum_to(n):
    result = 0
    for loop in range(1, n + 1):
        result += loop
        if loop == 35:
            break
    return result


print('Summarized 10 first numbers:', sum_to(10))
print('Summarized 40 first numbers:', sum_to(40))

# Write a function days_in_month which takes the name of a month, and returns the number of days in the month. Ignore
# leap years:
# days_in_month("February") == 28
# days_in_month("December") == 31
# If the function is given invalid arguments, it should return None.


def days_in_month(month):
    months31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    months30 = ['April', 'Jun', 'September', 'November']
    if month == 'February':
        return 28
    if month in months31:
        return 31
    if month in months30:
        return 30
    return 'None'


print(days_in_month('Cesar'))
print(days_in_month('February'))
print(days_in_month('September'))
print(days_in_month('December'))
