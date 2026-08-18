class Book:
    def __init__(self, title, author, isbn, is_available = True):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = is_available 

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value.strip():
            print("Invalid")
        else:
            self.__title = value

    @property
    def author(self):
        return self.__author
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def is_available(self):
        return self.__is_available
    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
        else:
            print("Already borrowed")

    def return_book(self):
            self.__is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} | Available: {self.is_available}"
    
class EBook(Book):
    def __init__(self, title, author, isbn, is_available, file_size, format):
        super().__init__(title, author, isbn, is_available)
        self.file_size = file_size
        self.format = format

    def __str__(self):
        return super().__str__() + f"  | {self.file_size}MB and {self.format} Format"
    
    def download(self):
        print(f"Downloading {self.title} {self.file_size}MB.....")

class Person:
    def __init__(self, name, age, email):
        self.__name = name
        self.__age = age 
        self.__email = email

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value.strip():
            print("Invalid")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 0 or value > 120:
            print("Invalid")
        else:
            self.__age = value

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            print("Invalid")
        else:
            self.__email = value
    
    def introduce(self):
        return f"Name  :  {self.name}\nAge  :  {self.age}\nEmail :  {self.email}"
    
class Member(Person):
    def __init__(self, name, age, email, member_id, borrowed_book = None):
        super().__init__(name, age, email)
        self.member_id = member_id
        self.borrowed_book = borrowed_book if borrowed_book is not None else []

    def borrow(self, book):
        return self.borrowed_book.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
    
    def introduce(self):
        return super().introduce() + f"\nMember_ID: {self.member_id}"
    
    def display_borrowed(self):
        print(f"Borrowed Books : {self.borrowed_book}")

class Librarian(Person):
    def __init__(self, name, age, email, employee_id, salary):
        super().__init__(name, age, email)
        self.__employee_id = employee_id
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id
    
    @property
    def salary(self):
        return self.__salary
    
    def add_book(self, library, book):
        library.add_book(book)
    
    def remove_book(self, library, title):
        library.remove_book(title)
    
    def introduce(self):
        return super().introduce() + f"\nEmployee_ID: {self.employee_id}\nSalary : {self.salary}"
    
class Library:
    def __init__(self, name, books = None, members = None):
        self.__name = name 
        self.__books = books if books is not None else {}
        self.__members = members if members is not None else []

    def add_book(self, book):
        self.__books[book.isbn] = book

    def remove_book(self, isbn):
        if isbn in self.__books:
            del self.__books[isbn]
        else:
            print("Not Found")

    def register_member(self, m):
        self.__members.append(m)

    def find_book(self, title):
        for book in self.__books.values():
            if book.title == title:
                return book
        return None
    
    def available_books(self):
        return list(self.__books.keys())
    
    def display_all(self):
        print("Books:")
        for book in self.__books.values():
            print(book)
        print(f"Members : {len(self.__members)}")


b1 = Book("python", "Eric Matthes", "ISBN001")
e1 = EBook("Learn ML", "Andrew Ng", "ISBN002", True,  15.5, "PDF")
m1 = Member("viswanath", 21, "vishu@gmail.com", "M001")
lib1 = Librarian("Kumar", 35, "Kumar@library.com", "E001", 45000)

library = Library("City Library")

lib1.add_book(library, b1)
lib1.add_book(library, e1)

library.register_member(m1)

m1.borrow(b1)
m1.display_borrowed()

m1.borrow(b1)

m1.return_book(b1)
m1.borrow(b1)

library.display_all()
library.available_books()


