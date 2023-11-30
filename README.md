# MySQL GUI Bookstore Management System

- This project is written in Python and uses the `mysql-connector` module to connect to the MySQL database and perform queries, and the `tkinter` module to create the GUI (Graphical User Interface).

# User Requirements Covered
- Customers should be able to browse and search for books by title, author, or ISBN
- Customers should be able to add books to their cart and proceed to checkout
- The bookstore should be able to manage their inventory and update it when new books arrive
- The bookstore should be able to keep track of customer information and order history.

# Screenshots
## Summary
<img width="1100" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/5de30fd3-798d-45f5-aea8-b73e7e7f1829">
<img width="1100" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/9ce804df-0b8b-45b2-9d6f-d91219554e2f">
<img width="1100" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/33e9c8e1-ce43-4e95-a7a2-8140d1f513ed">

## ER Diagram
<img width="1137" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/11a6ad47-6724-4721-9270-ad04892a8138">

## Entity Relations
- One customer can place many orders and the customer does not have to create an order.
- An order can only be created by one customer. A customer needs to be there for an order to be created. (1-to-many relationship)
- An order can be finalized by a transaction. An order must have a transaction. A transaction is needed for an order to be completed. There needs to be an order for the transaction to take place. (1-to-1 relationship)
- An order can request for many books. An order needs to have at least one book in it. A book can be requested by many orders. A book need not be in any order. (many-to-many relationship)
- An order contains many order items. An order needs to have at least one order item. Order items can only be in one order. Order items must be in an order for it to exist. (1-to-many relationship)
- An order item contains a book in it. An order item must have a book in it. A book can be a part of an order item. A book does not have to be in an order item. (1-to-many relationship)

# More Screenshots
### Main Login Screen
<img width="257" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/d646fa3f-e7fc-4ccc-8ad0-e830cda7675a">

## Admin View

### Admin Homepage
<img width="860" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/8df8a58e-4430-43c4-b137-703ac2f858eb">

### Add Book
<img width="298" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/abfd2f70-203b-4d3a-806f-a8cdac8a8b62">

### Edit Book
<img width="343" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/6118af92-08b9-4605-8bc8-4eb0bc6afae4">

### View Placed Orders
<img width="962" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/e0d53548-f14f-4fec-8adb-31ffd3a2e145">

## Customer View

### Customer Homepage
<img width="772" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/55cfbf56-3d55-408f-bb34-ab66a6fc11fc">

### Customer Search Filter Menu
<img width="298" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/5b626ffe-3bb7-41f8-9645-459b1b8b741e">

### Filtered Search Results
<img width="752" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/2c37a726-3986-43b3-840d-f754a98764eb">

### Shopping Cart
<img width="829" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/51ba9aba-e9de-4359-a793-f8bd53ac2c08">

### Checkout
<img width="453" alt="image" src="https://github.com/hritsh/bookstore/assets/65954042/233c8771-3702-4286-806a-05345e8a95e3">

