def sum_to(number):
    result_sum = 0
    for num in range(number + 1):
        if num < 35:
            result_sum += num
    return result_sum


number_to_sum = 23
print("sum to of " + str(number_to_sum) + " is: " + str(sum_to(number_to_sum)))
