class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"

    def display_details(self):
        print("\n------ Book Details ------")
        print("Book ID     :", self.book_id)
        print("Title       :", self.title)
        print("Author      :", self.author)
        print("Status      :", self.status)

    def issue_book(self):
        self.status = "Issued"
        print("\nBook issued successfully.")

    def return_book(self):
        self.status = "Available"
        print("\nBook returned successfully.")


# Input
book_id = input("Enter Book ID : ")
title = input("Enter Book Title : ")
author = input("Enter Author Name : ")

# Object Creation
obj = Book(book_id, title, author)

# Initial Details
obj.display_details()

# Issue Book
obj.issue_book()
obj.display_details()

# Return Book
obj.return_book()
obj.display_details()