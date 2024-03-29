INSERT INTO Book (ISBN, Title, Author, Publisher, Publication_Date, Price, Quantity) VALUES
('123456', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', '1925-04-10', 10.99, 50),
('234567', 'To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott', '1960-07-11', 12.99, 30),
('345678', '1984', 'George Orwell', 'Secker and Warburg', '1949-06-08', 8.99, 40),
('456789', 'The Catcher in the Rye', 'J. D. Salinger', 'Little, Brown and Company', '1951-07-16', 9.99, 20),
('567890', 'Pride and Prejudice', 'Jane Austen', 'T. Egerton, Whitehall', '1813-01-28', 7.99, 60),
('678901', 'One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Harper & Row', '1967-05-30', 11.99, 35),
('789012', 'The Hobbit', 'J. R. R. Tolkien', 'George Allen & Unwin', '1937-09-21', 13.99, 25),
('890123', 'Animal Farm', 'George Orwell', 'Secker and Warburg', '1945-08-17', 6.99, 45),
('901234', 'Brave New World', 'Aldous Huxley', 'Chatto & Windus', '1932-06-17', 8.99, 55),
('012345', 'Lord of the Flies', 'William Golding', 'Faber and Faber', '1954-09-17', 7.99, 15),
('123457', 'The Picture of Dorian Gray', 'Oscar Wilde', 'Ward, Lock, and Company', '1890-07-01', 9.99, 10),
('234568', 'The Sound and the Fury', 'William Faulkner', 'Jonathan Cape and Harrison Smith', '1929-10-07', 12.99, 30),
('345679', 'Invisible Man', 'Ralph Ellison', 'Random House', '1952-04-14', 10.99, 25),
('456790', 'The Sun Also Rises', 'Ernest Hemingway', 'Scribner', '1926-10-22', 11.99, 20),
('567901', 'Frankenstein', 'Mary Shelley', 'Lackington, Hughes, Harding, Mavor, & Jones', '1818-01-01', 7.99, 40),
('678912', 'The Adventures of Huckleberry Finn', 'Mark Twain', 'Chatto & Windus', '1884-12-10', 6.99, 50),
('789023', 'The Count of Monte Cristo', 'Alexandre Dumas', 'Pétion', '1844-01-28', 14.99, 15),
('890134', 'Don Quixote', 'Miguel de Cervantes', 'Francisco de Robles', '1605-01-16', 17.99, 10);

INSERT INTO Customer (Name, Email, Phone, Address) VALUES
('John Smith', 'john.smith@email.com', '555-123-4567', '123 Main St.'),
('Jane Doe', 'jane.doe@email.com', '555-234-5678', '456 Oak Ave.'),
('Mary Johnson', 'mary.johnson@email.com', '555-345-6789', '789 Elm St.'),
('Robert Lee', 'robert.lee@email.com', '555-456-7890', '345 Maple Ave.'),
('Lisa Chen', 'lisa.chen@email.com', '555-567-8901', '567 Pine St.'),
('David Kim', 'david.kim@email.com', '555-678-9012', '901 Oak St.'),
('Emily Wong', 'emily.wong@email.com', '555-789-0123', '234 Cherry St.'),
('James Davis', 'james.davis@email.com', '555-890-1234', '678 Walnut St.'),
('Sarah Johnson', 'sarah.johnson@email.com', '555-901-2345', '123 Pine St.'),
('John Smith', 'john.smith@email.com', '555-123-4567', '123 Main St.'),
('Jane Doe', 'jane.doe@email.com', '555-234-5678', '456 Oak Ave.'),
('Mary Johnson', 'mary.johnson@email.com', '555-345-6789', '789 Elm St.'),
('Robert Lee', 'robert.lee@email.com', '555-456-7890', '345 Maple Ave.'),
('Lisa Chen', 'lisa.chen@email.com', '555-567-8901', '567 Pine St.'),
('David Kim', 'david.kim@email.com', '555-678-9012', '901 Oak St.'),
('Emily Wong', 'emily.wong@email.com', '555-789-0123', '234 Cherry St.'),
('James Davis', 'james.davis@email.com', '555-890-1234', '678 Walnut St.'),
('Sarah Johnson', 'sarah.johnson@email.com', '555-901-2345', '123 Pine St.');

INSERT INTO `Order` (Customer_ID, Order_Date) VALUES
(1, '2023-04-15 09:30:00'),
(2, '2023-04-15 10:15:00'),
(1, '2023-04-16 11:00:00'),
(2, '2023-04-16 12:30:00'),
(3, '2023-04-16 14:00:00'),
(4, '2023-04-17 10:00:00'),
(5, '2023-04-17 11:30:00'),
(6, '2023-04-18 13:00:00'),
(7, '2023-04-18 14:45:00'),
(8, '2023-04-19 09:00:00'),
(9, '2023-04-19 11:00:00'),
(10, '2023-04-19 13:00:00'),
(1, '2023-04-20 10:00:00'),
(2, '2023-04-20 11:30:00'),
(3, '2023-04-21 14:00:00'),
(4, '2023-04-21 15:30:00'),
(5, '2023-04-22 09:00:00'),
(6, '2023-04-22 10:30:00');

INSERT INTO Transaction (Order_ID, Total_Price, Payment_Method) VALUES
(1, 34.97, 'Credit Card'),
(2, 12.99, 'Cash'),
(3, 23.98, 'Debit Card'),
(4, 21.98, 'Credit Card'),
(5, 10.99, 'Cash'),
(6, 34.23, 'Debit Card'),
(7, 12.99, 'Credit Card'),
(8, 21.98, 'Cash'),
(9, 32.97, 'Debit Card'),
(10, 10.99, 'Credit Card'),
(11, 12.99, 'Credit Card'),
(12, 34.97, 'Debit Card'),
(13, 30.97, 'Credit Card'),
(14, 40.96, 'Cash'),
(15, 12.99, 'Debit Card'),
(16, 10.98, 'Credit Card'),
(17, 14.97, 'Cash'),
(18, 9.99, 'Debit Card');

INSERT INTO Order_Item (Order_ID, ISBN, Quantity, Price) VALUES
(1, '123456', 2, 10.99),
(1, '234567', 1, 12.99),
(2, '234567', 1, 12.99),
(3, '345678', 3, 8.99),
(3, '456789', 2, 11.99),
(4, '345678', 1, 8.99),
(5, '234567', 2, 12.99),
(6, '123456', 1, 10.99),
(7, '456789', 1, 11.99),
(7, '567890', 3, 9.99),
(8, '234567', 1, 12.99),
(8, '345678', 2, 8.99),
(9, '123456', 2, 10.99),
(10, '234567', 1, 12.99),
(10, '345678', 1, 8.99),
(10, '456789', 2, 11.99),
(10, '567890', 3, 9.99);
