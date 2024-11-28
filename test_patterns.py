from catalog.library_catalog import LibraryCatalog
from catalog.book_adapter import BookAdapter
from users.user_factory import UserFactory
from users.user_observer import UserObserver
from interface.library_interface import LibraryInterface
from iterator.book_iterator import BookIterator

def test_patterns():
    print("### TESTING SINGLETON (LibraryCatalog) ###")
    catalog1 = LibraryCatalog()
    catalog2 = LibraryCatalog()
    print("Catalog instances are the same:", catalog1 is catalog2)
    # klasa LibraryCatalog działa zgodnie z wzorcem Singleton — w całym programie istnieje tylko jedna instancja tego katalogu

    print("\n### TESTING ADAPTER (BookAdapter) ###")
    adapter = BookAdapter()
    json_data = '[{"title": "1410", "author": "Krzysztof Tannenberg", "status": "Available"}]'
    csv_data = "title,author,status\nMr. Robot,Sam Esmail,Available"
    books_from_json = adapter.import_books(json_data, "JSON")
    books_from_csv = adapter.import_books(csv_data, "CSV")
    print("Books from JSON:", books_from_json)
    print("Books from CSV:", books_from_csv)

    print("\n### TESTING FACTORY (UserFactory) ###")
    user_factory = UserFactory()
    student = user_factory.create_user("Tomasz", "Student")
    teacher = user_factory.create_user("Lukasz", "Teacher")
    print("Created users:", student, teacher)

    print("\n### TESTING OBSERVER (UserObserver) ###")
    observer = UserObserver("Tomasz")
    library_interface = LibraryInterface()
    library_interface.catalog.add_observer(observer)
    library_interface.add_book({"title": "Hobbit", "author": "John Tolkien", "status": "Available"})

    print("\n### TESTING FACADE (LibraryInterface) ###")
    library_interface.return_book("Hobbit")  # Inna osoba zwraca książkę
    library_interface.borrow_book("Hobbit", student)  # Tomasz wypożycza książkę

    print("\n### TESTING ITERATOR (BookIterator) ###")
    catalog = LibraryCatalog()
    catalog.add_book({"title": "Petit Prince", "author": "Antoine de Saint", "status": "Available"})
    catalog.add_book({"title": "Meow: A Novel", "author": "Sam Austen", "status": "Available"})

    iterator = BookIterator(catalog.get_books())
    print("Iterating through books:")
    for book in iterator:
        print(book)

if __name__ == "__main__":
    test_patterns()
