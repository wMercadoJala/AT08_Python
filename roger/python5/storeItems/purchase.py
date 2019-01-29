"""

Create a class to perform purchase an item(ask for the item and for the amount,
after an item is buy, you should decrease the amount of data, also need to calculate
the total price, after this is calculated need to ask if the user would like to buy any other item.
"""


class Purchase:
    """
    This class represent a purchase.
    """

    def __init__(self, store):
        """
        Constructor of class.
        :param store: object Store.
        """
        self.list_purchase = {}
        self.total_price = 0
        self.Store = store

    def buy_item(self, item, amount):
        """
        This method buy a item in store.
        :param item: Required Item.
        :param amount: Required amount.
        :return: String status message.
        """
        item_buy = item.lower()
        amount_buy = int(amount)
        if not self.ask_for_item(item_buy):
            return "The item is not in stock."
        elif not self.ask_for_amount(item_buy.lower(), amount_buy):
            return "There is no such quantity in stock."
        else:
            self.Store.get_stock().set_amount(item_buy, amount_buy)
            self.add_to_list(item_buy, amount_buy)
            return "Purchased Item"

    def ask_for_item(self, item):
        """
        This method ask in Store if item exist.
        :param item: Required item.
        :return: boolean value.
        """
        return self.Store.item_in_stock(item)

    def ask_for_amount(self, item, amount):
        """
        This method ask in Store if amount of item exist.
        :param item: Required item.
        :param amount: Required amount of item.
        :return: boolean value.
        """
        return self.Store.exist_this_amount_item(item, amount)

    def add_to_list(self, item, amount):
        """
        This method add item in purchase list and calculate the price total of items.
        :param item: Required item.
        :param amount: Required amount of Item.
        """
        new_buy = {}
        individual_price = self.Store.get_items_with_price()[item]
        total_price = individual_price * amount
        new_buy['amount'] = amount
        new_buy['price'] = individual_price
        new_buy['total'] = total_price
        self.list_purchase[item] = new_buy
        self.total_price = self.total_price + total_price

    def print_list_buy(self):
        """
        This method print in console the purchased items list and total price of items.
        """
        for item in self.list_purchase:
            print("Item:{0} Amount:{1} Individual Price:{2} Total Price:{3}"
                  .format(item, self.list_purchase[item]['amount'], self.list_purchase[item]['price']
                          , self.list_purchase[item]['total']))
