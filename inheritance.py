from Book import Book


class Lib(Book):
    def __init__(self, book_title, author_name, publisher_name, location, size):
        # Book.__init__(book_title, author_name, publisher_name)
        super().__init__(book_title, author_name, publisher_name)
        location = location
        size = size


lib = Lib("Kidagaa", "Ken W.", "Eagle Inc", "Kibabii", 4)
print(lib.get_book_title())
