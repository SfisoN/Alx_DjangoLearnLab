This file consolidates the commands and expected outputs for the CRUD operations performed in the Django shell.


## Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected: <Book: 1984 by George Orwell (1949)>


## Retrieve
books = Book.objects.all()
for b in books:
print(b.id, b.title, b.author, b.publication_year)
# Expected example output:
# 1 1984 George Orwell 1949


## Update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# Verify:
book = Book.objects.get(pk=book.pk)
print(book.id, book.title, book.author, book.publication_year)
# Expected: 1 Nineteen Eighty-Four George Orwell 1949


## Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Confirm:
Book.objects.all()
# Expected: <QuerySet []>