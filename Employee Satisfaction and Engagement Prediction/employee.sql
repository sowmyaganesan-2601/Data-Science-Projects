USE employee;
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    salary FLOAT
);
SELECT * from employee
BULK INSERT employee
FROM 'C:\Users\pc\Downloads\employee_dataset_10000.csv'
WITH (
    FIELDTERMINATOR = ',', 
    ROWTERMINATOR = '\n', 
    FIRSTROW = 2  -- Skip header row
);

ALTER TABLE employee
ADD age INT,
    department VARCHAR(50),
    education_level VARCHAR(50),
    years_at_company INT,
    work_life_balance INT,
    job_satisfaction INT,
    performance_rating INT,
    left_company BIT;
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary FLOAT,
    age INT,
    department VARCHAR(50),
    education_level VARCHAR(50),
    years_at_company INT,
    work_life_balance INT,         -- Values: 1 (Low) to 4 (Excellent)
    job_satisfaction INT,          -- Values: 1 (Low) to 4 (High)
    performance_rating INT,        -- Values: 1 (Low) to 5 (Outstanding)
    left_company BIT               -- 0 = Still with company, 1 = Left
);

Drop table employee
INSERT INTO employee (
    id, name, position, salary,
    age, department, education_level,
    years_at_company, work_life_balance,
    job_satisfaction, performance_rating, left_company
)
SELECT 
    id, name, position, salary,
    age, department, education_level,
    years_at_company, work_life_balance,
    job_satisfaction, performance_rating, left_company
FROM employee_temp;
select *  from employee_temp
dele
select * from employee
drop table employee_temp

-- Drop the existing table if it exists
DROP TABLE IF EXISTS employee;

-- Create the employee table
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    post VARCHAR(100),
    salary DECIMAL(10, 2),
    age INT,
    department VARCHAR(50),
    education_level VARCHAR(50),
    years_at_company INT,
    work_life_balance INT,
    job_satisfaction INT,
    performance_rating INT,
    left_company BIT
);

