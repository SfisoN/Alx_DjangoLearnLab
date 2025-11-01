## Command (run inside `python manage.py shell`):
from bookshelf.models import Book
books = Book.objects.get()
for b in books:
print(b.id, b.title, b.author, b.publication_year)


## Expected output (example):
# 1 1984 George Orwell 1949


# Comment: Retrieves all Book objects and prints their attributes.