# Need to create add and remove book methods
# Need to create borrow, read all borrowed and return a borrowed book

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

    def SortLibrary(self):
        LibraryOfBooks = self.LibraryOfBooks
        ListOfBooks = list(LibraryOfBooks.values())
        ListOfBooks = mergesort.MergeSort(ListOfBooks)
        LibraryOfBooks = dict(enumerate(ListOfBooks))
        del ListOfBooks

    def BrowseForABook(self):
        UserChoice = input("\nType the first letter of the book\'s title - ")
        print("\n\n\n")
        PlaceInAlphabet = letters_place_in_alphabet.GetPlaceInAlphabet(UserChoice)

        SearchResult, CurrentIndex = binarysearch.search(library.LibraryOfBooks, PlaceInAlphabet)

        if len(SearchResult) == 0:
            print("Book Not Found.")
            time.sleep(1.5)
            return

        for index in range(0, len(SearchResult), 1):
            print(str(index + 1) + " - " + SearchResult[index].title + ", " + SearchResult[index].author)
        UserChoice = input("\n\nType the number associated with the book you want - ")
        print("\n")
        IndexUserChoice = int(UserChoice) - 1
        print("\n" + SearchResult[IndexUserChoice].title)
        CurrentIndex = CurrentIndex + IndexUserChoice
        print(CurrentIndex)

    def AddBook(self):
        NewBook = Book(None, None, None, None)
        UserChoice = input("\nType the Name of the Book - ")

        NewBook.title = UserChoice
        NewBook.PlaceInAlphabet = letters_place_in_alphabet.GetPlaceInAlphabet(UserChoice)

        UserChoice = input("Type the Author of the book - ")

        NewBook.author = UserChoice
        NewBook.availability = "Available"

        NextIndex = len(self.LibraryOfBooks)
        self.LibraryOfBooks[NextIndex] = NewBook

    def RemoveBook(self, Index):
        pass


library = Library({})
InsideLibrary = True
library.LibraryOfBooks = storage.LoadContents(library.LibraryOfBooks)
library.SortLibrary()

storage.SaveContents(library.LibraryOfBooks) #Saves the sorted library

while InsideLibrary:

    MainMenuChoice = input()

    if MainMenuChoice.lower() == "exit":
        InsideLibrary = False
    if MainMenuChoice.lower() == "search":
        library.BrowseForABook()
    if MainMenuChoice.lower() == "add":
        library.AddBook()
    
    library.SortLibrary()
    storage.SaveContents(library.LibraryOfBooks)
