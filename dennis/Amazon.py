class Store:

    def __init__(self, items=["Headphones"], prices=[120], amount=[30]):
        self.list_items = []
        for index in range(len(items)):
            elem = (items[index], prices[index], amount[index])
            self.list_items.append(elem)

    def get_items(self):
        return self.list_items

    def rest_item(self, item, amount):
        for elem in self.list_items:
            if elem[0] is item:
                elem[2] = (elem[2] - amount) if elem[2] > amount else 0
