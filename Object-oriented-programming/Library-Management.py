class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True
        self.issued_to = None

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"{self.book_id} | {self.title} | {self.title} | {self.author} | {status}")


class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"Student Id: {self.student_id}")
        print(f"Name: {self.name}")


class Librarian:

    def __init__(self, librarian_id, name):
        self.librarian_id = librarian_id
        self.name = name

    def display(self):
        print(f"Librarian Id: {self.librarian_id}")
        print(f"Name: {self.name}")


class Transaction:

    def __init__(self, book, student):
        self.book = book
        self.student = student

    def issued_book(self):
        if self.book.is_available:
            self.book.is_available = False
            self.book.issued_to = self.student
            print(f"Book '{self.book.title}' issued to {self.student.name}.")
        else:
            print("Sorry, this book is already issued.")

    def return_book(self):
        if not self.book.is_available:
            self.book.is_available = True
            self.book.issued_to = None
            print(f"Book '{self.book.title}' returned by {self.student.name}.")
        else:
            print("This book was not issued")


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def display_books(self):
        print("\n---- Library Books ----")

        for book in self.books:
            book.display()


# Main Program..

library = Library("City Library")

book1 = Book(101, "Python Programming", "John Smith")
book2 = Book(102, "Data Structures", "Robert Brown")

library.add_book(book1)
library.add_book(book2)

student1 = Student(1, "Ramesh")

librarian1 = Librarian(501, "Priya")

print("\n---- Student Details ----")
student1.display()

print("\n---- Librarian Details ----")
librarian1.display()

library.display_books()

# Issued Books..

transaction = Transaction(book1, student1)

print("\n---- Issued Book ----")
transaction.issued_book()

library.display_books()

# Returned books..

print("\n---- Return Book ----")
transaction.return_book()

library.display_books()