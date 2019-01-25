from Amazon import Store


class Client:

    def __init__(self, name):
        self.name = name
        self.store = Store(["Cookies", "Drink", "Ice-creams"], [5, 2, 3], [10, 10, 20])

    def pickup(self, item_picked_up, item_amount):
        self.store.rest_item(item_picked_up, item_amount)
