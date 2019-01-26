# store

import item
import picked


class Store:
    def __init__(self):
        self.item_list = []
        self.picked_list = picked.Picked()

    def create_item(self, name, price, amount):
        self.item_list.append(item.Item(name, price, amount))

    def item_balance(self):
        for element in self.item_list:
            print(f'item: {element.name}, price: {element.price}, quantity: {element.amount}')

    def get_price_item(self, name):
        for element in self.item_list:
            if element.name == name:
                return element.price
        raise ValueError

    def item_picked(self, name, quantity):
        try:
            self.picked_list.add_item(name, self.get_price_item(name), quantity)
        except ValueError:
            print('This item do not exist in our store.')

    def print_picked_list(self):
        self.picked_list.print_items_quantity()


my_store = Store()
my_store.create_item('Toshiba', 700, 5)
my_store.create_item('Samsung', 300, 12)
my_store.create_item('HP', 650, 5)
my_store.create_item('Huawei', 250, 12)
my_store.item_balance()
my_store.item_picked('Toyota', 0)
my_store.item_picked('Samsung', 2)
my_store.item_picked('Toshiba', 1)
my_store.print_picked_list()
