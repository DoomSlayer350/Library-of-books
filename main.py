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
        ListOfBooks = list(LibraryOfBooks.values())
        ListOfBooks = mergesort.MergeSort(ListOfBooks)
        LibraryOfBooks = dict(enumerate(ListOfBooks))
        del ListOfBooks

    def BrowseForABook(self):
        UserChoice = input("\nType the first letter of the book\'s title - ")
        print("\n\n\n")
        LowerCaseUserChoice = UserChoice.lower()
        FilteredUserChoice = UserChoice.strip()
        ListOfCharacters = list(FilteredUserChoice)
        FirstLetter = ListOfCharacters[0]
        PlaceInAlphabet = letters_place_in_alphabet.GetPlaceInAlphabet(FirstLetter)

        SearchResult = binarysearch.search(library.LibraryOfBooks, PlaceInAlphabet)
        for index in range(0, len(SearchResult), 1):
            print(str(index + 1) + " - " + SearchResult[index].title + ", " + SearchResult[index].author)
        UserChoice = input("\n\nType the number associated with the book you want - ")
        print("\n")
        IndexUserChoice = int(UserChoice) - 1
        print("\n" + SearchResult[IndexUserChoice].title)

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
    
    library.SortLibrary()
    storage.SaveContents(library.LibraryOfBooks)
