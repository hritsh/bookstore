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
('Jane Doe', 'jane.doe@email.com', '555-234-5678', '456 Oak Ave.');

INSERT INTO `Order` (Customer_ID, Order_Date) VALUES
(1, '2023-04-15 09:30:00'),
(2, '2023-04-15 10:15:00');

INSERT INTO Transaction (Order_ID, Transaction_Date, Payment_Method) VALUES
(1, '2023-04-15 09:45:00', 'Credit Card'),
(1, '2023-04-15 09:46:00', 'Credit Card');

INSERT INTO Order_Item (Order_ID, ISBN, Quantity, Price) VALUES
(1, '123456', 2, 10.99),
(1, '234567', 1, 12.99),
(2, '234567', 1, 12.99);