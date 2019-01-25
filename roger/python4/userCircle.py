import re

from roger.python4.modules import areaOfCircle as area
from roger.python4.modules import perimeterOfCircle as perimeter

"""
Create a script to ask to the user of the radio and print both results (area and perimeter).
"""


def circle_user():
    radius = ''
    while not (radius.isdigit() or re.match(r'\d+\.\d+', radius)):
        print("Please insert number value.")
        radius = input("Insert radius of circle -> ")
    print("     Area of circle with radius {0} is:".format(radius), area.area_is(radius))
    print("Perimeter of circle with radius {0} is:".format(radius), perimeter.perimeter_is(radius))


circle_user()
