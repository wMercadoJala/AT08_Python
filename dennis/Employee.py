from Persona import Persona


class Employee(Persona):

    def __init__(self, first_name, last_name, age, ci, id_number, department):
        super().__init__(first_name, last_name, age, ci)
        self.id_number = id_number
        self.department = department

    def get_employee(self):
        return self.get_name() + ", " + self.id_number + ", " + self.department
