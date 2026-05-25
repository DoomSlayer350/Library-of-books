#Start by creating a class called Book. Each book object should have attributes such as title, author, ISBN, and availability.

#Create another class called Library that contains a list of books. This class should have methods to add a book, remove a book, and display all books in the library. (use a csv to save all data)

#Implement a method in the Library class that allows a user to search for a book by entering the title or author name. This method should display all matching books.

#Add a method in the Library class that allows a user to borrow a book. This method should update the availability of the book accordingly.

#Finally, create an instance of the Library class and interact with it by adding books, searching for books, borrowing books, and displaying the library's books.

#This project should help you practice working with object-oriented programming concepts in Python while creating a simplified library management system.

dictionary = {}

import csv
import time
import pathlib

current_directory = pathlib.Path().resolve() #Gets the current directory
current_directory = str(current_directory) #Convert to string and Replaces backward slashes with forward slashes.

class Book:
    def __init__(self, title, author, availability):
        self.title = title
        self.author = author
        self.availability = availability

def readcsv(dictionary):

    filepath = current_directory + "\\Library.csv"

    with open(filepath, "r") as file:
        #print("reading")
        reader = csv.reader(file)
        index = 0
        for rows in reader:
            index += 1
            n = 1
            saved_val_list = []
            for value in rows:
                saved_val_list.append(value)
                if n == 3:
                    dictionary[index] = Book(saved_val_list[0],saved_val_list[1],saved_val_list[2])
                    print(dictionary[index])
                n += 1
    return dictionary
#dictionary = readcsv(dictionary)
# print(dictionary)
#line = dictionary[1]
#print(line.title)
#print(line.author)
#print(line.availability)

def writecsv(dictionary):

    filepath = current_directory + "\\Library.csv"

    with open(filepath, "w") as file:

        data = []

        for key in dictionary:
            line = dictionary[key]
            row = []
            row.append(line.title)
            row.append(line.author)
            row.append(line.availability)

            data.append(row)
            

        #print(data)
        
        writer = csv.writer(file)
        
        writer.writerows(data)


#writecsv(dictionary)

def construct_display_dictionary(dictionary):
    display_dictionary = {}
    for key in dictionary:
        line = dictionary[key]
        title = line.title
        author = line.author
        availability = line.availability
        display_dictionary[key] = [title, author, availability]
    return display_dictionary



#display_dictionary = construct_display_dictionary(dictionary)

#print(display_dictionary)

class Library:
    def search_for_a_book(dictionary):
        choice_input = input("Do you want to search using the author's name (type 'a') or do you want to use the book's title (type 't') - \n")
        if choice_input == "a":
            user_search_input = input("Type the author's name - \n")
            user_letter_choice = []
            for letter in user_search_input:
                user_letter_choice.append(letter)
            search_dictionary = {}
            #print(dictionary)
            n = 0
            for key in dictionary:
                line = dictionary[key]
                title = line.title
                author = line.author
                availability = line.availability
                n = 0
                significance = 0
                for letter in author:
                    #print(title)
                    #print(n)
                    try:
                         if letter == user_letter_choice[n]:
                            #print(letter,user_letter_choice[n])
                            significance += 1
                            dictionary_key = (title, author, availability)
                            search_dictionary[dictionary_key] = significance
                            #print(search_dictionary)
                    except Exception as E:
                        #print(E)
                        None
                    n += 1
            #sort = sorted(dict(search_dictionary.items()))
            #print(sort)
            #search_dictionary = sort
            sort = []
            for key in search_dictionary:
                line = search_dictionary[key]
                sort.append(key)
                sort.append(line)
            sort_value = []
            for value in sort:
                #print(type(value))
                if type(value) == int:
                    sort_value.append(value)
            #print(sort_value)
            sort_value.sort(reverse = True)
            #print(sort_value)
            sort = []
            for value in sort_value:
                for key in search_dictionary:
                    line = search_dictionary[key]
                    if value == line:
                        if key in sort:
                            continue
                        sort.append(key)
                        sort.append(line)
            #print(sort)
            sorted_dictionary = {}
            for value in sort:
                index = sort.index(value)
                if index % 2 == 0:
                    sorted_dictionary[value] = sort[index+1]
            #print(sorted_dictionary)
            #print(sort_value)
            return sorted_dictionary
        elif choice_input == "t":
            user_search_input = input("Type the title of the book - \n")
            user_letter_choice = []
            for letter in user_search_input:
                user_letter_choice.append(letter)
            search_dictionary = {}
            #print(dictionary)
            n = 0
            for key in dictionary:
                line = dictionary[key]
                title = line.title
                author = line.author
                availability = line.availability
                n = 0
                significance = 0
                for letter in title:
                    #print(title)
                    #print(n)
                    try:
                        if letter == user_letter_choice[n]:
                            #print(letter,user_letter_choice[n])
                            significance += 1
                            dictionary_key = (title, author, availability)
                            search_dictionary[dictionary_key] = significance
                            #print(search_dictionary)
                    except Exception as E:
                        #print(E)
                        None
                    n+=1
            #sort = sorted(dict(search_dictionary.items()))
            #print(sort)
            #search_dictionary = sort
            sort = []
            for key in search_dictionary:
                line = search_dictionary[key]
                sort.append(key)
                sort.append(line)
            sort_value = []
            for value in sort:
                #print(type(value))
                if type(value) == int:
                    sort_value.append(value)
            #print(sort_value)
            sort_value.sort(reverse = True)
            #print(sort_value)
            sort = []
            for value in sort_value:
                for key in search_dictionary:
                    line = search_dictionary[key]
                    if value == line:
                        if key in sort:
                            continue
                        sort.append(key)
                        sort.append(line)
            #print(sort)
            sorted_dictionary = {}
            for value in sort:
                index = sort.index(value)
                if index % 2 == 0:
                    sorted_dictionary[value] = sort[index+1]
            #print(sorted_dictionary)
            #print(sort_value)
            return sorted_dictionary
    def add_book(dictionary):
        user_title_input = input("Type in the title of the book - \n")
        user_author_input = input("Type in the author's name - \n")
        new_book = Book(user_title_input, user_author_input, "available")
        length = (len(dictionary)) + 1
        dictionary[length] = new_book
        return dictionary
    def remove_book(dictionary):
        user_title_input = input("Type in the title of the book - \n")
        for key in dictionary:
            value = dictionary[key]
            title = value.title
            if title == user_title_input:
                dictionary.pop(key)
                #print(dictionary)
                break
        return dictionary
    def borrow_book(dictionary):
        user_title_input = input("Type in the title of the book - \n")
        borrowed = {}
        for key in dictionary:
            line = dictionary[key]
            if line.title == user_title_input:
                line.availability = "unavailable"
                length_key = len(borrowed) + 1
                current_timestamp = time.time()
                borrowed[length_key] = [line.title, line.author, current_timestamp]
        return dictionary, borrowed
    def writeborrowedcsv(borrowed):

        filepath = current_directory + "\\BorrowedBooks.csv"

        #print(borrowed)
        
        with open(filepath, "w") as file:

            writer = csv.writer(file)

            data = []
            
            for key in borrowed:
                line = borrowed[key]
                data.append(line)

            writer.writerows(data)
    def display_date():
        current_time = time.time()
        current_time = time.ctime(current_time)
        print(current_time)
    def read_borrow(borrowed):

        filepath = current_directory + "\\BorrowedBooks.csv"

        with open(filepath, "r") as file:
            
            reader = csv.reader(file)

            key = 1
            
            for line in reader:
                borrowed[key] = line
                key+=1
            return borrowed

        
    def display_borrowed(borrowed):
        borrow_display = {}
        #print(borrowed)
        for key in borrowed:
            #print("\niterated\n")
            line = borrowed[key]
            n = 1
            borrow_display[key] = []
            for value in line:
                if n == 3:
                    value = float(value)
                    value = time.ctime(value)
                    borrow_display[key].append(value)
                else:
                    borrow_display[key].append(value)
                n += 1
        return borrow_display
        for key in borrow_display:
            line = borrow_display[key]
            #print(line)
            #print(borrow_display)
            if line == []:
                continue
            print(str(key) + ": The title of the book is " + str(line[0]) + ". " + "The author is " + str(line[1]) + ". " + "The date when it was borrowed was " + str(line[2]))
    def return_borrowed_book(dictionary, borrowed):
        user_return_input = input("Type the book's name you want to return - \n")
        for key in borrowed:
            line = borrowed[key]
            n = 1
            for value in line:
                if n == 1:
                    if user_return_input == value:
                        highlighted = value
                        last_key = key
                        break
        del(borrowed[last_key])
        for key in dictionary:
            line = dictionary[key]
            title = line.title
            if title == highlighted:
                line.availability = "available"
        return dictionary, borrowed
    def remove_borrow_nil(borrowed):
        flag = True
        n = 0
        while flag == True:
            n += 1
            if n == 3:
                flag = False
            for key in borrowed:
                line = borrowed[key]
                #print(line)
                if line == []:
                    n = 1
                    del(borrowed[key])
                    break
        return borrowed
#search_dictionary = library.search_for_a_book(dictionary)
#print(search_dictionary)

#dictionary = library.add_book(dictionary)
#print(dictionary)
#writecsv(dictionary)
#dictionary = library.remove_book(dictionary)
#writecsv(dictionary)

#borrowed = library.borrow_book(dictionary)

#library.writeborrowedcsv(borrowed)

#borrowed = {}

#borrowed = library.read_borrow(borrowed)

#print(borrowed)

#borrowed = library.remove_borrow_nil(borrowed)

#print(borrowed)

#library.display_date()

#library.display_borrowed(borrowed)

#dictionary, borrowed = library.return_borrowed_book(dictionary, borrowed)

#print(dictionary, "\n" * 5, borrowed)

def running_program():
    program = True
    library = Library
    dictionary = {}
    borrowed = {}
    dictionary = readcsv(dictionary)
    borrowed = library.read_borrow(borrowed)
    borrowed = library.remove_borrow_nil(borrowed)
    print(("\n" * 3) + "Welcome to the library. For Guidance, type /help to display a command list")
    print("You can do things like borrowing a book, adding a book, leaving the library(ofc you're eventually gonna leave) and much more!")
    while program == True:
        print("\n")
        print("-"*45)
        library.display_date()
        print("-"*45)
        print("\n")
        #print(dictionary, borrowed)
        user_func_input = input()
        if user_func_input == "/help":
            print(
                "\n/display - display all books owned by the library \n" +
                "\n/search - searches for books close or matching to your search \n" +
                "/add - add a book to the library \n" +
                "/remove - remove an existing book from the library \n" +
                "/borrow - borrow an existing book from the library \n" +
                "/inventory - display all borrowed books \n" +
                "/return - return a book that you have borrowed \n" +
                "/leave - leave the library (first command you're probably gonna use) \n"
                )
        elif user_func_input == "/leave":
            writecsv(dictionary)
            library.writeborrowedcsv(borrowed)
            program = False
        elif user_func_input == "/search":
            search_dictionary = library.search_for_a_book(dictionary)
            n = 1
            #print(search_dictionary)
            for key in search_dictionary:
                line = search_dictionary[key]
                #print(key)
                print("\n" + str(n) + ": The title is " + str(key[0]) + ". The author is " + str(key[1]) + ". Currently it is " + str(key[2]) + ". This is how closely it is related to your search: " + str(line))
                n += 1
        elif user_func_input == "/borrow":
            dictionary, borrowed = library.borrow_book(dictionary)
            #print(dictionary, borrowed)
        elif user_func_input == "/inventory":
            borrow_display = library.display_borrowed(borrowed)
            n = 1
            for key in borrow_display:
                line = borrow_display[key]
                #print(str(n))
                print("\n" + str(n) + ": The title is " + str(line[0]) + ". The author is " + str(line[1]) + ". The date when this was borrowed was " + str(line[2]) + ".")
                n+=1
        elif user_func_input == "/display":
            display_dictionary = construct_display_dictionary(dictionary)
            for key in display_dictionary:
                line = display_dictionary[key]
                print("\nTitle: " + str(line[0]) + ", Author: " + str(line[1]) + ", Currently: " + str(line[2]))
        elif user_func_input == "/add":
            dictionary = library.add_book(dictionary)
        elif user_func_input == "/remove":
            dictionary = library.remove_book(dictionary)
        elif user_func_input == "/return":
            dictionary, borrowed = library.return_borrowed_book(dictionary, borrowed)
        else:
            print("I think you typed in the wrong command. Try again - \n")
running_program()
