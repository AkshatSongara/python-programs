class Employee:
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager is managing")

m = Manager()

m.work()
m.manage()