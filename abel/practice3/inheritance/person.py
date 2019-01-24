class person:

    def __init__(self, name, last_name, age, ci):
        """

        :param name:
        :param last_name:
        :param age:
        :param ci:
        """
        self.name = name
        self.last_name = last_name
        self.age = age
        self.ci = ci

    def view(self):
        print("is a  person ")
