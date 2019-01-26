"""
IN PROGRESS
2. Create a class to pickup items
"""
from roger.python5.storeItems.item import Item


class Stock:
    def __init__(self):
        self.items_list = []
        self.amount_items = 0

    def add_item(self, item, price, amount):
        self.items_list.append(Item(item, price, amount))
        self.amount_items += 1

    def show_items(self):
        for item in self.items_list:
            print("Item:{0} Price:{1} Amount:{2}".format(item.item, item.price, item.amount))

