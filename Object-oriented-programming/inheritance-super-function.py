class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

stuobj = Student("Kumar", "Python")

print("Student Name:", stuobj.name)
print("Student Course:", stuobj.course)