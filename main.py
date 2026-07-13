#Start by creating a class called Book. Each book object should have attributes such as title, author, ISBN, and availability.

#Create another class called Library that contains a list of books. This class should have methods to add a book, remove a book, and display all books in the library. (use a csv to save all data)

#Implement a method in the Library class that allows a user to search for a book by entering the title or author name. This method should display all matching books.

#Add a method in the Library class that allows a user to borrow a book. This method should update the availability of the book accordingly.

#Finally, create an instance of the Library class and interact with it by adding books, searching for books, borrowing books, and displaying the library's books.

#This project should help you practice working with object-oriented programming concepts in Python while creating a simplified library management system.

import time
import storage

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

class Library:

    def ReturnBook():
        return "Book returned."
    
InsideLibrary = True
while InsideLibrary:
    MainMenuChoice = input()
    if MainMenuChoice.lower() == "exit":
        InsideLibrary = False