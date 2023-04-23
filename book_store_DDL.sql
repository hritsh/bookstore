CREATE TABLE Book (
  ISBN CHAR(13) PRIMARY KEY,
  Title VARCHAR(255) NOT NULL,
  Author VARCHAR(255) NOT NULL,
  Publisher VARCHAR(255) NOT NULL,
  Publication_Date DATE NOT NULL,
  Price DECIMAL(10, 2) NOT NULL,
  Quantity INT NOT NULL
);

CREATE TABLE Customer (
  Customer_ID INT AUTO_INCREMENT PRIMARY KEY,
  Name VARCHAR(255) NOT NULL,
  Email VARCHAR(255) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(255) NOT NULL
);

CREATE TABLE `Order` (
  Order_ID INT AUTO_INCREMENT PRIMARY KEY,
  Customer_ID INT NOT NULL,
  Order_Date DATETIME NOT NULL,
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE Transaction (
  Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
  Order_ID INT NOT NULL,
  Transaction_Date DATETIME NOT NULL,
  Payment_Method VARCHAR(255) NOT NULL,
  FOREIGN KEY (Order_ID) REFERENCES `Order`(Order_ID)
);

CREATE TABLE Order_Item (
  Order_ID INT NOT NULL,
  ISBN CHAR(13) NOT NULL,
  Quantity INT NOT NULL,
  Price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (Order_ID, ISBN),
  FOREIGN KEY (Order_ID) REFERENCES `Order`(Order_ID),
  FOREIGN KEY (ISBN) REFERENCES Book(ISBN)
);