class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LibraryCatalog, cls).__new__(cls)
            cls._instance.books = []
        return cls._instance

    # def add_book(self, book):
    #     self.books.append(book)
    def add_book(self, book_id, title, author, status="Available"):
        book = {"id": book_id, "title": title, "author": author, "status": status}
        self.books.append(book)

    def get_books(self):
        return self.books

    def find_book(self, title):
        return [book for book in self.books if book['title'] == title]


    def find_book_by_id(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None  # Jeśli książki nie znaleziono
