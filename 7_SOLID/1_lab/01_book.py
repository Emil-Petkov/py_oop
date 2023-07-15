# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page

######################################################################

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = 0

    def turn_page(self, pages):
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None


book1 = Book("Python for beginners", "Emil Petkov")
book1.turn_page(650)

book2 = Book("From Zero to Hero in Python", "Emil Petkov")
book2.turn_page(900)

library = Library()
library.add_book(book1)
library.add_book(book2)

search = library.find_book("Python for beginners")
print(search.title)  # Python for beginners
print(search.author)  # Emil Petkov
print(book1.pages)  # 650
