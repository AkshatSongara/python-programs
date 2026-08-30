class Person:
    def introduce(self):
        print("I am a person")

class Employee(Person):
    def work(self):
        print("Employee is working")

class Manager(Employee):
    def manage(self):
        print("Manager is managing the team")

m = Manager()

m.introduce()
m.work()
m.manage()