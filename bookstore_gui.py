from tkinter import messagebox, ttk
import mysql.connector
import tkinter as tk


def show_all_books(table):
    # Show all books
    cursor.execute("SELECT * FROM Book")
    books = cursor.fetchall()
    table.delete(*table.get_children())
    for book in books:
        table.insert("", tk.END, values=book)


def gui_admin_menu():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Admin Bookstore Management System")

    # Create a frame to hold the table
    table_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create a table to display the books
    table = ttk.Treeview(table_frame, columns=(
        "ISBN", "Title", "Author", "Publisher", "Publication Date", "Price", "Quantity"), show="headings")

    # Add the columns to the table with a delete column
    table.heading("ISBN", text="ISBN")
    table.heading("Title", text="Title")
    table.heading("Author", text="Author")
    table.heading("Publisher", text="Publisher")
    table.heading("Publication Date", text="Publication Date")
    table.heading("Price", text="Price")
    table.heading("Quantity", text="Quantity")

    # Create a scrollbar for the table
    table_scrollbar = tk.Scrollbar(
        table_frame, orient="vertical", command=table.yview)

    # Configure the table to use the scrollbar
    table.configure(yscrollcommand=table_scrollbar.set)

    # Create a button to add a book
    add_button = tk.Button(button_frame, text="Add",
                           command=lambda: add_book(table))

    # Create a button to edit a book
    edit_button = tk.Button(button_frame, text="Edit",
                            command=lambda: update_book(table))

    # Create a button to delete a book
    delete_button = tk.Button(
        button_frame, text="Delete", command=lambda: delete_book(table))

    # Create a button to view orders
    view_orders_button = tk.Button(
        button_frame, text="View Orders", command=lambda: view_orders())

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the table and buttons
    table_frame.pack()
    button_frame.pack()
    table.pack(side="left")
    table_scrollbar.pack(side="right", fill="y")
    add_button.pack(side="left")
    edit_button.pack(side="left")
    delete_button.pack(side="left")
    view_orders_button.pack(side="left")
    exit_button.pack(side="left")

    # Display the table
    show_all_books(table)

    # Bind the double click event to the table
    table.bind("<Double-1>", lambda event: update_book(table))

    # Start the main loop
    window.mainloop()


def add_book(table):
    # Create a new window
    window = tk.Toplevel()

    # Create a frame to hold the labels and entries
    entry_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create labels and entries for the book details
    isbn_label = tk.Label(entry_frame, text="ISBN")
    isbn_entry = tk.Entry(entry_frame)
    title_label = tk.Label(entry_frame, text="Title")
    title_entry = tk.Entry(entry_frame)
    author_label = tk.Label(entry_frame, text="Author")
    author_entry = tk.Entry(entry_frame)
    publisher_label = tk.Label(entry_frame, text="Publisher")
    publisher_entry = tk.Entry(entry_frame)
    publication_date_label = tk.Label(entry_frame, text="Publication Date")
    publication_date_entry = tk.Entry(entry_frame)
    price_label = tk.Label(entry_frame, text="Price")
    price_entry = tk.Entry(entry_frame)
    quantity_label = tk.Label(entry_frame, text="Quantity")
    quantity_entry = tk.Entry(entry_frame)

    # Create a button to add the book
    add_button = tk.Button(button_frame, text="Add", command=lambda: add_book_to_database(
        table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window))

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the labels and entries
    entry_frame.pack()
    button_frame.pack()
    isbn_label.grid(row=0, column=0)
    isbn_entry.grid(row=0, column=1)
    title_label.grid(row=1, column=0)
    title_entry.grid(row=1, column=1)
    author_label.grid(row=2, column=0)
    author_entry.grid(row=2, column=1)
    publisher_label.grid(row=3, column=0)
    publisher_entry.grid(row=3, column=1)
    publication_date_label.grid(row=4, column=0)
    publication_date_entry.grid(row=4, column=1)
    price_label.grid(row=5, column=0)
    price_entry.grid(row=5, column=1)
    quantity_label.grid(row=6, column=0)
    quantity_entry.grid(row=6, column=1)
    add_button.pack(side="left")
    exit_button.pack(side="left")

    # Start the main loop
    window.mainloop()


def add_book_to_database(table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window):
    # Get the book details from the entries
    isbn = isbn_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    publisher = publisher_entry.get()
    publication_date = publication_date_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    # Check if the book already exists
    if isbn in cart:
        messagebox.showerror("Error", "Book already exists")
    else:
        # Add the book to the database
        cursor.execute(
            "INSERT INTO Book (isbn, title, author, publisher, publication_date, price, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)", (isbn, title, author, publisher, publication_date, price, quantity))

        # Commit the changes
        connection.commit()

        # Update the table
        show_all_books(table)

        # Close the window
        window.destroy()


def delete_book(table):
    # Get the selected book
    selected_book = table.focus()

    # Get the values of the selected book
    values = table.item(selected_book, "values")

    # Delete the book from the database
    cursor.execute("DELETE FROM Book WHERE isbn = %s", (values[0],))

    # Commit the changes
    connection.commit()

    # Update the table
    show_all_books(table)


def update_book(table):
    # Create a new window
    window = tk.Toplevel()

    # Create a frame to hold the labels and entries
    entry_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Get the selected book
    selected_book = table.focus()

    # Get the values of the selected book
    values = table.item(selected_book, "values")

    # Create labels and entries for the book details
    isbn_label = tk.Label(entry_frame, text="ISBN")
    isbn_entry = tk.Entry(entry_frame)
    isbn_entry.insert(0, values[0])
    title_label = tk.Label(entry_frame, text="Title")
    title_entry = tk.Entry(entry_frame)
    title_entry.insert(0, values[1])
    author_label = tk.Label(entry_frame, text="Author")
    author_entry = tk.Entry(entry_frame)
    author_entry.insert(0, values[2])
    publisher_label = tk.Label(entry_frame, text="Publisher")
    publisher_entry = tk.Entry(entry_frame)
    publisher_entry.insert(0, values[3])
    publication_date_label = tk.Label(entry_frame, text="Publication Date")
    publication_date_entry = tk.Entry(entry_frame)
    publication_date_entry.insert(0, values[4])
    price_label = tk.Label(entry_frame, text="Price")
    price_entry = tk.Entry(entry_frame)
    price_entry.insert(0, values[5])
    quantity_label = tk.Label(entry_frame, text="Quantity")
    quantity_entry = tk.Entry(entry_frame)
    quantity_entry.insert(0, values[6])

    # Create a button to update the book
    update_button = tk.Button(button_frame, text="Update", command=lambda: update_book_in_database(
        table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window))

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the labels and entries
    entry_frame.pack()
    button_frame.pack()
    isbn_label.grid(row=0, column=0)
    isbn_entry.grid(row=0, column=1)
    title_label.grid(row=1, column=0)
    title_entry.grid(row=1, column=1)
    author_label.grid(row=2, column=0)
    author_entry.grid(row=2, column=1)
    publisher_label.grid(row=3, column=0)
    publisher_entry.grid(row=3, column=1)
    publication_date_label.grid(row=4, column=0)
    publication_date_entry.grid(row=4, column=1)
    price_label.grid(row=5, column=0)
    price_entry.grid(row=5, column=1)
    quantity_label.grid(row=6, column=0)
    quantity_entry.grid(row=6, column=1)
    update_button.pack(side="left")
    exit_button.pack(side="left")

    # Start the main loop
    window.mainloop()


def update_book_in_database(table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window):
    # Get the book details from the entries
    isbn = isbn_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    publisher = publisher_entry.get()
    publication_date = publication_date_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    # Update the book in the database
    cursor.execute("UPDATE Book SET title = %s, author = %s, publisher = %s, publication_date = %s, price = %s, quantity = %s WHERE isbn = %s",
                   (title, author, publisher, publication_date, price, quantity, isbn))

    # Commit the changes
    connection.commit()

    # Update the table
    show_all_books(table)

    # Close the window
    window.destroy()


def view_orders():
    """Display all orders in the database."""
    # Create a new window
    window = tk.Toplevel()

    # Create a frame to hold the table
    table_frame = tk.Frame(window)

    # Create a table to display the orders
    table = ttk.Treeview(table_frame, columns=(
        "Order ID", "Customer ID", "Customer Email", "Order Date", "Books Ordered (ISBN)", "Quantities", "Prices", "Total Price", "Transaction ID", "Payment Method"))

    # Add the columns to the table
    table.heading("Order ID", text="Order ID")
    table.heading("Customer ID", text="Customer ID")
    table.heading("Customer Email", text="Customer Email")
    table.heading("Order Date", text="Order Date")
    table.heading("Books Ordered (ISBN)", text="Books Ordered")
    table.heading("Quantities", text="Quantities")
    table.heading("Prices", text="Prices")
    table.heading("Total Price", text="Total Price")
    table.heading("Transaction ID", text="Transaction ID")
    table.heading("Payment Method", text="Payment Method")

    # Create a scrollbar for the table
    table_scrollbar = tk.Scrollbar(
        table_frame, orient="vertical", command=table.yview)

    # Display the table
    table_frame.pack()
    table_scrollbar.pack(side="right", fill="y")
    table.pack()
    table.configure(yscrollcommand=table_scrollbar.set)

    # Display the orders
    show_all_orders(table)

    # Start the main loop
    window.mainloop()


def show_all_orders(table):
    """Display all orders in the database."""
    # Delete all rows in the table
    table.delete(*table.get_children())

    # Get all orders along with order items and transaction details from the database
    cursor.execute("SELECT o.Order_ID, o.Customer_ID, c.Email as Customer_Email, o.Order_Date, oi.ISBN AS Books_Ordered, oi.Quantity, oi.Price, t.Total_Price, t.Transaction_ID, t.Payment_Method FROM `Order` o JOIN Transaction t ON o.Order_ID = t.Order_ID JOIN Order_Item oi ON o.Order_ID = oi.Order_ID JOIN Customer c ON o.Customer_ID = c.Customer_ID ORDER BY o.Order_ID;")

    # Display the orders
    prev_order_id = 0
    for (order_id, customer_id, customer_email, order_date, books_ordered, quantities, prices, total_price, transaction_id, payment_method) in cursor:
        if order_id != prev_order_id:
            table.insert("", "end", values=(
                order_id, customer_id, customer_email, order_date, books_ordered, quantities, prices, total_price, transaction_id, payment_method))
        else:
            table.insert("", "end", values=(
                "", "", "", "", books_ordered, quantities, prices, "", "", ""))
        prev_order_id = order_id


def gui_customer_menu():
    """Display the customer menu."""
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Bookstore")

    # Create a frame to hold the table
    table_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create a table to display the books
    table = ttk.Treeview(table_frame, columns=(
        "ISBN", "Title", "Author", "Publisher", "Publication Date", "Price", "Quantity"), show="headings")

    # Add the columns to the table
    table.heading("ISBN", text="ISBN")
    table.heading("Title", text="Title")
    table.heading("Author", text="Author")
    table.heading("Publisher", text="Publisher")
    table.heading("Publication Date", text="Publication Date")
    table.heading("Price", text="Price")
    table.heading("Quantity", text="Quantity")

    # Create a scrollbar for the table
    table_scrollbar = tk.Scrollbar(
        table_frame, orient="vertical", command=table.yview)

    # Configure the table to use the scrollbar
    table.configure(yscrollcommand=table_scrollbar.set)

    # Display the table and scrollbar
    table_frame.pack()
    table.pack(side="left")
    table_scrollbar.pack(side="right", fill="y")

    # Create a button to search for a book
    search_button = tk.Button(
        button_frame, text="Search", command=lambda: gui_search_book(table))

    # Create a button to add a book to the cart
    add_to_cart_button = tk.Button(
        button_frame, text="Add to Cart", command=lambda: gui_add_to_cart(table))

    # Create a button to view the cart
    view_cart_button = tk.Button(
        button_frame, text="View Cart", command=gui_view_cart)

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the buttons
    button_frame.pack()
    search_button.pack(side="left")
    add_to_cart_button.pack(side="left")
    view_cart_button.pack(side="left")
    exit_button.pack(side="left")

    # Display the books in the table
    show_all_books(table)

    # Start the main loop
    window.mainloop()


def gui_search_book(table):
    """Display a window to search for a book."""
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Search Books")

    # Create a frame to hold the labels and entries
    entry_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create labels and entries for the search criteria
    isbn_label = tk.Label(entry_frame, text="ISBN")
    isbn_entry = tk.Entry(entry_frame)
    title_label = tk.Label(entry_frame, text="Title")
    title_entry = tk.Entry(entry_frame)
    author_label = tk.Label(entry_frame, text="Author")
    author_entry = tk.Entry(entry_frame)
    publisher_label = tk.Label(entry_frame, text="Publisher")
    publisher_entry = tk.Entry(entry_frame)
    publication_date_label = tk.Label(entry_frame, text="Publication Date")
    publication_date_entry = tk.Entry(entry_frame)
    price_label = tk.Label(entry_frame, text="Price")
    price_entry = tk.Entry(entry_frame)
    quantity_label = tk.Label(entry_frame, text="Quantity")
    quantity_entry = tk.Entry(entry_frame)

    # Create a button to search for the book
    search_button = tk.Button(button_frame, text="Search", command=lambda: search_book(
        table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window))

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the labels and entries
    entry_frame.pack()
    button_frame.pack()
    isbn_label.grid(row=0, column=0)
    isbn_entry.grid(row=0, column=1)
    title_label.grid(row=1, column=0)
    title_entry.grid(row=1, column=1)
    author_label.grid(row=2, column=0)
    author_entry.grid(row=2, column=1)
    publisher_label.grid(row=3, column=0)
    publisher_entry.grid(row=3, column=1)
    publication_date_label.grid(row=4, column=0)
    publication_date_entry.grid(row=4, column=1)
    price_label.grid(row=5, column=0)
    price_entry.grid(row=5, column=1)
    quantity_label.grid(row=6, column=0)
    quantity_entry.grid(row=6, column=1)

    # Display the buttons
    search_button.pack(side="left")
    exit_button.pack(side="left")

    # Start the main loop
    window.mainloop()


def search_book(table, isbn_entry, title_entry, author_entry, publisher_entry, publication_date_entry, price_entry, quantity_entry, window):
    """Search for a book."""
    # Clear the table
    table.delete(*table.get_children())

    # Get the search criteria
    isbn = isbn_entry.get()
    title = title_entry.get()
    author = author_entry.get()
    publisher = publisher_entry.get()
    publication_date = publication_date_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    # Create a query
    query = "SELECT * FROM Book WHERE isbn LIKE %s AND title LIKE %s AND author LIKE %s AND publisher LIKE %s AND publication_date LIKE %s AND price LIKE %s AND quantity LIKE %s"
    isbn = "%" + isbn + "%"
    title = "%" + title + "%"
    author = "%" + author + "%"
    publisher = "%" + publisher + "%"
    publication_date = "%" + publication_date + "%"
    price = "%" + price + "%"
    quantity = "%" + quantity + "%"
    values = (isbn, title, author, publisher,
              publication_date, price, quantity)

    # Execute the query
    cursor.execute(query, values)

    # Get the results
    results = cursor.fetchall()

    # Display the results
    for result in results:
        table.insert("", "end", values=result)

    # Close the window
    window.destroy()


def gui_add_to_cart(table):
    """Add a book to the cart."""
    # Get the selected book
    selected = table.focus()
    book = table.item(selected, "values")

    # Get the ISBN and stock
    isbn = book[0]
    stock = int(book[6])

    # Check if the book is already in the cart
    if isbn not in cart and stock:
        # Add the book to the cart
        cart[isbn] = 1
    elif isbn in cart and stock >= cart[isbn]:
        # Get the quantity
        quantity = cart[isbn]

        # Increment the quantity
        quantity += 1

        # Update the quantity
        cart[isbn] = quantity


def gui_view_cart():
    """Display the cart."""
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Shopping Cart")

    # Create a frame to hold the table
    table_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create a treeview to display the cart
    table = ttk.Treeview(table_frame, columns=(
        "ISBN", "Title", "Author", "Publisher", "Publication Date", "Price", "Quantity"))

    # Create a scrollbar
    scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=table.yview)

    # Configure the treeview
    table.configure(yscrollcommand=scrollbar.set)
    table.heading("#0", text="", anchor="w")
    table.heading("ISBN", text="ISBN", anchor="w")
    table.heading("Title", text="Title", anchor="w")
    table.heading("Author", text="Author", anchor="w")
    table.heading("Publisher", text="Publisher", anchor="w")
    table.heading("Publication Date", text="Publication Date", anchor="w")
    table.heading("Price", text="Price", anchor="w")
    table.heading("Quantity", text="Quantity", anchor="w")

    # Create a button to checkout
    checkout_button = tk.Button(
        button_frame, text="Checkout", command=gui_checkout)

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the table and scrollbar
    table_frame.pack()
    table.pack(side="left")
    scrollbar.pack(side="left", fill="y")

    # Display the buttons
    button_frame.pack()
    checkout_button.pack(side="left")
    exit_button.pack(side="left")

    # Display the books in the cart
    show_cart(table)

    # Start the main loop
    window.mainloop()


def show_cart(table):
    """Display the books in the cart."""
    # Clear the table
    table.delete(*table.get_children())

    # Display the books in the cart
    for isbn in cart:
        # Get the book
        book = get_book(isbn)

        # Display the book
        table.insert("", "end", values=book)


def get_book(isbn):
    """Get a book from the database."""
    # Create a query
    query = "SELECT * FROM Book WHERE isbn = %s"
    values = (isbn,)

    # Execute the query
    cursor.execute(query, values)

    # Get the result
    book = cursor.fetchone()

    # Replace the quantity
    book = book[:6] + (cart[isbn],)

    # Return the book
    return book


def gui_checkout():
    """Checkout the books in the cart."""
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Checkout")

    # Create a frame to hold the labels and entries
    entry_frame = tk.Frame(window)

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create a label and entry for the customer name
    customer_name_label = tk.Label(entry_frame, text="Customer Name:")
    customer_name_entry = tk.Entry(entry_frame)

    # Create a label and entry for the customer email
    customer_email_label = tk.Label(entry_frame, text="Customer Email:")
    customer_email_entry = tk.Entry(entry_frame)

    # Create a label and entry for the customer address
    customer_address_label = tk.Label(entry_frame, text="Customer Address:")
    customer_address_entry = tk.Entry(entry_frame)

    # Create a label and entry for the customer phone number
    customer_phone_number_label = tk.Label(
        entry_frame, text="Customer Phone Number:")
    customer_phone_number_entry = tk.Entry(entry_frame)

    # Create a label and entry for the payment method Radio Buttons (Cash or Credit card)
    payment_method_label = tk.Label(entry_frame, text="Payment Method:")
    payment_method = tk.StringVar()
    payment_method.set("Cash")
    cash_button = tk.Radiobutton(
        entry_frame, text="Cash", variable=payment_method, value="Cash")
    credit_card_button = tk.Radiobutton(
        entry_frame, text="Credit Card", variable=payment_method, value="Credit Card")

    # Create a button to checkout
    checkout_button = tk.Button(button_frame, text="Checkout", command=lambda: checkout(
        customer_name_entry, customer_email_entry, customer_address_entry, customer_phone_number_entry, payment_method))

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the labels and entries
    entry_frame.pack()
    customer_name_label.grid(row=0, column=0, sticky="e")
    customer_name_entry.grid(row=0, column=1)
    customer_email_label.grid(row=1, column=0, sticky="e")
    customer_email_entry.grid(row=1, column=1)
    customer_address_label.grid(row=2, column=0, sticky="e")
    customer_address_entry.grid(row=2, column=1)
    customer_phone_number_label.grid(row=3, column=0, sticky="e")
    customer_phone_number_entry.grid(row=3, column=1)
    payment_method_label.grid(row=4, column=0, sticky="e")
    cash_button.grid(row=4, column=1, sticky="w")
    credit_card_button.grid(row=4, column=2, sticky="w")

    # Display the buttons
    button_frame.pack()
    checkout_button.pack(side="left")
    exit_button.pack(side="left")

    # Start the main loop
    window.mainloop()


def checkout(customer_name_entry, customer_email_entry, customer_address_entry, customer_phone_number_entry, payment_method):
    """Checkout the books in the cart."""
    # Get the customer name, address, and phone number
    customer_name = customer_name_entry.get()
    customer_email = customer_email_entry.get()
    customer_address = customer_address_entry.get()
    customer_phone_number = customer_phone_number_entry.get()

    # Get the payment method
    payment_method = payment_method.get()

    # Get the books in the cart
    books = cart.items()

    # Create a query to insert the customer
    query = "INSERT INTO Customer (Name, Email, Phone, Address) VALUES (%s, %s, %s, %s)"
    values = (customer_name, customer_email,
              customer_phone_number, customer_address)

    # Execute the query
    cursor.execute(query, values)

    # Get the customer ID
    customer_id = cursor.lastrowid

    # Create a query to insert the order
    query = "INSERT INTO `Order` (Customer_ID, Order_Date) VALUES (%s, now())"
    values = (customer_id)

    # Execute the query
    cursor.execute(query, values)

    # Get the order ID
    order_id = cursor.lastrowid

    # Create a query to insert the transaction
    query = "INSERT INTO Transaction (Order_ID, Total_Price, Payment_Method) VALUES (%s, %s, %s)"
    values = (order_id, cart.total_price(), payment_method)

    # Execute the query
    cursor.execute(query, values)

    # Create a query to insert the order items
    query = "INSERT INTO Order_Item (Order_ID, ISBN, Quantity, Price) VALUES (%s, %s, %s, %s)"
    values = []

    # Loop through the books in the cart
    for book in books:
        # Get the ISBN, quantity, and price
        isbn = book[0]
        quantity = book[1].quantity
        price = book[1].price

        # Add the values to the list
        values.append((order_id, isbn, quantity, price))

    # Execute the query
    cursor.executemany(query, values)

    # Commit the changes
    connection.commit()

    # Display a message
    messagebox.showinfo("Checkout", "The books have been checked out.")

    # Clear the cart
    cart.clear()


def gui_menu():
    """Display the main menu."""
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Choose Mode")

    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)

    # Create radio buttons to select either admin or customer mode
    mode = tk.StringVar()
    mode.set("Admin")
    admin_button = tk.Radiobutton(
        window, text="Admin", variable=mode, value="Admin")
    customer_button = tk.Radiobutton(
        window, text="Customer", variable=mode, value="Customer")

    # Create a button to login
    login_button = tk.Button(button_frame, text="Login",
                             command=lambda: login(mode, window))

    # Create a button to exit
    exit_button = tk.Button(button_frame, text="Exit", command=window.destroy)

    # Display the radio buttons
    admin_button.pack()
    customer_button.pack()

    # Display the buttons
    button_frame.pack()
    login_button.pack(side="left")
    exit_button.pack(side="left")

    # Start the main loop
    window.mainloop()


def login(mode, window):
    """Login to the bookstore."""
    # Get the mode
    mode = mode.get()

    # Destroy the main menu window
    window.destroy()

    # Check if the mode is admin
    if mode == "Admin":
        # Display the admin menu
        gui_admin_menu()
    else:
        # Display the customer menu
        gui_customer_menu()


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
    gui_menu()

    # Close the cursor and connection
    cursor.close()
    connection.close()
