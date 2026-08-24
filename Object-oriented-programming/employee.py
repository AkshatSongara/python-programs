class Employee:

    name = ""
    id = ""
    salary = ""
    department = ""

    def show(self):

        print("Employee name:", self.name)
        print("Employee id:", self.id)
        print("Employee salary:", self.salary)
        print("Employee department:", self.department)

e1 = Employee()
e2 = Employee()

e1.name = "Manoj"
e1.id = 101
e1.salary = 15000
e1.department = "Computer Science"

e1.show()

e2.name = "Priya"
e2.id = 102
e2.salary = 20000
e2.department = "HR"

e2.show()