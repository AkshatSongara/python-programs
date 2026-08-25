class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    def show(self):

        print("Employee name:", self.name)
        print("Employee salary:", self.salary)

    def bonus(self):

        bonus_amount = 10 / 100 * self.salary
        print("Bonus salary is:", bonus_amount)

    def increment_salary(self, percentage):

        increment = percentage / 100 * self.salary
        self.salary = self.salary + increment
        print("New salary:", self.salary)


e1 = Employee("Kishore", 15000)
e2 = Employee("Pankaj", 20000)

e1.show()
e1.bonus()
e1.increment_salary(10)

print()

e2.show()
e2.bonus()
e2.increment_salary(20)