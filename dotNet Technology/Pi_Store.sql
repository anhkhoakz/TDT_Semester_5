USE MASTER

GO

CREATE DATABASE PI_STORE

GO

-- -- Set the database to single-user mode, which forces disconnections
-- ALTER DATABASE PI_STORE SET SINGLE_USER WITH ROLLBACK IMMEDIATE;

-- -- Drop the database
-- DROP DATABASE PI_STORE;

USE PI_STORE

GO

-- Create Employee table
CREATE TABLE Employee
(
    ID NVARCHAR(5) PRIMARY KEY,
    Password NVARCHAR(100) NOT NULL,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    Phone NVARCHAR(15) NOT NULL UNIQUE,
    Address NVARCHAR(255) NOT NULL,
    Salary DECIMAL(18, 2) NOT NULL,
    HireDate DATE NOT NULL,
    Status BOOLEAN NOT NULL
);

-- Create Client table
CREATE TABLE Client
(
    ID NVARCHAR(6) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL UNIQUE,
    Phone NVARCHAR(15) NOT NULL,
    Address NVARCHAR(255) NOT NULL
);

-- Create Product table
CREATE TABLE Product
(
    ID NVARCHAR(8) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Description NVARCHAR(255),
    Price DECIMAL(18, 2) NOT NULL,
    Quantity INT NOT NULL
);

-- Create Order table
CREATE TABLE [Order]
(
    ID NVARCHAR(8) PRIMARY KEY,
    ClientID NVARCHAR(6) NOT NULL,
    EmployeeID NVARCHAR(5) NOT NULL,
    OrderDate DATE NOT NULL,
    TotalPrice DECIMAL(18, 2) NOT NULL,
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);

-- Create OrderItem table
CREATE TABLE OrderItem
(
    ID NVARCHAR(8) PRIMARY KEY ,
    OrderID NVARCHAR(8) NOT NULL,
    ProductID NVARCHAR(8) NOT NULL,
    Quantity INT NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ProductID) REFERENCES Product(ID)
);

-- Create Bill table
CREATE TABLE Bill
(
    ID NVARCHAR(8) PRIMARY KEY,
    OrderID NVARCHAR(8) NOT NULL,
    ClientID NVARCHAR(6) NOT NULL,
    EmployeeID NVARCHAR(5) NOT NULL,
    BillDate DATE NOT NULL,
    TotalPrice DECIMAL(18, 2) NOT NULL,
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);


-- Insert data into Employee table
INSERT INTO Employee
VALUES
    ('E001', '123456', 'John Doe', 'joshuafields@hotmail.com' , '1234567890', '1234 Elm Street', 50000.00, '2020-01-01');



