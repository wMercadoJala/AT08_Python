from rodrigo.practice3.main.person import Person


class Employee(Person):
    def __init__(self, name, last_name, age, id, employee_id, department):
        super().__init__(name, last_name, age, id)
        self.employee_id = employee_id
        self.department = department

    def get_employee(self):
        string_format = "----Employee {0}----\nEmployeeID= {1}\nDepartment= {2}"
        return string_format.format(self.name, self.employee_id, self.department)


employee = Employee("Juan", "Cabrera", 99, 846215, 13, "Laboratory")
print(employee.get_employee())
print(employee.get_name())