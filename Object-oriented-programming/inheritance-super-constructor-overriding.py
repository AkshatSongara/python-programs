class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am person")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        super().introduce()
        print("I am student")

s = Student("Amit", "Python")

print(s.name)
print(s.course)
s.introduce()