"""
This class represent a person.
"""


class Person:
    def __init__(self, name, last_name, age, ci):
        """
        Constructor class Person.
        :param name: Name of person.
        :param last_name: Las name of person.
        :param age: Age of person.
        :param ci: Number of CI of person.
        """
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def names(self):
        """
        Method for return name and last name of person.
        :return: String with the person data.
        """
        return "{0} {1}".format(self.name, self.last_name)
