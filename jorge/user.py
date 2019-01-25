class user:

    def __init__(self, id_user):
        self.id_user = id_user
        self.name = {}
        self.age = {}

    def fill_date_user(self, name, age):
        self.name.update({"name" : name})
        self.age.update({"age" : age})

    def get_nickname(self):
        return self.id_user

    def get_name(self):
        return self.name.get("name")

    def get_age(self):
        return self.age.get("age")

