-- 1. Retrieve all information on male employees.
SELECT *
FROM EMPLOYEE 
WHERE Sex = 'M';

-- 2. Retrieve the names and date of birth of all employees born before 1950.
SELECT Fname, Minit, Lname, Bdate
FROM  EMPLOYEE
WHERE Bdate < '1950-01-01';

-- 3. Retrieve the name and address of all employees who work for the Research department.
SELECT e.Fname, e.Minit, e.Lname, e.Address
FROM  EMPLOYEE e, DEPARTMENT d
WHERE e.Dno = d.Dnumber AND d.Dname = 'Research';

-- 4. List the names of every manager and the name and number of the department they manage.
SELECT e.Fname, e.Minit, e.Lname, d.Dname, d.Dnumber
FROM  DEPARTMENT d, EMPLOYEE e
WHERE d.Mgr_ssn = e.Ssn;

-- 5. Find the names and addresses of all workers who worked on the project with PNo 2.
SELECT e.Fname, e.Minit, e.Lname, e.Address
FROM  EMPLOYEE e, WORKS_ON w
WHERE w.Pno = '2' AND w.Essn = e.Ssn;

-- 6 .For every project located in “Stafford”, list the project number, the controlling department number, 
-- and the department's manager's last name, address, and date of birth.
SELECT Pnumber, Dnumber, Lname, Address, Bdate
FROM  PROJECT, DEPARTMENT, EMPLOYEE
WHERE Plocation = 'Stafford' AND Dnum = Dnumber AND Mgr_ssn = Ssn;

-- 7. Retrieve the names of employees with no dependents.
SELECT Fname, Minit, Lname
FROM EMPLOYEE
EXCEPT
SELECT e.Fname, e.Minit, e.Lname
FROM EMPLOYEE e
JOIN DEPENDENT d ON e.Ssn = d.Essn;

-- 8. Retrieve the names of the employees who work for the "Sales" department and the hiring dates of the 
-- department's manager (mgr_start_date), ordered by their first names in ascending order.
SELECT e.Fname, e.Minit, e.Lname, d.mgr_start_date
FROM  EMPLOYEE e, DEPARTMENT d
WHERE d.Dname = 'Sales' AND d.Dnumber = e.Dno
ORDER BY e.Fname ASC;

-- 9. Retrieve the names of all employees and the names of their department manager. 
-- Show only employees whose salary is greater than 500, and order the results by the employee's last name.
SELECT e.Fname AS Employee_FirstName, e.Minit AS Employee_MInitial, e.Lname AS Employee_LastName,
       m.Fname AS Manager_FirstName, m.Lname AS Manager_LastName
FROM  EMPLOYEE e, DEPARTMENT d, EMPLOYEE m
WHERE e.Salary > 500 AND e.Dno = d.Dnumber AND m.Ssn = d.Mgr_ssn
ORDER BY e.Lname ASC;

-- 10. Retrieve the names of employees, the projects they worked on, and the department name, 
-- but only for projects located in "Houston".
SELECT e.Fname, e.Minit, e.Lname, p.Pname, d.Dname
FROM  PROJECT p, EMPLOYEE e, WORKS_ON w, DEPARTMENT d
WHERE p.Plocation = 'Houston' AND e.Ssn = w.Essn AND w.Pno = p.Pnumber AND p.Dnum = d.Dnumber;