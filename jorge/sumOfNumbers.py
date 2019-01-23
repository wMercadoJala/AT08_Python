def sum_to(number):
    result = 0
    for num in range(number + 1):
        if num < 35:
            result += num
    return result


print(sum_to(5))

