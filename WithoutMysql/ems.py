import pickle

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employees(self):
        print(f"\n| {'ID':^5} | {'Name':^20} | {'Salary':^20} | {'Department':^10} |")
        print("-" * 64)

        for employee in self.employees:
            print(f"| {employee.emp_id:^5} | {employee.emp_name:^20} | {employee.emp_salary:^20} | {employee.emp_department:^10} |")

        print("-" * 64)

    def update_employee(self, emp_id, new_employee_data):
        for i, employee in enumerate(self.employees):
            if employee.emp_id == emp_id:
                self.employees[i] = new_employee_data
                print("Employee updated successfully.")
                return
        print("Employee not found.")

    def delete_employee(self, emp_id):
        for i, employee in enumerate(self.employees):
            if employee.emp_id == emp_id:
                del self.employees[i]
                print("Employee deleted successfully.")
                return
        print("Employee not found.")

    def save_data(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.employees, file)

    def load_data(self, filename):
        try:
            with open(filename, "rb") as file:
                self.employees = pickle.load(file)
        except FileNotFoundError:
            self.employees = []
