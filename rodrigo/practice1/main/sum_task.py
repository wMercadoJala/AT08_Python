def sum_to(num):
    if num > 35:
        num = 35
    sum = 0
    for each_number in range(num):
        sum += each_number + 1
    return sum
