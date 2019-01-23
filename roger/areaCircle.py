from math import pi


def area_of_circle(radio):
    return \
        {True: "Area of circle with radio " + str(radio) + " is: " + str(
            round(pi * radio ** 2, 2)) + " Meters"
            , False: "radius less than 10"}[radio > 10]


print(area_of_circle(20))
print(area_of_circle(15))
print(area_of_circle(5))
print(area_of_circle(9))
