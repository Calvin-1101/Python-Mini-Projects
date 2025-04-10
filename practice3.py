
class Book:
    def __init__(self,title,author,is_checked_out = False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
    #please study what is __str__()
    def __str__(self):
        return f"{self.title} by {self.author}"




class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)
        print(self.books)


    def list_avail_books(self):
        for book in self.books:
            if book.is_checked_out == False:
                print(self.book)


    def search_by_title(self, title):
        for book in self.books:
            if book == title:
                print("YES THATS TRUE")


    def borrow_book(title):
        book = self.search_by_title(title)
        if book:
            if book.is_checked_out == False:
                print("Book is available, and has been borrowed by you")
                book.is_checked_out = True
            
            
        else:
            print("Book is unavailable or does not exist")

        
        

    

book1 = Book("Python","MJ", False)
print(book1)

lib = Library()
m1 = lib.add_books(book1)


