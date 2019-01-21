import math


def of_circle(radius):
    if radius < 10:
        return None
    return "{0:.5}".format(math.pi * radius ** 2)
