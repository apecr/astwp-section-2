from functools import reduce

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        price_list = [item['price'] for item in self.items]
        return reduce((lambda x, y: x + y), price_list)


store = Store('Alberto')
store.add_item('Thing1', 100)
store.add_item('Thing2', 200)
store.add_item('Thing3', 50)
print(store.stock_price())