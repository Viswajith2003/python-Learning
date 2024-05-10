class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        self.checked_out = True

    def return_book(self):
        self.checked_out = False

    def __str__(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        # Using list comprehension to remove book by ISBN
        self.books = [book for book in self.books if book.isbn != isbn]

    def add_member(self, member):
        self.members.append(member)

    def remove_member(self, member_id):
        # Using list comprehension to remove member by ID
        self.members = [member for member in self.members if member.member_id != member_id]

    def checkout_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn and not book.checked_out:
                book.check_out()
                break

        for member in self.members:
            if member.member_id == member_id:
                member.check_out_book(book)
                break

    def return_book(self, isbn, member_id):
        for member in self.members:
            if member.member_id == member_id:
                for book in member.checked_out_books:
                    if book.isbn == isbn:
                        book.return_book()
                        member.return_book(book)
                        break

    def __str__(self):
        book_list = "\n".join([str(book) for book in self.books])
        member_list = "\n".join([str(member) for member in self.members])
        return f"Library: {self.name}\nBooks:\n{book_list}\nMembers:\n{member_list}"


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        self.checked_out_books.append(book)

    def return_book(self, book):
        self.checked_out_books.remove(book)
