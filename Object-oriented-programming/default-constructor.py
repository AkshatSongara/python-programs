class Employee:

    def __init__(self, name = "Unknown", salary = 0):

        self.name = name
        self.salary = salary

    def show(self):

        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

e1 = Employee()
e1.show()

print()

e1 = Employee("Amit", 15000)
e1.show()