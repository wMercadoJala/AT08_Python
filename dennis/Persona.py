class Persona:

    def __init__(self, first_name, last_name, age, ci):
        self.firstname = first_name
        self.lastname = last_name
        self.age = age
        self.ci = ci

    def get_name(self):
        return self.firstname + " " + self.lastname

    def get_age(self):
        return self.get_name() + ", " + self.age + " years old"

    def get_ci(self):
        return self.get_name() + ", " + self.ci
