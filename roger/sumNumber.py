def sum_to(number):
    result = 0
    for index in range(0, number + 1):
        if index <= 35:
            result += index
    return result


print("total sum to 2: " + str(sum_to(2)))
print("total sum to 3: " + str(sum_to(3)))
print("total sum to 34: " + str(sum_to(34)))
print("total sum to 35: " + str(sum_to(35)))
print("total sum to 36: " + str(sum_to(36)))
print("total sum to 40: " + str(sum_to(40)))
