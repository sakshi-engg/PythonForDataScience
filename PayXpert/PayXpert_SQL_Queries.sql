-- Drop existing tables if any (for fresh start)
DROP TABLE IF EXISTS FinancialRecord;
DROP TABLE IF EXISTS Tax;
DROP TABLE IF EXISTS Payroll;
DROP TABLE IF EXISTS Employee;
Create database PayXpert;
Use Payxpert;
-- 1. Employee Table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    Email VARCHAR(100) UNIQUE,
    PhoneNumber VARCHAR(15),
    Address VARCHAR(255),
    Position VARCHAR(50),
    JoiningDate DATE,
    TerminationDate DATE NULL
);

-- 2. Payroll Table
CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary FLOAT,
    OvertimePay FLOAT,
    Deductions FLOAT,
    NetSalary FLOAT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- 3. Tax Table
CREATE TABLE Tax (
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    TaxYear INT,
    TaxableIncome FLOAT,
    TaxAmount FLOAT,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- 4. FinancialRecord Table
CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    RecordDate DATE,
    Description VARCHAR(255),
    Amount FLOAT,
    RecordType VARCHAR(50),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

SELECT * FROM Employee;
SELECT * FROM Payroll;
SELECT * FROM Tax;
SELECT * FROM FinancialRecord;

-- Insert into employees
INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
VALUES 
('John', 'Doe', '1985-06-15', 'Male', 'john.doe@example.com', '1234567890', '123 Elm Street', 'Software Engineer', '2020-01-10'),
('Jane', 'Smith', '1990-09-22', 'Female', 'jane.smith@example.com', '0987654321', '456 Oak Avenue', 'HR Manager', '2019-03-15');

-- Insert into payroll records
INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES 
(1, '2023-01-01', '2023-01-31', 60000, 5000, 7000, 58000),
(2, '2023-01-01', '2023-01-31', 55000, 2000, 6000, 51000);

-- Insert into tax records
INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES 
(1, 2023, 720000, 72000),
(2, 2023, 660000, 66000);

-- Insert into financial records
INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES 
(1, '2023-02-01', 'Medical Reimbursement', 3000, 'Income'),
(2, '2023-02-01', 'Laptop Purchase', 5000, 'Expense');

select * from FinancialRecord;