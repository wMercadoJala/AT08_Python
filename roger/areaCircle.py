from math import pi


def area_of_circle(radio):
    """
    This method calculates the area of ​​the circle by entering a radius minor to 10.
    :param radio: Radius of circle.
    :return: string with the area of circle with radio minor to 10.
    """
    return \
        {True: "Area of circle with radio " + str(radio) + " is: " + str(
            round(pi * radio ** 2, 2)) + " Meters"
            , False: "radius less than 10"}[radio > 10]


print(area_of_circle(20))
print(area_of_circle(15))
print(area_of_circle(5))
print(area_of_circle(9))
