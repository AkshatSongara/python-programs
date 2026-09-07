class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        # status = "Available" if self.is_available else "Issued"
        print(f"{self.book_id} | {self.title} | {self.title} | {self.author}")


class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"Student Id: ", {self.student_id})
        print(f"Name: ", {self.name})


class Librarian:

    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name

    def display(self):
        print(f"Librarian Id: ", {self.librarian_id})
        print(f"Name: ", {self.name})

book1 = Book(101, "Python Programming", "John Smith")
book2 = Book(102, "Data Structures", "Robert Brown")

book1.display()
book2.display()

student1 = Student(1, "Ramesh")
student1.display()

librarian = Librarian(501, "Priya")
librarian.display()