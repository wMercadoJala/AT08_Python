from math import pi


def calc_area(radio_circle):
    return str(round(pi * radio_circle ** 2, 2)) if radio_circle >= 10 else "less than 10"


print(calc_area(9))
print(calc_area(14))
