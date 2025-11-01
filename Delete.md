## Command (run inside `python manage.py shell`):
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()


# To confirm deletion:
Book.objects.all()


## Expected output (example):
# <QuerySet []>


# Comment: The book was deleted, and querying all books returns an empty queryset.