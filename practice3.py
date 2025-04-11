
class Book:
    def __init__(self,title,author,is_checked_out = False):
        self.title = title
        self.author = author
        self.is_checked_out = is_checked_out
    #please study what is __str__()
    #we override the __str__() method to specify what we want to return whenever we print() Book
    def __str__(self):
        return f"{self.title} by {self.author}"

    #one issue faced now is, in the class Library, when i want to print self.books, it is in a list of book names
    #when printing lists, python automatically calls the __repr__() method > which will give the output [<__main__.Book object at 0x000001C3E19C3750>]
    #hence, we override the __repr__() method to make it the SAME as __str__()
    def __repr__(self):
        return self.__str__()


class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)


    def list_avail_books(self):
        for book in self.books:
            if book.is_checked_out == False:
                print("testing list_avail_books",book)


    def search_by_title(self, title):
        for book in self.books:
            if title in book.title: #using IF IN statement: if "title" is in book.title, then print true
                print("YES THATS TRUE")
                return book
        return None


    def borrow_book(self,title):
        book = self.search_by_title(title)
        if book:
            if book.is_checked_out == False:
                print("Book is available, and has been borrowed by you")
                book.is_checked_out = True
                print(book)
            
            else:
                print("Book is unavailable for borrow")
        
        else:
            print("Book is invalid")

    def return_book(self,title):
        book = self.search_by_title(title)
        if book:
            if book.is_checked_out == True:
                print("Book has been returned")
                book.is_checked_out = False
            else:
                print("Book is invalid for return")




book1 = Book("Python","MJ", False)
book2 = Book("C++", "Ben", False )
lib = Library()
lib.add_books(book1)
lib.add_books(book2)
lib.list_avail_books()


#lib.search_by_title("C++")


lib.borrow_book("C++")

lib.list_avail_books()

lib.return_book("C++")

lib.list_avail_books()
