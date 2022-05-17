class Book:
    def __init__(self, book_title, author_name, publisher_name):
        self.book_title = book_title
        self.author_name = author_name
        self.publisher_name = publisher_name

    def set_book_title(self, book_title):
        self.book_title = book_title

    def set_author_name(self, author_name):
        self.author_name = author_name

    def set_publishers_name(self, publisher_name):
        self.publisher_name = publisher_name

    def get_book_title(self):
        return self.book_title

    def get_author_name(self):
        return self.author_name

    def get_publisher_name(self):
        return self.publisher_name

    def __str__(self):
        return ("Book Title: " + str(self.book_title) +
                "\nAuthor Name: " + str(self.author_name) +
                "\nPublisher Name: " + str(self.publisher_name))


book1 = Book("Kidagaa","Ken W.","Eagle Inc")
print(book1.__str__())