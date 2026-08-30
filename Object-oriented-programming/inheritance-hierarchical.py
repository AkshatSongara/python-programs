class Employee:
    def login(self):
        print("Employee logged in")

class Developer(Employee):
    def code(self):
        print("Developer is coding")

class Designer(Employee):
    def design(self):
        print("Designer is Designing")

dev = Developer()
des = Designer()

dev.login()
dev.code()

des.login()
des.design()