# item


"""
This class instantiate single object item.
"""
class Item:
    """
    Method constructor.
    name: type string.
    price: type int.
    amount: type int, is the quantity in stock.
    """
    def __init__(self, name, price, amount):
        self.item = {'name': name, 'price': price, 'amount': amount}
