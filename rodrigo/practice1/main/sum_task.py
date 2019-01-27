def sum_to(num):
    """
    This method makes the sum of all successive number under input num until 35.
    :param num: Input number.
    :return: The sum.
    """
    if num > 35:
        num = 35
    sum = 0
    for each_number in range(num):
        sum += each_number + 1
    return sum
