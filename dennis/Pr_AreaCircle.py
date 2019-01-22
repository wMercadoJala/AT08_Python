from math import pi


def area_of_circle(radio):
    if radio >= 10:
        area = "the area of circle with radio " + str(radio) + " meters is: " + str(round(pi * radio**2, 2)) + " Meters"
    else:
        area = "radius less than 10"
    return area


print(area_of_circle(11))
print(area_of_circle(3))
print(area_of_circle(7.5))
print(area_of_circle(28))
