import pyodbc

# Database connection setup
server = 'DESKTOP-CABV4JI\\SQLEXPRESS'
database = 'employee'
driver = 'ODBC Driver 17 for SQL Server'

con = pyodbc.connect(f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')
cursor = con.cursor()

# Function to check if an employee exists
def check_employee(employee_id):
    sql = 'SELECT * FROM employee WHERE id = ?'
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None

# Function to add an employee
def add_employee():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return

    Name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")

    sql = 'INSERT INTO employee (id, name, position, salary) VALUES (?, ?, ?, ?)'
    data = (Id, Name, Post, Salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except Exception as err:
        print(f"Error: {err}")
        con.rollback()

# Function to remove an employee
def remove_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    sql = 'DELETE FROM employee WHERE id = ?'
    try:
        cursor.execute(sql, (Id,))
        con.commit()
        print("Employee Removed Successfully")
    except Exception as err:
        print(f"Error: {err}")
        con.rollback()

# Function to promote an employee
def promote_employee():
    Id = input("Enter Employee's Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    try:
        Amount = float(input("Enter increase in Salary: "))
        sql_select = 'SELECT salary FROM employee WHERE id = ?'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE employee SET salary = ? WHERE id = ?'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")

    except Exception as e:
        print(f"Error: {e}")
        con.rollback()

# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM employee'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")
    except Exception as err:
        print(f"Error: {err}")

# Function to display the menu
def menu():
    while True:
        print("\nWelcome to Employee Management Record")
        print("Press:")
        print("1 to Add Employee")
        print("2 to Remove Employee")
        print("3 to Promote Employee")
        print("4 to Display Employees")
        print("5 to Exit")

        ch = input("Enter your Choice: ")

        if ch == '1':
            add_employee()
        elif ch == '2':
            remove_employee()
        elif ch == '3':
            promote_employee()
        elif ch == '4':
            display_employees()
        elif ch == '5':
            print("Exiting the Menu. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")

if __name__ == "__main__":
    menu()


