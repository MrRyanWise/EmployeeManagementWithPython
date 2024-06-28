import mysql.connector

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="manageemp"
)

cursor = con.cursor()


# Function to check if an employee exists
def check_employee(employee_id):
    # Query to select all rows from the employees table where id matches
    sql = 'SELECT * FROM employees WHERE id=%s'

    # Making cursor buffered to make rowcount method work properly
    data = (employee_id,)

    # Executing the SQL Query
    cursor.execute(sql, data)

    # Fetch the first row to check if employee exists
    employee = cursor.fetchone()

    # If employee is found, return True, else return False
    return employee is not None


# Function to add an employee
def add_employee():
    Id = input("Enter Employee Id: ")
    if check_employee(Id):
        print("Employee already exists. Please try again.")
        return

    Name = input("Enter Employee Name: ")
    Post = input("Enter Employee Post: ")
    Salary = input("Enter Employee Salary: ")

    sql = 'INSERT INTO employees (id, name, position, salary) VALUES (%s, %s, %s, %s)'
    data = (Id, Name, Post, Salary)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Added Successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        con.rollback()


# Function to remove an employee
def remove_employee():
    Id = input("Enter Employee Id: ")
    if not check_employee(Id):
        print("Employee does not exist. Please try again.")
        return

    sql = 'DELETE FROM manageemp.employees WHERE id=%s'
    data = (Id,)
    try:
        cursor.execute(sql, data)
        con.commit()
        print("Employee Removed Successfully")
    except mysql.connector.Error as err:
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

        sql_select = 'SELECT salary FROM manageemp.employees WHERE id=%s'
        cursor.execute(sql_select, (Id,))
        current_salary = cursor.fetchone()[0]
        new_salary = current_salary + Amount

        sql_update = 'UPDATE manageemp.employees SET salary=%s WHERE id=%s'
        cursor.execute(sql_update, (new_salary, Id))
        con.commit()
        print("Employee Promoted Successfully")

    except (ValueError, mysql.connector.Error) as e:
        print(f"Error: {e}")
        con.rollback()


# Function to display all employees
def display_employees():
    try:
        sql = 'SELECT * FROM manageemp.employees'
        cursor.execute(sql)
        employees = cursor.fetchall()
        for employee in employees:
            print("------------------------------------")
            print("Employee Id : ", employee[0])
            print("Employee Name : ", employee[1])
            print("Employee Post : ", employee[2])
            print("Employee Salary : ", employee[3])
            print("------------------------------------")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def display_employees2():
    try:
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)

        rows = cursor.fetchall()

        if rows:
            # Affichage des en-têtes de colonnes
            print(f"| {'ID':^5} | {'Name':^20} | {'Position':^20} | {'Salary':^10} |")
            print("-" * 64)

            # Affichage des données de chaque ligne
            for row in rows:
                print(f"| {row[0]:^5} | {row[1]:^20} | {row[2]:^20} | {row[3]:^10} |")

            print("-" * 64)
        else:
            print("Aucune donnée trouvée dans la table 'employees'.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la connexion à MySQL: {err}")


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
            display_employees2()
        elif ch == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    menu()
