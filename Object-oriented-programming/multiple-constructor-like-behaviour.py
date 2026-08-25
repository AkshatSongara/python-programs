class Employee:

    def __init__(self, name = "Unknown", salary = 0, department = "Not assigned"):

        self.name = name
        self.salary = salary
        self.department = department

    def print(self):

        print("Employee name:", self.name)
        print("Employee salary:", self.salary)
        print("Employee department:", self.department)


e1 = Employee()
e2 = Employee("Kunal")
e3 = Employee("Santosh", 10000)
e4 = Employee("Ramesh", 15000, "Technical")

e1.print()
print()

e2.print()
print()

e3.print()
print()

e4.print()
print()