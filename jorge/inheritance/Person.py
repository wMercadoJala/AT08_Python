class Person:

    def __init__(self, name, last_name, age, ci):
        self.name = name
        self.lastname = last_name
        self.age = age
        self.ci = ci

    def get_full_name(self):
        return self.firstname + " " + self.lastname