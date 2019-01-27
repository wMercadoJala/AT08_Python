from rodrigo.practice2.main.practice_circle import area
from rodrigo.practice2.main.practice_circle import perimeter


def user_circle():
    """
    Method for a user who can introduce radius of a circle and knows the area and the perimeter.
    :return: The characteristics of a circle.
    """
    radius = 0
    try:
        radius = int(input("Please, insert a radius of the circle-> "))
    except ValueError:
        print("Please, insert a number")
    print("The area of the circle is equal to {0:.4} [units]".format(area.of_circle(radius)))
    print("The perimeter of the circle is equal to {0:.4} [units]".format(perimeter.of_circle(radius)))


user_circle()
