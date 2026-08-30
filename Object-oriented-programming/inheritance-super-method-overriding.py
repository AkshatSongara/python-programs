class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        super().work()
        print("Manager is managing the team")

m = Manager()

m.manage()