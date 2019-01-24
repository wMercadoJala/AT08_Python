from math import pi


def area_of_circle(radio):
    area = (lambda: "radius less than 10", lambda: "the area is: " + str(round(pi * radio**2, 2)) + " Meters")[radio >= 10]()
    return area


print(area_of_circle(30))
print(area_of_circle(9))

