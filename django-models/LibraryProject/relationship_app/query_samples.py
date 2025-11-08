from .models import Author, Book, Library


# 1️⃣ Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


# 2️⃣ List all books in a specific library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books


# 3️⃣ Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian
