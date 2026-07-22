# Code for reading/writing to library
import pathlib
import csv
import mergesort
from book import Book

current_directory = pathlib.Path().resolve() #Gets the current directory
current_directory = str(current_directory) #Convert to string and Replaces backward slashes with forward slashes.

def LoadContents(LibraryOfBooks):
    LibraryOfBooks = {}
    FilePath = current_directory + "\\Library.csv"
    
    with open(FilePath, "r") as file:
        Reader = csv.reader(file)
        Index = 0
        for Row in Reader:
            if Row == []: #Skip Empty Rows
                continue
            LibraryOfBooks[Index] = Book(Row[0], Row[1], Row[2], int(Row[3]))
            Index += 1
        return LibraryOfBooks



def SaveContents(LibraryOfBooks):

    filepath = current_directory + "\\Library.csv"

    with open(filepath, "w") as file:

        data = []

        for Key in LibraryOfBooks:

            line = LibraryOfBooks[Key]
            row = []
            row.append(line.title)
            row.append(line.author)
            row.append(line.availability)
            row.append(line.PlaceInAlphabet)
            data.append(row)
            
        writer = csv.writer(file)
        writer.writerows(data)