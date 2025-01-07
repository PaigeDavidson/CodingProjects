Main.sql output:

emp_num	name	age	rep_office	title	manager	hire_date	quota	sales
101	Dan Roberts	45	12	Sales Rep	104	1996-10-20	300000.00	305673.00
102	Sue Smith	48	21	Sales Rep	108	1996-12-10	350000.00	474050.00
103	Paul Cruz	29	12	Sales Rep	104	1997-03-01	275000.00	286775.00
104	Bob Smith	33	12	Sales Mrg	106	1997-05-19	200000.00	142594.00
105	Bill Adams	37	13	Sales Rep	104	1996-02-12	350000.00	367911.00
106	Sam Clark	52	11	Vp Sales	NULL	1998-06-14	275000.00	299912.00
107	Nancy Angelli	49	22	Sales Rep	108	1998-11-14	300000.00	186042.00
108	Larry Fitch	62	21	Sales Mrg	106	1999-10-12	350000.00	361865.00
109	Mary Jones	31	11	Sales Rep	106	1999-10-12	300000.00	392725.00
110	Tom Snyder	41	NULL	Sales Rep	101	2000-01-13	NULL	75985.00

[Execution complete with exit code 0]

The CUSTOMER table stores data about each customer, such as the company name, credit limit, and

the salesperson who usually calls on the customer (i.e. the customer representative).

The SALESREP table stores the employee number, his/her name, age, direct supervisor (denoted as manager), year-to-date sales and other data about each salesperson.

Note: Managers included in SALESREP table are direct supervisors of sales representatives - not all of them are/must be office manager
The OFFICE table stores data about each of the five sales offices including the city where the office is located, the sales region to which it belongs, the office’s manager ID (denoted as MGR), and so on.

The ORDER table keeps track of every order placed by a customer, identifying the salesperson who took the order (not necessarily the salesperson who calls on the customer), the product ordered, the ordered quantity, and the total value (i.e. amount) of the order (in USD), and so on. For simplicity, each order is for only one product.

The PRODUCT table stores data about each product available for sale, such as the manufacturer, product number, description, and price.

*****************TABLES ***********************

mysql> SELECT * FROM SALESREPS;
+---------+---------------+------+------------+-----------+---------+------------+-----------+-----------+
| emp_num | name          | age  | rep_office | title     | manager | hire_date  | quota     | sales     |
+---------+---------------+------+------------+-----------+---------+------------+-----------+-----------+
| 101           | Dan Roberts|  45 | 12             |Sales Rep| 104     | 1996-10-20 | 300000.00 | 305673.00 |

mysql> SELECT * FROM OFFICES;
+--------+-------------+---------+------+-----------+-----------+
| OFFICE | CITY        | REGION  | MGR  | TARGET    | SALES     |
+--------+-------------+---------+------+-----------+-----------+
| 11           | New York | Eastern     | 106     | 575000.00   | 692637.00 |

mysql> SELECT * FROM CUSTOMERS;
+----------+-------------------+----------+--------------+
| CUST_NUM | COMPANY           | CUST_REP | CREDIT_LIMIT |
+----------+-------------------+----------+--------------+
| 2101               | Jones Mfg.             | 106             |     65000.00 |

mysql> mysql> SELECT * FROM ORDERS;
+-----------+------------+------+------+------+---------+------+----------+
| ORDER_NUM | ORDER_DATA | CUST | REP  | MFR  | PRODUCT | QTY  | AMOUNT   |
+-----------+------------+------+------+------+---------+------+----------+
| 113012              | 2000-01-11        | 2111    | 105    | ACI   | 41003          |   35    |  3745.00 |

mysql> SELECT * FROM PRODUCTS;
+--------+------------+-----------------+---------+-------------+
| MFR_ID | PRODUCT_ID | DESCRIPTION     | PRICE   | QTY_ON_HAND |
+--------+------------+-----------------+---------+-------------+
| ACI        | 41002                 | Size 2 Widget   |   76.00        |         167 |


****** Notes ******~

Command to get into the database and be able to run commands:
    *  mysql -u root -p hw3
    * to exit: just type "exit"
    * I didn't initalize a password for this one so you can just press enter on the passwords

Command to run a queries file on a database and send the output to a txt file:
    * mysql -u root -p hw3 --batch --raw < Queries.sql > output.txt
    * This command runs the queries in Queries.txt on the hw3 database and creates a file (Output.txt) to send the output to

Command to run a .sql query file on a database and output the results to the terminal
    * mysql -u root -p hw3 < Queries.sql
    * Where hw3 is the database and Queries.sql is the file with my queries in it

Starting and stopping sql:
    * to start: brew services start mysql
    * to check the services that are running: brew services list
    * to stop: brew services stop mysql

Creating a database
    * You can just create one with a couple of steps:
        * get into the sql moniter with commandL: mysql -u root
        * then run command: CREATE DATABASE <databaseName>;
        * check that is was added to your databases by running command: SHOW databases;
    * Then to build the database with something like the EmployeeDB.sql file:
        * enter command "exit" to leave the sql moniter
        * from directory with the initializing .sql file run the command: mysql -u root -p <databaseName> <InitializeFileNamee.sql>
        * if this doesnt work, try this: 
            Ensure you are logged into MySQL: Log into your MySQL instance using the command:

            mysql -u your_user -p
            Switch to the hw4 database: Select the hw4 database using:

            USE hw4;

            Execute the main.sql file: Use the SOURCE command to execute the SQL file and populate your database. Assuming the main.sql file is in your current working directory:

            SOURCE main.sql;

            Verify the data: After the script runs, confirm the tables and data were created successfully:

            Check the tables:
            SHOW TABLES;
            Verify the data in each table, e.g., for the CUSTOMERS table:
            SELECT * FROM CUSTOMERS;