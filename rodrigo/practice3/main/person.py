class Person:
    """
    This class represent a person
    """

    def __init__(self, name, last_name, age, id):
        """
        Constructor for set the initial values of the class.
        :param name: Input name
        :param last_name: Input last_name
        :param age: Input age
        :param id: Input id
        """
        self.name = name
        self.last_name = last_name
        self.age = age
        self.id = id

    def get_name(self):
        """
        This method get the name and last_name of the person
        :return: String name
        """
        return "{0} {1}".format(self.name, self.last_name)
