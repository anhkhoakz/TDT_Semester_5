USE MASTER;

GO

CREATE DATABASE PI_STORE;

GO

-- -- Set the database to single-user mode, which forces disconnections
-- ALTER DATABASE PI_STORE SET SINGLE_USER WITH ROLLBACK IMMEDIATE; USE MASTER; DROP DATABASE PI_STORE;

-- -- Drop the database
-- USE MASTER; DROP DATABASE PI_STORE;

USE PI_STORE;

GO

-- Create Employee table
CREATE TABLE Employee
(
    ID VARCHAR(50) PRIMARY KEY,
    Password VARCHAR(50),
    Role VARCHAR(50) DEFAULT 'Cashier',
    Name NVARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15) UNIQUE,
    Address VARCHAR(255),
    Salary DECIMAL(18, 2),
    HireDate DATE DEFAULT GETDATE(),
    Status VARCHAR(50)
);

-- Create Client table
CREATE TABLE Client
(
    ID VARCHAR(50) PRIMARY KEY,
    Name NVARCHAR(100),
    Email VARCHAR(100),
    Phone VARCHAR(15) UNIQUE,
    Address VARCHAR(255)
);

-- Create Product table
CREATE TABLE Product
(
    ID VARCHAR(50) PRIMARY KEY,
    Name NVARCHAR(100),
    Type NVARCHAR(50),
    -- Description NVARCHAR(255),
    Stock INT DEFAULT 0,
    Price DECIMAL(18, 2),
    Status VARCHAR(50),
    Image VARCHAR(255),
    AddedDate DATE DEFAULT GETDATE()
);

-- Create Order table
CREATE TABLE [Order]
(
    ID VARCHAR(50) PRIMARY KEY,
    ClientID VARCHAR(50),
    EmployeeID VARCHAR(50),
    OrderDate DATE DEFAULT GETDATE(),
    TotalPrice DECIMAL(18, 2),
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);

-- Create OrderItem table
CREATE TABLE OrderItem
(
    ID VARCHAR(50) PRIMARY KEY,
    OrderID VARCHAR(50),
    ProductID VARCHAR(50),
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ProductID) REFERENCES Product(ID)
);

-- Create Bill table
CREATE TABLE Bill
(
    ID VARCHAR(50) PRIMARY KEY,
    OrderID VARCHAR(50),
    ClientID VARCHAR(50),
    EmployeeID VARCHAR(50),
    BillDate DATE DEFAULT GETDATE(),
    TotalPrice DECIMAL(18, 2),
    FOREIGN KEY (OrderID) REFERENCES [Order](ID),
    FOREIGN KEY (ClientID) REFERENCES Client(ID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(ID)
);

-- Insert data into Employee table
INSERT INTO Employee
VALUES
    ('E001', '123456', 'admin', 'Nancy Cain', 'joshuafields@hotmail.com', '079123456', '1234 Elm Street', 10000000, '2023-01-01', 'Active');

INSERT INTO Employee
VALUES
    ('admin', 'admin', 'admin', 'April Arellano', 'admin@hotmail.com', '079123123', '1234 Elm Street', 1000000, '2024-01-01', 'Active');

SELECT *
FROM Employee;