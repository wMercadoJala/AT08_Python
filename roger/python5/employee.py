from roger.python5.person import Person
"""
This class represent a employee extends of Person.
"""


class Employee(Person):
    def __init__(self, name, last_name, age, ci, employed_id, department):
        """
        Constructor class Employee.
        :param name: Name of employee.
        :param last_name: Las name of employee.
        :param age: Age of employee.
        :param ci: Number of CI of employee.
        :param employed_id: Number of ID of employee.
        :param department: Department of employee.
        """
        super().__init__(name, last_name, age, ci)
        self.employee_id = employed_id
        self.department = department

    def get_employee(self):
        """
        Methof for return employee data..
        :return: String with the employee data.
        """
        return "Employee : {0} {1}¨\nAge: {2}\nC.I.: {3}\nEmployed ID: {4}\nDepartment: {5}"\
            .format(self.name, self.last_name, self.age, self.ci, self.employee_id, self.department)


employee = Employee("Marneus", "Calgar", 85, 40000, 1, "administration")
print(employee.get_employee())
print("Person:", employee.names())
