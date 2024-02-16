class Book:
    def __init__(self, name, id, quantity):
        self.name = name
        self.id = id
        self.quantity = quantity


class User:
    def __init__(self, name, id, password):
        self.name = name
        self.password = password
        self.id = id
        self.borrowed_books = []
        self.return_books = []


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, id, name, quantity):
        book = Book(name, id, quantity)
        self.books.append(book)
        print(f'{name} book Added Successfully\n')

    def add_user(self, name, id, password):
        user = User(name, id, password)
        self.users.append(user)
        return user

    def remove_book(self, id):
        for book in self.books:
            if book.id == id:
                self.books.remove(book)
                print(f"{book.name} Removed Successfully")
                break
        else:
            print("Book not found")

    def borrow_book(self, id, user):
        for book in self.books:
            if book.id == id:
                if book in user.borrowed_books:
                    print("You have already borrowed this book")
                    break
                else:
                    if book.quantity > 0:
                        book.quantity -= 1
                        user.borrowed_books.append(book)
                        print(f"{book.name} Borrowed Successfully")
                        break
            else:
                print("Book not found or out of stock")

    def return_book(self, id, user):
        for book in user.borrowed_books:
            if book.id == id:
                book.quantity += 1
                user.borrowed_books.remove(book)
                user.return_books.append(book)
                print(f"{book.name} Returned Successfully")
                break
        else:
            print("Book not found or not borrowed")






libray = Library("My Library")

admin = libray.add_user("admin", 101, "admin")
normal_user = libray.add_user("user", 102, "user")
libray.add_book(1, "Python", 50)
libray.add_book(2, "Java", 20)
libray.add_book(3, "C++", 30)

current_user = None
while True:
    if current_user is None:
        print("Currently No Logged in User")
        option = int(input("1. Login\n2. Register\n"))
        if option == 1:
            user_id = int(input("Enter User ID (Integer only): "))
            password = input("Enter Password: ")
            for user in libray.users:
                if user.id == user_id and user.password == password:
                    current_user = user
                    break
            else:
                print("Invalid User ID or Password or User not found")
        elif option == 2:
            name = input("Enter Name: ")
            user_id = int(input("Enter User ID (Integer only): "))
            password = input("Enter Password: ")
            for Id in libray.users:
                if user_id == Id:
                    print("User already exists")
                    break
            user = libray.add_user(name, user_id, password)
            current_user = user
            print("User Registered Successfully")


    else:
        print(f'Welcome Back {current_user.name}')
        if current_user.name == "admin":
            print("Options:")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. View Books")
            print("4. View Users")
            print("5. Logout")

            option = int(input("Enter Option: "))
            if option == 1:
                name = input("Enter Book Name: ")
                id = int(input("Enter Book ID: "))
                quantity = int(input("Enter Book Quantity: "))
                libray.add_book(id, name, quantity)

            elif option == 2:
                id = int(input("Enter Book ID to remove: "))
                libray.remove_book(id)

            elif option == 3:
                for book in libray.books:
                    print(f"ID: {book.id}, Name: {book.name}, Quantity: {book.quantity}")

            elif option == 4:
                for user in libray.users:
                    print(f"ID: {user.id}, Name: {user.name}")

            else:
                current_user = None
                print("Logged out Successfully")


        else:
            print("Options:")
            print("1.Borrow Book")
            print("2.Return Book")
            print("3.View borrowed Books")
            print("4.View returned Books")
            print("5. Logout")

            option = int(input("Enter Option: "))
            if option == 1:
                id = int(input("Enter Book ID to borrow: "))
                libray.borrow_book(id, current_user)

            elif option == 2:
                id = int(input("Enter Book ID to return: "))
                libray.return_book(id, current_user)

            elif option == 3:
                for book in current_user.borrowed_books:
                    print(f"ID: {book.id}, Name: {book.name}, Quantity: {book.quantity}")

            elif option == 4:
                for book in current_user.return_books:
                    print(f"ID: {book.id}, Name: {book.name}, Quantity: {book.quantity}")


            else:
                current_user = None
                print("Logged out Successfully")
