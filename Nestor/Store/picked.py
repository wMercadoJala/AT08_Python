# picked


class Picked:
    def __init__(self):
        self.total_items_to_buy = 0
        self.items_price = []
        self.items_quantity = []

    def add_item(self, item, price, quantity):
        self.total_items_to_buy += 1
        self.items_price.append((item, price))
        self.items_quantity.append((item, quantity))

    def print_items_quantity(self):
        for item in self.items_quantity:
            print(f'{item[0]}: {item[1]}')
