# Code for reading/writing to library
import pathlib
import csv

current_directory = pathlib.Path().resolve() #Gets the current directory
current_directory = str(current_directory) #Convert to string and Replaces backward slashes with forward slashes.

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

def LoadContents(LibraryOfBooks):
    LibraryOfBooks = {}
    FilePath = current_directory + "\\Library.csv"
    print(FilePath)
    
    with open(FilePath, "r") as file:
        Reader = csv.reader(file)
        Index = 0
        for Row in Reader:
            
            if Row == []: #When it gets to the last line, the next row is []
                return LibraryOfBooks
            
            LibraryOfBooks[Index] = Book(Row[0], Row[1], Row[2])
            Index += 1