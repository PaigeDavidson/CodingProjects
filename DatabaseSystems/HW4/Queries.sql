-- 1. Show the name, age, sales and quota of the sales representative Bill Adams.
SELECT name, age, sales, quota
FROM SALESREPS 
WHERE name='Bill Adams';

-- 2. List the customer company names and product descriptions of all the products each customer/company has ordered. Arrange the output descending by the company name. Make sure there is no redundancy in the list you printed.
SELECT DISTINCT
    c.COMPANY,
    p.DESCRIPTION
FROM 
    CUSTOMERS c
JOIN 
    ORDERS o ON c.CUST_NUM = o.CUST
JOIN 
    PRODUCTS p ON o.PRODUCT = p.PRODUCT_ID
ORDER BY 
    c.COMPANY DESC;

-- 3. Show the total value of the inventory on hand (i.e., PRICE * QTY_ON_HAND ) for each product. Arrange in descending order by total value.
SELECT DESCRIPTION, PRICE * QTY_ON_HAND AS TOTAL_VALUE
FROM PRODUCTS
ORDER BY
    TOTAL_VALUE DESC;
-- 4. How many customers are there?
SELECT COUNT(*) AS TOTAL_CUSTOMERS
FROM CUSTOMERS;
-- 5. List the cities where the local offices have their targets smaller than $575,000.
SELECT CITY
FROM OFFICES
WHERE TARGET < 575000;
-- 6. What is the average age of all the sales people?
SELECT AVG(age) AS AVERAGE_AGE
FROM SALESREPS;
-- 7. List order numbers for all the orders that are over $25,000; include also the name of the salesperson who took the order and the name of the company (i.e. customer) who placed it.
SELECT ORDER_NUM, s.NAME AS SALESPERSON, c.COMPANY as COMPANY
FROM ORDERS o
    JOIN CUSTOMERS c ON o.CUST = c.CUST_NUM
    JOIN SALESREPS s ON o.REP = s.emp_num
WHERE AMOUNT > 25000;
-- 8. How many sales offices have salespeople who are over quota?
SELECT COUNT(DISTINCT rep_office) AS Num_Offices_With_Salespeople_over_quota
FROM SALESREPS
WHERE quota < sales;
-- 9. For each salesperson - show his/her name, sales and the city where he/she works. Order your list in ascending manner, using sales of individual sales representatives for the ordering.
SELECT s.name, s.sales, o.CITY
FROM SALESREPS s
JOIN OFFICES o ON s.rep_office = o.OFFICE 
ORDER BY s.sales ASC;
-- 10. List all the companies which have ordered any size widget, and the widget they ordered. Make sure you print out only unique pairs of attribute values.
SELECT DISTINCT 
    c.COMPANY, p.DESCRIPTION
FROM CUSTOMERS c
    JOIN ORDERS o ON c.CUST_NUM = o.CUST
    JOIN PRODUCTS p ON o.PRODUCT = p.PRODUCT_ID
WHERE p.DESCRIPTION LIKE 'Size % Widget';

-- 11. List the office, city, region and amount that sales are over (or under) target for each office (if sales are over the target the number needs to be positive, if under – I want to see a negative number).
SELECT OFFICE, CITY, REGION, (SALES - TARGET) AS SALES_DIFF
FROM OFFICES;
-- 12. What is the total number (i.e. quantity!) of every part that has been ordered? Note: Do not get confused – I am not asking for the total quantity of ALL parts together, but for a list of {part, quantity} pairs...
SELECT p.DESCRIPTION AS part, SUM(o.QTY) AS Quantity_Ordered
FROM ORDERS o
JOIN PRODUCTS p ON o.PRODUCT = p.PRODUCT_ID
GROUP BY p.DESCRIPTION;
-- 13. List the salespeople, the city they work in, and the name of the manager of the office (not necessarily their direct supervisor) in which they work.
SELECT s.name, o.CITY, m.name AS Manager
FROM SALESREPS s
    JOIN OFFICES o ON s.rep_office = o.OFFICE 
    JOIN SALESREPS m ON o.MGR = m.emp_num;
-- 14. List all orders showing order number, amount, customer (i.e. company) name and the customer’s credit limit, for all cases where the order was greater than $20,000.
SELECT o.ORDER_NUM, o.AMOUNT, c.COMPANY, c.CREDIT_LIMIT
FROM ORDERS o
    JOIN CUSTOMERS c ON o.CUST = c.CUST_NUM
WHERE o.AMOUNT > 20000;
-- 15. Are there any customers who are over their credit limit? If so, list the customer, the total amount the customer has on order, and the credit limit.
SELECT c.COMPANY, SUM(o.AMOUNT) AS TOTAL, c.CREDIT_LIMIT
FROM CUSTOMERS c
    JOIN ORDERS o ON c.CUST_NUM = o.CUST
GROUP BY c.COMPANY, c.CREDIT_LIMIT
HAVING SUM(o.AMOUNT > c.CREDIT_LIMIT);
-- 16. List the salespeople with a higher quota than their direct manager.
SELECT s.name
FROM SALESREPS s
    JOIN SALESREPS m ON s.manager = m.emp_num
WHERE s.quota > m.quota;
-- 17. List salespeople who work in different offices than their direct managers. Show the salesperson’s name and the city of the office, where he/she is employed.
SELECT s.name, o.CITY
FROM SALESREPS s
    JOIN OFFICES o ON s.rep_office = o.OFFICE
    JOIN SALESREPS m ON s.manager = m.emp_num
WHERE m.rep_office != s.rep_office;
-- 18. What is the total order amount for each salesperson? Order output by increasing total order amount; do not print the same names multiple times.
SELECT DISTINCT s.name, SUM(o.AMOUNT) AS TOTAL_AMOUNT
FROM SALESREPS s
    JOIN ORDERS o ON s.emp_num = o.REP
GROUP BY s.name
ORDER BY SUM(o.AMOUNT) ASC;
-- 19. List all the customers whose sales representative is an office manager. Arrange output increasing (i.e. in alphabetic order) by the company/customer name.
SELECT DISTINCT c.COMPANY
FROM CUSTOMERS c
    JOIN OFFICES o ON c.CUST_REP = o.MGR
ORDER BY c.COMPANY ASC;
-- 20. What is the total amount (i.e. value!) of orders for each salesperson whose orders total for more than $30,000? Order output by amounts, in increasing manner
SELECT DISTINCT s.name, SUM(o.AMOUNT) AS TOTAL_AMOUNT
FROM SALESREPS s
    JOIN ORDERS o ON s.emp_num = o.REP
GROUP BY s.name
HAVING SUM(o.AMOUNT) > 30000
ORDER BY SUM(o.AMOUNT) ASC;
-- 21. List the offices and the target amounts for every office where the target for the office exceeds the sum of the individual salespeople’s quotas.
SELECT o.OFFICE, o.TARGET
FROM OFFICES o
    LEFT JOIN SALESREPS s ON o.OFFICE = s.rep_office
GROUP BY o.OFFICE, o.CITY, o.TARGET
HAVING o.TARGET > SUM(s.quota);
-- 22. List the salespeople whose quotas are equal to or higher than the target of the Atlanta sales office (note: you are not allowed to just write SQL command with “office=13” explicitly, you must use word “Atlanta” somewhere in your command).
SELECT s.name
FROM SALESREPS s
    JOIN OFFICES o ON s.rep_office = o.OFFICE
WHERE s.quota >= (SELECT o.TARGET
                    FROM OFFICES o
                    WHERE o.CITY = 'Atlanta');
-- 23. List the salespeople who do not work in offices managed by Larry Fitch (note: you are not allowed to just write SQL command with “MGR!=108” explicitly, you must use full Larry’s name in your command).
SELECT s.name
FROM SALESREPS s
    JOIN OFFICES o ON s.rep_office = o.OFFICE
WHERE o.MGR != (SELECT s.emp_num
                        FROM SALESREPS s
                        WHERE s.name = 'Larry Fitch');
-- 24. List the unique identifiers of products for which a single order on amount of $25,000 or more has been received.
SELECT p.PRODUCT_ID
FROM PRODUCTS p 
    JOIN ORDERS o ON p.PRODUCT_ID = o.PRODUCT
WHERE o.AMOUNT >= 25000;
-- 25. List the names of companies who placed an order with a sales representative that is not the sales representative that usually calls on them (i.e. he/she is not specified in an appropriate record of the CUSTOMER table, as the regular sales representative for this client/company). Include also the names of these salesreps, indicating in attribute TEMPORARY_SALES_REP name of salesrep, who took the order
SELECT c.COMPANY, 
       s.name AS TEMPORARY_SALES_REP
FROM ORDERS o
    JOIN CUSTOMERS c ON o.CUST = c.CUST_NUM
    JOIN SALESREPS s ON o.REP = s.emp_num
WHERE o.REP != c.CUST_REP;

