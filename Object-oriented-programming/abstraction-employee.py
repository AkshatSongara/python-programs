from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):

    def salary(self):
        print("Developer Salary: 50,000")

class Manager(Employee):

    def salary(self):
        print("Manager Salary: 80,000")

class Tester(Employee):

    def salary(self):
        print("Tester Salary: 45,000")

developer = Developer()
manager = Manager()
tester = Tester()

developer.salary()
manager.salary()
tester.salary()