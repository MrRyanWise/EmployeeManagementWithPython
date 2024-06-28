from employee import Employee
from ems import EmployeeManagementSystem


def main():
    ems = EmployeeManagementSystem()
    ems.load_data("employee_data.pkl")

    while True:
        print("\nEmployee Management System Menu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            emp_name = input("Enter Employee Name: ")
            emp_salary = float(input("Enter Employee Salary: "))
            emp_department = input("Enter Employee Department: ")

            employee = Employee(emp_id, emp_name, emp_salary, emp_department)
            ems.add_employee(employee)
            print("Employee added successfully.")

        elif choice == "2":
            ems.view_employees()

        elif choice == "3":
            emp_id = input("Enter Employee ID to update: ")
            emp_name = input("Enter New Employee Name: ")
            emp_salary = float(input("Enter New Employee Salary: "))
            emp_department = input("Enter New Employee Department: ")

            new_employee_data = Employee(emp_id, emp_name, emp_salary, emp_department)
            ems.update_employee(emp_id, new_employee_data)

        elif choice == "4":
            emp_id = input("Enter Employee ID to delete: ")
            ems.delete_employee(emp_id)

        elif choice == "5":
            ems.save_data("employee_data.pkl")
            print("Employee data saved. Exiting...")
            break


if __name__ == "__main__":
    main()