import math


def of_circle(radius):
    """
    This method calculates the area of circle if the radius is greater than 10.
    :param radius: Input radius.
    :return: The area.
    """
    if radius < 10:
        return None
    return "{0:.5}".format(math.pi * radius ** 2)
