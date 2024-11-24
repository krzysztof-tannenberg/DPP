from catalog.library_catalog import LibraryCatalog
from users.user_observer import LibraryCatalogWithObserver


class LibraryInterface:
    def __init__(self):
        self.catalog = LibraryCatalogWithObserver()

    def add_book(self, book):
        self.catalog.add_book(book)

    def find_book(self, title):
        return self.catalog.find_book(title)

    def borrow_book(self, title, user):
        book = self.catalog.find_book(title)
        if book and book["status"] == "Available":  # Poprawka: `book` jest słownikiem
            book["status"] = "Borrowed"
            print(f"{user.name} borrowed '{title}'.")
        else:
            print(f"The book '{title}' is not available.")

    def return_book(self, title):
        book = self.catalog.find_book(title)
        if book:
            book["status"] = "Available"  # Poprawka: `book` jest słownikiem
            self.catalog.notify_observers(f"The book '{title}' is now available.")
            print(f"The book '{title}' has been returned.")
        else:
            print(f"The book '{title}' is not found in the catalog.")


