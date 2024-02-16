class Product:
    def __init__(self, name, price, ):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product Name: {self.name} Price: {self.price}'


class Shop:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def buy_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return f'You have bought {product.name} for {product.price}'
        return 'Product not found'

    def __repr__(self):
        return f'Shop Name: {self.name} Location: {self.location} Products: {self.products}'


product1 = Product('Milk', 2)
product2 = Product('Bread', 1)
shop1 = Shop('Supermarket', 'Dhaka')
shop1.add_product(product1)

print(shop1.buy_product('Milk'))
