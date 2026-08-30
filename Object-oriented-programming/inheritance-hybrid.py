class person:
    def introduce(self):
        print("I am person")

class Employee(person):
    def work(self):
        print("I am working")

class Trainer(person):
    def train(self):
        print("I am training")

class Manager(Employee, Trainer):
    def manage(self):
        print("I am managing")

m = Manager()

m.introduce()
m.work()
m.train()
m.manage()