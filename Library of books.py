#Start by creating a class called Book. Each book object should have attributes such as title, author, ISBN, and availability.

#Create another class called Library that contains a list of books. This class should have methods to add a book, remove a book, and display all books in the library. (use a csv to save all data)

#Implement a method in the Library class that allows a user to search for a book by entering the title or author name. This method should display all matching books.

#Add a method in the Library class that allows a user to borrow a book. This method should update the availability of the book accordingly.

#Finally, create an instance of the Library class and interact with it by adding books, searching for books, borrowing books, and displaying the library's books.

#This project should help me practice working with object-oriented programming concepts in Python while creating a simplified library management system.

dictionary = {}

import csv
import pathlib

current_directory = pathlib.Path().resolve() #Gets the current directory
current_directory = str(current_directory) #Convert to string and Replaces backward slashes with forward slashes.


def readcsv(dictionary):

    filepath = str(current_directory) + "\\Library.csv"

    with open(filepath, "r") as file:
        print("reading")
        reader = csv.reader(file)
        index = 0
        for rows in reader:
            index += 1
            for value in rows:
                try:
                    REF = dictionary[index]
                    print(REF)
                    print("Value is: " + str(value))
                    dictionary[index] += [value]
                    print(dictionary)
                except Exception as E:
                    print("Error: ", E)
                    dictionary[index] = [value]
        print(dictionary)
        return dictionary
def writecsv(dictionary):

    filepath = str(current_directory) + "\\Library.csv"
    print("doing")
    with open(filepath, "w") as file:
        writer = csv.writer(file)
        for i in dictionary:
            data = [dictionary[i]]
            print(data)
            writer.writerows(data)

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

class Library:
    def add_book(self, book, dictionary):
        for Book in dictionary:
            if book == Book:
                return "Already Available"
        length = len(dictionary) - 1
        dictionary[length] = book
    def remove_book(self, book, dictionary):
        for Book in dictionary:
            if book == Book:
                dictionary[dictionary.index(Book)] = None
                return "Removed", book.title
        return "Unable to find", book.title
    def display(self, dictionary):
        print(dictionary)
    def search(self, dictionary):
        choice_input = input("If you want to search by an Author's name, type 'a'. If you want to search a book by its title, type 't' - \n")
        if choice_input == "a":
            search_input = input("Type the author's name and press ENTER - \n")
            search_dictionary = {}
            choice_input_list = []
            for input_letter in search_input:
                choice_input_list.append(input_letter)
            for key in dictionary:
                value_list = dictionary[key]
                n = 0
                for value in value_list:
                    if n == 1:
                        title = value_list[1]
                        length = len(search_dictionary)
                        length += 1
                        try:
                            search_dictionary[length] = word_significance
                        except Exception as E:
                            print(E)
                        count = 0
                        word_significance = 1
                        print(word_significance)
                        for letter in value:
                            occurence = count
                            try:
                                choice_value = choice_input_list[occurence]
                            except:
                                continue
                            print(count)
                            print(choice_value, letter)
                            if choice_value == letter:
                                word_significance += 1
                                search_dictionary[title] = word_significance
                                print(word_significance)
                            else:
                                count += 1
                                continue
                            count += 1
                    n += 1
        elif choice_input == "t":
            search_input = input("Type the title of the book and press ENTER - \n")
            search_dictionary = {}
            choice_input_list = []
            for input_letter in search_input:
                choice_input_list.append(input_letter)
            for key in dictionary:
                value_list = dictionary[key]
                n = 0
                for value in value_list:
                    if n == 0:
                        title = value_list[0]
                        length = len(search_dictionary)
                        length += 1
                        try:
                            search_dictionary[length] = word_significance
                        except Exception as E:
                            print(E)
                        count = 0
                        word_significance = 1
                        print(word_significance)
                        for letter in value:
                            occurence = count
                            try:
                                choice_value = choice_input_list[occurence]
                            except:
                                continue
                            print(count)
                            print(choice_value, letter)
                            if choice_value == letter:
                                word_significance += 1
                                search_dictionary[title] = word_significance
                                print(word_significance)
                            else:
                                count += 1
                                continue
                            count += 1
                    n += 1
        else:
            print("Control Statements Failed")
        search_dictionary = dict(sorted(search_dictionary.items()))
        print(search_dictionary)
        return search_dictionary

Library = Library()
readcsv(dictionary)
main_body = True

while main_body:
    MainMenuInput = input("Type \'s\' if you would like to search for a specific book.\nType \'a\' if you would like to add a book.\nType \'r\' if you would like to remove a book.\nType \'d\' if you would like to display all books\n\n")
    if MainMenuInput == "s":
        Library.search(dictionary)
    elif MainMenuInput == "a":
        NewBook_title = input("What's the title of the book?\n")
        NewBook_author = input("What's the author of the book?\n")
        NewBook = Book(NewBook_title, NewBook_author, True)
        Library.add_book(Book, dictionary)
    else:
        print("invalid answer.\n")

#BIG DISCLAIMER, the code appears to be broken and I should fix it sometime.