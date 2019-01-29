from roger.python5.storeItems.purchase import Purchase
from roger.python5.storeItems.stock import Stock
from roger.python5.storeItems.store import Store


def main():
    """
    This method simulates the purchase of an item.
    - Ask if you want to buy an item?
    - Print in console your purchase.
    - Print the balance of stock in store.
    """
    stock = Stock()
    stock.add_item('televisor', 700, 50)
    stock.add_item('radio', 150, 30)
    stock.add_item('xbox360', 500, 20)
    stock.add_item('tonka', 50, 15)
    store = Store(stock)
    purchase = Purchase(store)
    message = "Do you want to buy an item?\n1. Yes\n2. No\nSet number -> "
    while input(message) == '1':
        item = input("Item: ")
        amount = input("Amount: ")
        print(purchase.buy_item(item, amount))
    print("__________________")
    print("     Purchase     ")
    print("──────────────────")
    purchase.print_list_buy()
    print("Price total : ", purchase.total_price)
    print("__________________")
    print(" Balance of Store ")
    print("──────────────────")
    store.print_balance()
    print("Thanks...")


main()

