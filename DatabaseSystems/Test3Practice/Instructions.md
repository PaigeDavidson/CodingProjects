
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