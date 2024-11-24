from catalog.library_catalog import LibraryCatalog
from catalog.book_adapter import BookAdapter
from users.user_factory import UserFactory
from users.user_observer import UserObserver
from interface.library_interface import LibraryInterface
from iterator.book_iterator import BookIterator


def main():
    catalog = LibraryCatalog()
    adapter = BookAdapter()
    user_factory = UserFactory()
    library_interface = LibraryInterface()

    # Singleton and Facade usage
    library_interface.add_book({"title": "1410", "author": "Krzysztof Tannenberg", "status": "Available"})

    # Factory usage
    student = user_factory.create_user("Tomasz", "Student")
    teacher = user_factory.create_user("Lukasz", "Teacher")
    print(student, teacher)

    # Observer usage
    observer = UserObserver("Tomasz")
    library_interface.catalog.add_observer(observer)
    library_interface.return_book("1410")

    # Iterator usage
    iterator = BookIterator(catalog.get_books())
    for book in iterator:
        print(book)


if __name__ == "__main__":
    main()
