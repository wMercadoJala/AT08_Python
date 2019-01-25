import logging

from rodrigo.practice3.main.page.store import Store

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Purchase:

    def __init__(self):
        self.storage_items = Store()
        self.storage_items.storage("black marker", 20, 100)
        self.storage_items.storage("blue marker", 25, 100)
        self.storage_items.storage("red marker", 15, 150)

    def buy(self, items):
        logger.info("Start to buy items")
        total_price = 0
        for item in items:
            item_name, price, amount = self.storage_items.ask_for_item(item[0])
            quantity = item[1]
            if quantity > amount:
                logger.warning("The amount its to much than initial storage")
                print("We dont have enough items")
            else:
                logger.debug("Item: {0} Price: {1} Amount: {2}".format(item_name, price, amount))
                self.storage_items.decrease_amount(item[0], quantity)
                total_price = total_price + (price * quantity)
                print("Item Selected: {0} {1} units\nPrice: {2}".format(item_name, item[1], str(price * quantity)))
        return total_price

    def show_existing_items(self):
        logger.info("Showing the storage items")
        print(self.storage_items.items)


purchase = Purchase()
items_to_buy = [("black marker", 10), ("blue marker", 4)]
print(purchase.buy(items_to_buy), "<- total price")
purchase.show_existing_items()
