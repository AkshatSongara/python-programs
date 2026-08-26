class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def is_valid_salary(salary):
        return salary >= 10000

e1 = Employee("Varun", 10000)

e1.show()

print("Employee Company:", Employee.company)

Employee.change_company("Microsoft")

print("Employee Company:", Employee.company)

print(Employee.is_valid_salary(10000))
print(Employee.is_valid_salary(9000))