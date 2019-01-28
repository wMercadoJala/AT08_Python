"""
According the amount of items picked . Create a class considering :
- Initial  amount of items to buy are 0
- Initial list of items with the specific price for each one
- Initial list of items with the quantity of each one
"""
from roger.python5.storeItems.item import Item
from roger.python5.storeItems.stock import Stock
"""
IN PROGRESS
"""


class Store:

    def __init__(self):
        self.stock = Stock()

    def get_stock(self):
        return self.stock.items_list

    def get_items(self):
        items_list = []
        for item in self.stock.items_list:
            items_list.append(item.item)
        return items_list

    def get_items_with_price(self):
        items_with_price = {}
        for item in self.stock.items_list:
            items_with_price[item.item] = item.price
        return items_with_price

    def get_items_with_amount(self):
        items_with_amount = {}
        for item in self.stock.items_list:
            items_with_amount[item.item] = item.amount
        return items_with_amount

