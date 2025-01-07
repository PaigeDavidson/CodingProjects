CREATE TABLE EMPLOYEE (
    Fname VARCHAR(30),
    Minit CHAR(1),
    Lname VARCHAR(30),
    Ssn CHAR(9) PRIMARY KEY,
    Bdate DATE,
    Address VARCHAR(100),
    Sex CHAR(1),
    Salary DECIMAL(10, 2),
    Super_ssn CHAR(9),
    Dno INT
);

CREATE TABLE DEPARTMENT (
    Dname VARCHAR(30),
    Dnumber INT PRIMARY KEY,
    Mgr_ssn CHAR(9),
    Mgr_start_date DATE
);

CREATE TABLE DEPT_LOCATIONS (
    Dnumber INT,
    Dlocation VARCHAR(30)
);

CREATE TABLE PROJECT (
    Pname VARCHAR(30),
    Pnumber INT PRIMARY KEY,
    Plocation VARCHAR(30),
    Dnum INT
);

CREATE TABLE WORKS_ON (
    Essn CHAR(9),
    Pno INT,
    Hours DECIMAL(5, 2)
);

CREATE TABLE DEPENDENT (
    Essn CHAR(9),
    Dependent_name VARCHAR(30),
    Sex CHAR(1),
    Bdate DATE,
    Relationship VARCHAR(20)
);

-- Step 1: Insert into DEPARTMENT
INSERT INTO DEPARTMENT (Dname, Dnumber, Mgr_ssn, Mgr_start_date) VALUES
('Research', 1, '123456789', '2000-01-01'),
('Sales', 2, '987654321', '2005-05-01'),
('Administration', 3, '555555555', '2010-07-01');

-- Step 2: Insert into EMPLOYEE
INSERT INTO EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) VALUES
('John', 'A', 'Doe', '123456789', '1965-04-12', '123 Elm St', 'M', 50000, NULL, 1),
('Jane', 'B', 'Smith', '987654321', '1949-05-23', '456 Oak St', 'F', 60000, NULL, 2),
('Alice', 'C', 'Brown', '555555555', '1980-09-12', '789 Pine St', 'F', 75000, '123456789', 3),
('Bob', 'D', 'Green', '333333333', '1992-12-05', '321 Maple St', 'M', 55000, '987654321', 1);

-- Step 3: Insert into DEPT_LOCATIONS
INSERT INTO DEPT_LOCATIONS (Dnumber, Dlocation) VALUES
(1, 'New York'),
(2, 'Chicago'),
(3, 'Los Angeles');

-- Step 4: Insert into PROJECT
INSERT INTO PROJECT (Pname, Pnumber, Plocation, Dnum) VALUES
('ProjectX', 1, 'Stafford', 1),
('ProjectY', 2, 'Houston', 2),
('ProjectZ', 3, 'Stafford', 3);

-- Step 5: Insert into WORKS_ON
INSERT INTO WORKS_ON (Essn, Pno, Hours) VALUES
('123456789', 1, 20),
('987654321', 2, 15),
('555555555', 2, 10),
('333333333', 3, 25);

-- Step 6: Insert into DEPENDENT
INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES
('123456789', 'Mary', 'F', '2000-10-10', 'Daughter'),
('987654321', 'Tom', 'M', '2003-07-15', 'Son');


ALTER TABLE EMPLOYEE
ADD FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber);

ALTER TABLE DEPARTMENT
ADD FOREIGN KEY (Mgr_ssn) REFERENCES EMPLOYEE(Ssn);

ALTER TABLE DEPT_LOCATIONS
ADD FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT(Dnumber);

ALTER TABLE PROJECT
ADD FOREIGN KEY (Dnum) REFERENCES DEPARTMENT(Dnumber);

ALTER TABLE WORKS_ON
ADD FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn),
ADD FOREIGN KEY (Pno) REFERENCES PROJECT(Pnumber);

ALTER TABLE DEPENDENT
ADD FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn);


SELECT * FROM EMPLOYEE;

SELECT * FROM DEPARTMENT;

SELECT * FROM DEPT_LOCATIONS;

SELECT * FROM PROJECT;

SELECT * FROM WORKS_ON;

SELECT * FROM DEPENDENT;

