class student:

    name = ""
    age = ""
    marks = ""

    def show(self):

        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student marks:", self.marks)

s1 = student()
s2 = student()

s1.name = "Vikram"
s1.age = 25
s1.marks = 80

s1.show()

s2.name = "Lily"
s2.age = 22
s2.marks = 75

s2.show()