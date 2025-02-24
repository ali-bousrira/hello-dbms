-- Job 8
-- 1. 
CREATE DATABASE IF NOT EXISTS SomeCompany;
USE SomeCompany;

-- 2. 
CREATE TABLE IF NOT EXISTS Employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthdate DATE,
    position VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

-- 3. 
    CREATE TABLE IF NOT EXISTS Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    department_head INT,
    location VARCHAR(50),
    FOREIGN KEY (department_head) REFERENCES Employees(employee_id)
);

-- 4. 
INSERT INTO Employees (employee_id, first_name, last_name, birthdate, position, department_id) VALUES
(1, 'John', 'Doe', '1990-05-15', 'Software Engineer', 1),
(2, 'Jane', 'Smith', '1985-08-20', 'Project Manager', 2),
(3, 'Mike', 'Johnson', '1992-03-10', 'Data Analyst', 1),
(4, 'Emily', 'Brown', '1988-12-03', 'UX Designer', 1),
(5, 'Alex', 'Williams', '1995-06-28', 'Software Developer', 1),
(6, 'Sarah', 'Miller', '1987-09-18', 'HR Specialist', 3),
(7, 'Ethan', 'Clark', '1991-02-14', 'Database Administrator', 1),
(8, 'Olivia', 'Garcia', '1984-07-22', 'Marketing Manager', 2),
(9, 'Emilia', 'Clark', '1986-01-12', 'HR Manager', 3);

-- 5. 
SELECT first_name, last_name, position FROM Employees;

-- 6. 
UPDATE Employees SET position = 'Senior Software Engineer' WHERE employee_id = 1;

-- 7. 
DELETE FROM Employees WHERE employee_id = 9;

-- 8. 
SELECT e.first_name, e.last_name, d.department_name, d.location
FROM Employees e
JOIN Departments d ON e.department_id = d.department_id;

-- 9.
SELECT * FROM Employees WHERE department_id = 1; -- IT
SELECT * FROM Employees WHERE department_id = 2; -- Management
SELECT * FROM Employees WHERE department_id = 3; -- Human Resources

-- 10. 
SELECT d.department_name, e.first_name AS manager_first_name, e.last_name AS manager_last_name
FROM Departments d
JOIN Employees e ON d.department_head = e.employee_id
ORDER BY d.department_name ASC;

-- 11.
INSERT INTO Departments (department_id, department_name, department_head, location) VALUES (4, 'Marketing', 8, 'Branch Office South');
UPDATE Employees SET department_id = 4 WHERE employee_id = 8;

-- 12.
CREATE TABLE IF NOT EXISTS Projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    start_date DATE,
    end_date DATE,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);

INSERT INTO Projects (project_id, project_name, start_date, end_date, department_id) VALUES
(1, 'IT Infrastructure Upgrade', '2024-01-01', '2024-06-30', 1),
(2, 'Marketing Campaign', '2024-03-01', '2024-05-31', 4);

SELECT d.department_name, COUNT(p.project_id) AS number_of_projects
FROM Departments d
JOIN Projects p ON d.department_id = p.department_id
WHERE d.department_id IN (1,4)
GROUP BY d.department_name;


