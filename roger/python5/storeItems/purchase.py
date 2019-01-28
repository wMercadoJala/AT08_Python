"""

Create a class to perform purchase an item(ask for the item and for the amount,
after an item is buy, you should decrease the amount of data, also need to calculate
the total price, after this is calculated need to ask if the user would like to buy any other item.
"""
from roger.python5.storeItems.store import Store


class Purchase:

    def __init__(self, item, amount):

        self.item_buy = item
        self.amount_buy = amount

    def ask_for_item(self):
        for item_stock in Store.get_items():
            if self.item_buy is item_stock:
                return True
        return False

    def buy_item(self):
        if self.ask_for_item():
            return True







    
