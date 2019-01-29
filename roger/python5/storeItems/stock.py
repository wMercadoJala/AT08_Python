"""
2. Create a class to pickup items
"""
from roger.python5.storeItems.item import Item


class Stock:
    """
    This class represent a stock of a Store.
    """
    def __init__(self):
        """
        Constructor of class Stock.
        """
        self.items_list = []
        self.amount_items = 0

    def add_item(self, item, price, amount):
        """
        This method add an object Item in items list.
        :param item: New Item.
        :param price: Price of item.
        :param amount: Amount of item in stock.
        """
        self.items_list.append(Item(item.lower(), price, amount))
        self.amount_items += 1

    def show_items(self):
        """
        This method show and print in console all the items in Stock.
        """
        for item in self.items_list:
            print("Item:{0} Price:{1} Amount:{2}".format(item.item, item.price, item.amount))

    def set_amount(self, item, amount_buy):
        """
        This method update the amount of an item in the Stock.
        :param item: Item.
        :param amount_buy: Amount sold.
        """
        for element in self.items_list:
            if element.item == item:
                element.amount = element.amount - amount_buy
                break
