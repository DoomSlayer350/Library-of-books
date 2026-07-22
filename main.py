#Start by creating a class called Book. Each book object should have attributes such as title, author, ISBN, and availability.

#Create another class called Library that contains a list of books. This class should have methods to add a book, remove a book, and display all books in the library. (use a csv to save all data)

#Implement a method in the Library class that allows a user to search for a book by entering the title or author name. This method should display all matching books.

#Add a method in the Library class that allows a user to borrow a book. This method should update the availability of the book accordingly.

#Finally, create an instance of the Library class and interact with it by adding books, searching for books, borrowing books, and displaying the library's books.

#This project should help you practice working with object-oriented programming concepts in Python while creating a simplified library management system.

import time
import storage
import mergesort
import letters_place_in_alphabet
import binarysearch
from book import Book

# Search Functions

def SearchBookUsingAuthorName(LibraryOfBooks):
    SearchInput = input("Type the Author's name - ")
    
class Library:
    
    def __init__(self, LibraryOfBooks):
        self.LibraryOfBooks = LibraryOfBooks

    def BrowseForABook(self):
        UserChoice = input("\nType the title of the book - ")
        LowerCaseUserChoice = UserChoice.lower()
        FilteredUserChoice = UserChoice.strip()
        ListOfCharacters = list(FilteredUserChoice)
        FirstLetter = ListOfCharacters[0]
        PlaceInAlphabet = letters_place_in_alphabet.GetPlaceInAlphabet(FirstLetter)

        SearchResult = binarysearch.search(library.LibraryOfBooks, PlaceInAlphabet)
        print(SearchResult)
        print(SearchResult[0].title)

library = Library({})
LibraryOfBooks = {}
InsideLibrary = True
LibraryOfBooks = storage.LoadContents(LibraryOfBooks)
ListOfBooks = list(LibraryOfBooks.values())
print(ListOfBooks)
ListOfBooks = mergesort.MergeSort(ListOfBooks)
print(ListOfBooks)
LibraryOfBooks = dict(enumerate(ListOfBooks))
print(LibraryOfBooks)
library.LibraryOfBooks = LibraryOfBooks

storage.SaveContents(LibraryOfBooks) #Saves the sorted library
del ListOfBooks


while InsideLibrary:

    MainMenuChoice = input()

    if MainMenuChoice.lower() == "exit":
        InsideLibrary = False
    if MainMenuChoice.lower() == "search":
        library.BrowseForABook()
