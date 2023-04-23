from tkinter import messagebox, ttk
import mysql.connector
import tkinter as tk


def tableprint(lst):
    # Print MySQL output as a table, padded for readability
    widths = []
    columns = []
    border = '|'
    separator = '+'
    length = ['' for i in range(len(lst[0]))]
    for i in range(len(lst[0])):
        length[i] = max(list(map(lambda x: len(str(x[i])), lst)))

    i = 0
    for cd in cursor.description:
        widths.append(max(length[i], len(cd[0])))
        columns.append(cd[0])
        i += 1

    for w in widths:
        border += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(border % tuple(columns))
    print(separator)
    for row in lst:
        print(border % row)
    print(separator)


def customer_menu():
    # Customer menu
    while True:
        print("What would you like to do?")
        print("1. Show all books")
        print("2. Search for a book")
        print("3. Add to cart")
        print("4. Check out")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Show all books
            cursor.execute("SELECT * FROM Book")
            books = cursor.fetchall()
            tableprint(books)

        elif choice == "2":
            # Search for a book
            isbn = input("Enter the ISBN of the book you want to search for: ")
            cursor.execute("SELECT * FROM Book WHERE ISBN=%s" % isbn)
            book = cursor.fetchone()
            if book is None:
                print("Book not found")
            else:
                print("ISBN:", book[0])
                print("Title:", book[1])
                print("Author:", book[2])
                print("Publisher:", book[3])
                print("Publication Date:", book[4])
                print("Price:", book[5])
                print("Quantity:", book[6])

        elif choice == "3":
            # Add to cart
            isbn = input(
                "Enter the ISBN of the book you want to add to cart: ")
            quantity = input(
                "Enter the quantity of the book you want to add to cart: ")

            cursor.execute("SELECT * FROM Book WHERE ISBN=%s" % isbn)
            book = cursor.fetchone()
            if book is None:
                print("Book not found")
            else:
                if int(quantity) > int(book[6]):
                    print("Quantity not available")
                else:
                    cart[isbn] = quantity

            print("Book added to cart")

        elif choice == "4":
            # Check out
            customer_name = input("Enter your name: ")
            customer_email = input("Enter your email address: ")
            customer_phone = input("Enter your phone number: ")
            customer_address = input("Enter your address: ")
            cursor.execute("INSERT INTO Customer (Name, Email, Phone, Address) VALUES ('%s', '%s', '%s', '%s')" % (
                customer_name, customer_email, customer_phone, customer_address))
            connection.commit()
            customer_id = cursor.lastrowid
            cursor.execute(
                "INSERT INTO `Order` (Customer_ID, Order_Date) VALUES ( %s, now())" % (customer_id))
            connection.commit()
            order_id = cursor.lastrowid
            for book in cart:
                cursor.execute("INSERT INTO OrderItem (Order_ID, ISBN, Quantity) VALUES (%s, '%s', %s)" % (
                    order_id, book, cart[book]))
                connection.commit()
                cursor.execute(
                    "INSERT INTO Transaction (Order_ID, Transaction_Date, Payment_Method) VALUES (%s, now(), 'Cash')" % (order_id))
                cursor.execute("UPDATE Book SET Quantity = Quantity - %s WHERE ISBN = %s" % (
                    quantity, isbn))
                connection.commit()
                books.append(
                    (isbn, book[1], book[2], book[3], book[4], book[5], quantity))
            print("Order placed successfully")

        elif choice == "5":
            # Exit
            break

        else:
            print("Invalid choice")


def admin_menu():
    # Admin menu
    while True:
        print("What would you like to do?")
        print("1. Show all books")
        print("2. Add a book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Show all books
            cursor.execute("SELECT * FROM Book")
            books = cursor.fetchall()
            tableprint(books)

        elif choice == "2":
            # Add a book
            isbn = input("Enter the ISBN of the book: ")
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publisher = input("Enter the publisher of the book: ")
            publication_date = input(
                "Enter the publication date of the book: ")
            price = input("Enter the price of the book: ")
            quantity = input("Enter the quantity of the book: ")

            cursor.execute("INSERT INTO Book (ISBN, Title, Author, Publisher, Publication_Date, Price, Quantity) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                isbn, title, author, publisher, publication_date, price, quantity))
            connection.commit()
            print("Book added successfully")

        elif choice == "3":
            # Update a book
            isbn = input("Enter the ISBN of the book: ")
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            publisher = input("Enter the publisher of the book: ")
            publication_date = input(
                "Enter the publication date of the book: ")
            price = input("Enter the price of the book: ")
            quantity = input("Enter the quantity of the book: ")

            cursor.execute("UPDATE Book SET Title='%s', Author='%s', Publisher='%s', Publication_Date='%s', Price='%s', Quantity='%s' WHERE ISBN='%s'" % (
                title, author, publisher, publication_date, price, quantity, isbn))
            connection.commit()
            print("Book updated successfully")

        elif choice == "4":
            # Delete a book
            isbn = input("Enter the ISBN of the book: ")

            cursor.execute("DELETE FROM Book WHERE ISBN='%s'" % isbn)
            connection.commit()
            print("Book deleted successfully")

        elif choice == "5":
            # Exit
            break

        else:
            print("Invalid choice")


def menu():
    # Main menu
    while True:
        print("What would you like to login as?")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Customer
            customer_menu()

        elif choice == "2":
            # Admin
            admin_menu()

        elif choice == "3":
            # Exit
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bookstore"
    )

    # Create a cursor object
    cursor = connection.cursor()
    cart = {}

    # Display the main menu
    menu()

    # Close the cursor and connection
    cursor.close()
    connection.close()
