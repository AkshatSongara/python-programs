class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        status = "Available" if self.is_available else "Issued"
        print(f"{self.book_id} | {self.title} | {self.title} | {self.author} | {status}")


book1 = Book(101, "Python Programming", "John Smith")
book2 = Book(102, "Data Structures", "Robert Brown")

book1.display()
book2.display()