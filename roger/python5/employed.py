from roger.python5.person import Person


class Employed(Person):
    def __init__(self, name, last_name, age, ci, employed_id, department):
        super().__init__(name, last_name, age, ci)
        self.employed_id = employed_id
        self.department = department

    def get_employed(self):
        return self.name() + ", " + super().age + super().ci + self.employed_id + self.department

