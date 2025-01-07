-- Create the employees table
CREATE TABLE employees (
  employee_id INT PRIMARY KEY,
  employee_name VARCHAR(255),
  supervisor_id INT
);

-- Insert sample data into the employees table
INSERT INTO employees (employee_id, employee_name, supervisor_id)
VALUES
  (1, 'Alice', NULL),
  (2, 'Bob', 1),
  (3, 'Charlie', 1),
  (4, 'David', 2),
  (5, 'Eve', 2);

-- Create the customers table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  company_name VARCHAR(255),
  sales_rep_id INT
);

-- Insert sample data into the customers table
INSERT INTO customers (customer_id, company_name, sales_rep_id)
VALUES
  (1, 'Company A', 2),
  (2, 'Company B', 1),
  (3, 'Company C', 3),
  (4, 'Company D', 2);

-- Create the orders table
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  sales_rep_id INT,
  product_name VARCHAR(255),
  order_amount DECIMAL(10, 2)
);

-- Insert sample data into the orders table
INSERT INTO orders (order_id, customer_id, sales_rep_id, product_name, order_amount)
VALUES
  (101, 1, 2, 'Product X', 1500.00),
  (102, 2, 1, 'Product Y', 750.00),
  (103, 3, 3, 'Product Z', 1200.00),
  (104, 4, 2, 'Product X', 1800.00),
  (105, 2, 1, 'Product Z', 950.00);

select * from employees;
select * from orders;
select * from customers;


