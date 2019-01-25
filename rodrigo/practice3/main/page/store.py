import logging

logger = logging.getLogger(__name__)


class Store:
    def __init__(self):
        self.amount_items = 0
        self.items = []

    def storage(self, item, price, amount):
        logger.info("Item stored")
        item_tuple = (item, price, amount)
        self.items.append(item_tuple)

    def ask_for_item(self, item):
        logger.info("Ask for the item")
        for item_store in self.items:
            if item_store[0] == item:
                return item_store
        logger.warning("The items doesn't exist")
        return None

    def decrease_amount(self, item, quantity):
        logger.info("Decreasing amount")
        for item_store in self.items:
            if item_store[0] == item:
                index = self.items.index((item_store[0], item_store[1], item_store[2]))
                self.items[index] = (item_store[0], item_store[1], item_store[2] - quantity)
