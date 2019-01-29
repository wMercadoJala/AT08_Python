"""
According the amount of items picked . Create a class considering :
- Initial  amount of items to buy are 0
- Initial list of items with the specific price for each one
- Initial list of items with the quantity of each one
"""


class Store:
    """
    This class represent a Store.
    """

    def __init__(self, stock):
        """
        Constructor of class Store.
        :param stock: object Stock.
        """
        self.Stock = stock

    def get_stock(self):
        """
        This method get Stock.
        :return: Object Stock.
        """
        return self.Stock

    def get_items(self):
        """
        This method get only items in stock.
        :return: List with the items in stock.
        """
        items_list = []
        for item in self.Stock.items_list:
            items_list.append(item.item)
        return items_list

    def get_items_with_price(self):
        """
        This method get a list with items and prices in Stock.
        :return:Dictionary.
        """
        items_with_price = {}
        for item in self.Stock.items_list:
            items_with_price[item.item] = item.price
        return items_with_price

    def get_items_with_amount(self):
        """
        This method get a list with items and amount in Stock.
        :return:Dictionary.
        """
        items_with_amount = {}
        for item in self.Stock.items_list:
            items_with_amount[item.item] = item.amount
        return items_with_amount

    def item_in_stock(self, item):
        """
        This method verify if an item exist in Stock.
        :param item: Required Item.
        :return: Boolean value.
        """
        return True if item in self.get_items() else False

    def exist_this_amount_item(self, item, amount):
        """
        This method verify if an amount of item exist in Stock.
        :param item: Required item.
        :param amount: Required amount.
        :return: Boolean value.
        """
        return True if amount <= self.get_items_with_amount()[item] else False

    def print_balance(self):
        """
        This method print in console all items in Stock.
        """
        self.Stock.show_items()
