class user:

    def __init__(self, nickname):
        self.nick_name = nickname
        self.name = {}
        self.age = {}

    def fill_date_user(self, name, age):
        self.name.update({"name" : name})
        self.age.update({"age" : age})

    def get_nickname(self):
        return self.nick_name

    def get_name(self):
        return self.name.get("name")

    def get_age(self):
        return self.age.get("age")

