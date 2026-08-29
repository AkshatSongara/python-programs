class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):

    def study(self):
        print(self.name, "is studying")

s = Student("Ramesh")

s.show_name()
s.study()