class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "emp_name": self.emp_name,
            "emp_salary": self.emp_salary,
            "emp_department": self.emp_department,
        }