class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(self.name, "is studying", self.course)


s = Student("Amit", 22, "Python")

s.introduce()
s.study()