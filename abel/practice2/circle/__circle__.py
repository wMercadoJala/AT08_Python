from math import pi


def area_circle(radio):
    return str(round(pi * radio ** 2, 2))


def perimeter_circle(radio):
    return str(round(2 * radio * pi, 2))
