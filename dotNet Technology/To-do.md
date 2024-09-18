### **Pi Store Management System - To Do List**

#### **Environment Setup**

1. **Install Visual Studio**

    - Download and install Visual Studio.
    - Install the required C# .NET packages for Windows Forms development.

2. **Set Up SQL Server**
    - Install SQL Server or use an online service.
    - Create a new database for the Pi Store.

---

#### **Database Design**

3. **Create Database Schema**

    - Create the following tables in SQL Server:
        - **Employee** (ID, Name, Email, Phone, Address, Salary, HireDate)
        - **Client** (ID, Name, Email, Phone, Address)
        - **Product** (ID, Name, Description, Price, Quantity)
        - **Order** (ID, ClientID, EmployeeID, OrderDate, TotalPrice)
        - **OrderItem** (ID, OrderID, ProductID, Quantity)
        - **Bill** (ID, OrderID, ClientID, EmployeeID, BillDate, TotalPrice)

4. **Design ER Diagram (Optional)**
    - Visualize the database relations between the tables.

---

#### **Windows Forms Development**

5. **Create Login Form**

    - Design a simple form with Username and Password fields.
    - Implement SQL authentication logic to validate the user.

6. **Create Main Menu Form**
    - Create a form with a menu that links to:
        - Employee Management
        - Client Management
        - Product Management
        - Order Placement
        - Order Management
        - Bill Generation

---

#### **CRUD Functionality (Core Features)**

7. **Employee Management**

    - **To Do:**
        - Create a form to view, add, edit, and delete employees.
        - Implement SQL queries for each operation.

8. **Client Management**

    - **To Do:**
        - Create a form to view, add, edit, and delete clients.
        - Implement SQL queries for each operation.

9. **Product Management**

    - **To Do:**
        - Create a form to view, add, edit, and delete products.
        - Ensure product IDs are unique.
        - Implement SQL queries for each operation.

10. **Order Placement**

    - **To Do:**
        - Design a form to place an order by selecting a client and adding products.
        - Deduct the product quantity from the inventory when the order is placed.
        - Update the `Order` and `OrderItem` tables.

11. **Order Management**

    - **To Do:**
        - Create a form to view and manage orders, including their details and products.
        - Implement SQL queries to fetch and update order details.

12. **Bill Generation**
    - **To Do:**
        - Create a form to generate a bill by selecting an order.
        - Calculate the total price and insert the bill data into the `Bill` table.

---

#### **Additional Features**

13. **Input Validation and Error Handling**
    -   Add validation to forms (e.g., required fields, correct formats).
    -   Implement error messages for invalid input.

---

#### **Optional Features (Extra Credit)**

14. **Search Functionality**

    -   Add search functionality to search for employees, clients, products, orders, or bills by name, ID, or date range.

15. **Export to CSV**

    -   Implement functionality to export table data to CSV files.

16. **Charts and Graphs**
    -   Add a feature to visualize data (e.g., sales trends or employee performance) using charts.

---

#### **Final Steps**

17. **Test Application**

    -   Thoroughly test all forms and functionalities.
    -   Ensure proper input validation and error handling.

18. **Prepare for Submission**
    -   Clean up the code and ensure proper commenting.
    -   Submit the source code and database schema.

---
