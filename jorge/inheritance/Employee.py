from jorge.inheritance.Person import Person


class Employee(Person):

    def __init__(self, name, last_name, age, ci, employee_id, departament):
        super().__init__(name, last_name, age, ci)
        self.employee_id = employee_id
        self.departament = departament

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber