USE MASTER

GO

CREATE DATABASE PI_STORE

GO

-- -- Set the database to single-user mode, which forces disconnections
-- ALTER DATABASE PI_STORE SET SINGLE_USER WITH ROLLBACK IMMEDIATE; USE MASTER DROP DATABASE PI_STORE;

-- -- Drop the database
-- USE MASTER DROP DATABASE PI_STORE;

USE PI_STORE

GO

-- Create Employee table
CREATE TABLE Employee
(
    ID VARCHAR(50) PRIMARY KEY,
    Password VARCHAR(100) ,
    Role VARCHAR(50) DEFAULT 'Cashier',
    Name NVARCHAR(100) ,
    Email VARCHAR(50),
    Phone VARCHAR(50) UNIQUE,
    Address VARCHAR(50),
    Salary DECIMAL(38, 2),
    HireDate DATE DEFAULT GETDATE(),
    Status VARCHAR(50)
);

-- Create Client table
CREATE TABLE Client
(
    ID VARCHAR(50) PRIMARY KEY,
    Name NVARCHAR(50) ,
    Email VARCHAR(50),
    Phone VARCHAR(50) UNIQUE,
    Address VARCHAR(50)
);

-- Create Product table
CREATE TABLE Product
(
    ID VARCHAR(50) PRIMARY KEY,
    Name NVARCHAR(50),
    Type NVARCHAR(50),
    -- Description NVARCHAR(50),
    Stock INT DEFAULT 0,
    Price DECIMAL(38, 2),
    Status VARCHAR(50)

);

-- Create Order table
CREATE TABLE [Order]
(
    ID VARCHAR(50) PRIMARY KEY,
    ClientID VARCHAR(50) ,
    EmployeeID VARCHAR(50) ,
    OrderDate DATE DEFAULT GETDATE(),
    TotalPrice DECIMAL(38, 2) ,
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);

-- Create OrderItem table
CREATE TABLE OrderItem
(
    ID VARCHAR(50) PRIMARY KEY,
    OrderID VARCHAR(50) ,
    ProductID VARCHAR(50) ,
    Quantity INT ,
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ProductID) REFERENCES Product(ID)
);

-- Create Bill table
CREATE TABLE Bill
(
    ID VARCHAR(50) PRIMARY KEY,
    OrderID VARCHAR(50) ,
    ClientID VARCHAR(50) ,
    EmployeeID VARCHAR(50) ,
    BillDate DATE DEFAULT GETDATE(),
    TotalPrice DECIMAL(38, 2) ,
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);


-- Insert data into Employee table
INSERT INTO Employee
VALUES
    ('E001', '123456', 'admin', 'John Doe', 'joshuafields@hotmail.com' , '079123456', '1234 Elm Street', 50000.00, '2020-01-01', 'Active');

INSERT INTO Employee
VALUES
    ('admin', 'admin', 'admin', 'John Doe', 'admin@hotmail.com' , '079123123', '1234 Elm Street', 50000.00, '2020-01-01', 'Active');

SELECT *
FROM Employee