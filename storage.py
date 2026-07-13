# Code for reading/writing to library
import pathlib
import csv
from main import Book

current_directory = pathlib.Path().resolve() #Gets the current directory
current_directory = str(current_directory) #Convert to string and Replaces backward slashes with forward slashes.

def LoadContents(LibraryOfBooks):
    FilePath = current_directory + "\\Library.csv"
    print(FilePath)