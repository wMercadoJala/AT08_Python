# store

import item
import picked
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('info.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


"""
This class instantiated object store.
"""
class Store:
    def __init__(self):
        self.item_list = []
        self.picked_list = picked.Picked()

    def create_item(self, name, price, amount):
        self.item_list.append(item.Item(name, price, amount))

    def item_balance(self):
        for element in self.item_list:
            print(f"item: {element.item['name']}, price: {element.item['price']}, quantity: {element.item['amount']}")

    def get_price_item(self, name):
        for element in self.item_list:
            if element.item['name'] == name:
                return element.item['price']
        raise ValueError

    def item_picked(self, name, quantity):
        try:
            self.picked_list.add_item(name, self.get_price_item(name), quantity)
            logger.info('Adding item picked successfully.')
        except ValueError:
            print('This item do not exist in our store.')
            logger.info(f'Item {name} not found in our list store.')

    def update_balance(self, name, quantity):
        for element in self.item_list:
            if element.item['name'] == name:
                element.item['amount'] -= quantity
                return
        raise ValueError

    def purchase(self):
        try:
            for items in self.picked_list.get_quantities():
                self.update_balance(items[0], items[1])
            logger.info('All items has been bought successfully.')
        except ValueError:
            print('Cannot make purchase.')
            logger.info('One or more items could not bought.')

    def total_purchase(self):
        total_price = 0
        for items in self.picked_list.get_quantities():
            print(f"Item: {items[0]} :: Quantity: {items[1]} =>",
                  '{:8.2f}'.format(items[1] * self.get_price_item(items[0])))
            total_price += items[1] * self.get_price_item(items[0])
        print('{:-^40}'.format(''))
        print('Total price', '{:28.2f}'.format(total_price))


my_store = Store()
my_store.create_item('Toshiba', 700, 5)
my_store.create_item('Samsung', 300, 12)
my_store.create_item('HP', 650, 5)
my_store.create_item('Huawei', 250, 12)
print('==========[Items Balance]==========')
my_store.item_balance()
my_store.item_picked('Toyota', 10)
my_store.item_picked('Samsung', 2)
my_store.item_picked('Toshiba', 1)
my_store.purchase()
print('==========[Items Balance]==========')
my_store.item_balance()
print('==========[Total Purchase]==========')
my_store.total_purchase()
