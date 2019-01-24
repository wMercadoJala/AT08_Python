from dennis import Pr_PerimeterCircle, Pr_AreaOfCircle


def main():
    radius = input("Please, enter a radius: ")
    while not radius.isdigit():
        radius = input(radius + " is not a valid radius. Please, enter a radius")
    print("Area of circle of " + radius + " is: "
          + Pr_AreaOfCircle.area_of_circle(int(radius)) +
          " and the perimeter is: " + Pr_PerimeterCircle.perim_of_circle(int(radius)))


if __name__ == "__main__":
    main()
