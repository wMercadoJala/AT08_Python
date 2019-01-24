from abel.practice3.inheritance import person


class employee(person.person):

    def __init__(self, name, last_name, age, ci, employe_id, departament):
        """
        :param name:
        :param last_name:
        :param age:
        :param ci:
        :param employe_id:
        :param departament:
        """
        super().__init__(name, last_name, age, ci)

        self.employee_id = employe_id
        self.departament = departament

    def view(self):
        print("is a employed")


person_1 = person.person("abel", "mallcu", "4", "545")

employee_1 = employee("abel", "mallcu", "4", "545", "88888888", "tarija")

person_1.view()
employee_1.view()

print(employee_1.departament)
print(person_1.last_name)
