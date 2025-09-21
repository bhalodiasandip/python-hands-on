####
# Design a simple Library Management System using OOP concepts.
# It should have:
#     Books
#     Members who can borrow books
#     A library that contains books
#     Support different types of members (Student, Teacher)
#     Show encapsulation, inheritance, has-a relationship, and polymorphism
####
import datetime
from abc import ABC, abstractmethod
class Book:
    def __init__(self, name, category, author):
        self.name, self.category, self.author = name, category, author   
    def __str__(self):
        return f"{self.name} is written by {self.author}"    

class Library:
    __books = []
    def __init__(self, name):
        self.name = name    
    def addBook(self, book: Book):
        self.__books.append(book)
    def getBooks(self):
        return self.__books
    
class Member(ABC): 
    def __init__(self, name):
        self.name = name
    @abstractmethod    
    def borrow(self, book:Book, borrow_date: datetime.datetime): pass

class Student(Member):    
    def borrow(self, book:Book, borrow_date: datetime.datetime):
        print(f"Student {self.name} Borrowed Book: {book.name} on {borrow_date}")

class Teacher(Member):    
    def borrow(self, book:Book, borrow_date: datetime.datetime):
        print(f"Teacher {self.name} Borrowed Book: {book.name} on {borrow_date}")        
        
    
b1 = Book("Bhadar tara vaheta pani", "Drama", "Zaverchand Meghani")
b2 = Book("Zer to pidha zani zani", "Drama", "Manubhai Pancholi")
b3 = Book("Karanghelo", "History", "Kanaiyalal munshi")
lib1 = Library("Pandit Dindayal Upadhyay Library")
lib1.addBook(b1)
lib1.addBook(b2)
lib1.addBook(b3)
for b in lib1.getBooks():
    print(b)
s1 = Student("Raju")
t1 = Teacher("Hariharan")
for obj in [s1, t1]:
    obj.borrow(b1, datetime.datetime.now())