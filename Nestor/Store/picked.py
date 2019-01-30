# picked


"""
This class instantiated one object to add items to cart.
"""
class Picked:
    """
    Method constructor.
    """
    def __init__(self):
        self.total_items_to_buy = 0
        self.items_price = []
        self.items_quantity = []

    """
    This method added one item into cart.
    item: type string is the item name.
    price: type int.
    quantity: type int.
    """
    def add_item(self, item, price, quantity):
        self.total_items_to_buy += 1
        self.items_price.append((item, price))
        self.items_quantity.append((item, quantity))

    """
    This method get item list with prices.
    :return: type list.
    """
    def get_prices(self):
        return self.items_price

    """
    This method ge ime list with quantities.
    :return: type list.
    """
    def get_quantities(self):
        return self.items_quantity
