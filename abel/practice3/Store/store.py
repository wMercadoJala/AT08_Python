class store:
    products = []

    def new_article(self, item_name, price, amount):
        product = (item_name, price, amount)
        self.products.append(product)

    def query(self, item_name):
        for item_query in self.products:
            return item_query if item_query[0] == item_name else "item not exist"

    def reduce_stok(self, item_name, amount_of_purchace):
        for item_query in self.products:
            if item_query[0] == item_name:
                position = self.products.index((item_query[0], item_query[1], item_query[2]))
                self.products[position] = (item_query[0], item_query[1], item_query[2] - amount_of_purchace)

    def view_products(self):
        print(self.products)


sto = store()
sto.new_article("Sony vaio", "987 $$", 10)
sto.new_article("Toshiba", "987 $$", 0)
sto.new_article("Dell", "987 $$", 0)
sto.view_products()
print(sto.query("Sony vaio"))
print(sto.reduce_stok("Sony vaio", 3))
sto.view_products()
