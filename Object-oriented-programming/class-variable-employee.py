class Employee:

    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

        Employee.employee_count += 1

    def show(self):

        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)
        print("Employee Company:", Employee.company)

e1 = Employee("Mahesh", 15000)
e2 = Employee("Ramesh", 20000)

e1.show()
print()

e2.show()
print()

print("Total number of employee's:", Employee.employee_count)