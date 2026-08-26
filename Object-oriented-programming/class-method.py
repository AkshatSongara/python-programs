class Employee:

    company = "TechCorp"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Kunal")
e2 = Employee("Amit")

print("Employee Company:", e1.company)
print("Employee Company:", e2.company)
print()

Employee.change_company("Google")
# e1.change_company("Microsoft")

print("Employee Company:", e1.company)
print("Employee Company:", e2.company)