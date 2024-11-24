class Observer:
    def update(self, message):
        raise NotImplementedError


class UserObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Notification for {self.name}: {message}")


class LibraryCatalogWithObserver:
    def __init__(self):
        self.books = []
        self.observers = []

    def add_book(self, book):
        self.books.append(book)
        self.notify_observers(f"Book added: {book['title']}")

    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)
