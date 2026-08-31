class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is coding")
        super().work()

class Manager(Employee):
    def work(self):
        print("Manager is managing")
        super().work()

class TechLead(Manager, Developer):
    def work(self):
        print("TechLead is leading")
        super().work()

t = TechLead()
t.work()