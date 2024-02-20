from Menu import Menu, Burger, Pizza, Drink
from Restaurant import Restaurant
from User import Chef, Manager, Server, Customer
from Order import Order


def main():
    menu = Menu()
    pizza1 = Pizza("Margherita", 450, "Large", ["Cheese", "Tomato", "Basil"])
    pizza2 = Pizza("Pepperoni", 350, "Medium", ["Cheese", "Tomato", "Pepperoni"])
    burger1 = Burger("Beef Burger", 180, "Beef", ["Bun", "Cheese", "Lettuce", "Tomato"])
    burger2 = Burger("Chicken Burger", 250, "Chicken", ["Bun", "Cheese", "Lettuce", "Tomato"])
    drink1 = Drink("Coke", 20)
    drink2 = Drink("Pepsi", 20)
    drink3 = Drink("Coffe", 30, False)
    menu.add_food_item(pizza1, "pizza")
    menu.add_food_item(pizza2, "pizza")
    menu.add_food_item(burger1, "burger")
    menu.add_food_item(burger2, "burger")
    menu.add_food_item(drink1, "drink")
    menu.add_food_item(drink2, "drink")
    menu.add_food_item(drink3, "drink")

    menu.show_menu()

    # add employee
    restaurant = Restaurant("Atik Restaurant", 1000, menu)
    chef = Chef("Rahim", "123456", "rahim@gmail.com", "Dhaka", 1000, "01-01-2021", "Kitchen", "Pizza")
    manager = Manager("Karim", "123456", "karim@gmail.com", "Dhaka", 2000, "01-01-2020", "Admin")
    server = Server("Shahin", "123456", "shahin@gmail.com", "Dhaka", 500, "01-01-2022", "Server")

    restaurant.add_employee("chef", chef)
    restaurant.add_employee("manager", manager)
    restaurant.add_employee("server", server)

    restaurant.show_employee()

    # customer place order

    customer = Customer("Sakib", "123456", "sakib@gmail.com", "Dhaka")
    order1 = Order(customer, [pizza1, burger1, drink1])
    customer.place_order(order1)
    restaurant.add_order(order1)
    restaurant.received_payment(order1, 2500, customer)
    print("revenue and balance", restaurant.revenue, restaurant.balance)

    # 2nd customer place order
    customer1 = Customer("Roni", "123456", "sakib@gmail.com", "Dhaka")
    order2 = Order(customer1, [pizza2, pizza1, burger1, burger2, drink2, drink3, drink1])
    customer1.place_order(order2)
    restaurant.add_order(order2)
    restaurant.received_payment(order2, 2000, customer1)
    print("revenue and balance after 2nd customer", restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, "Rent")
    print("balance after paying rent", restaurant.balance)

    restaurant.pay_salary(server)
    print("balance after paying chef salary", restaurant.balance)

if __name__ == "__main__":
    main()
