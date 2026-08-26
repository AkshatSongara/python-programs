class Employee:

    company = "TechCorp"

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def show(self):

        print("Employee Name:", self.name)
        print("Employee salary:", self.salary)
        print("Employee Company:", self.company)        # Call by class name..
        print("Employee Company", Employee.company)     # Call by object..

e1 = Employee("Kishore", 15000)
e2 = Employee("Vinod", 20000)

e1.show()
print()

e2.show()
print()

Employee.company = "Google"

e1.show()
print()

e2.show()
print()