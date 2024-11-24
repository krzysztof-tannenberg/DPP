class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.name}"


class UserFactory:
    @staticmethod
    def create_user(name, role):
        if role == "Student":
            return User(name, "Student")
        elif role == "Teacher":
            return User(name, "Teacher")
        elif role == "Librarian":
            return User(name, "Librarian")
        else:
            raise ValueError("Invalid user role")
