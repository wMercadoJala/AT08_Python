"""

Create a class to perform purchase an item(ask for the item and for the amount,
after an item is buy, you should decrease the amount of data, also need to calculate
the total price, after this is calculated need to ask if the user would like to buy any other item.
"""
from roger.python5.storeItems.store import Store


class Purchase:

    def __init__(self):
        self.list_purchase = {}
        self.total_price = 0

    def ask_for_item(self, item_buy, amount_buy):
        if Store().item_in_stock(item_buy):
            self.buy_item(item_buy, amount_buy)

    def buy_item(self, item, amount):










    
