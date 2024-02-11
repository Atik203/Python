class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,price,items,quantity):
        product = {'price':price,'items':items,'quantity':quantity}
        self.cart.append(product)


    def remove(self,items):
        for product in self.cart:
            if product['items'] == items:
                self.cart.remove(product)
                return f'{items} removed'
        return 'Item not found'

    def checkout(self,amount):
        total = 0
        for product in self.cart:
            total += product['price'] * product['quantity']
        if(total<=amount):
            return f'Your change is {amount-total}'
        else:
            return 'Insufficient amount'


shopping = Shopping('John')
shopping.add_to_cart(10,'apple',2)
shopping.add_to_cart(5,'banana',3)
print(shopping.name,shopping.cart)
print(shopping.checkout(100))
print(shopping.remove('apple'))