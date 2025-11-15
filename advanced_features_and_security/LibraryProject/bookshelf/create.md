## Command (run inside `python manage.py shell`):
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book


## Expected output (an example representation):
# <Book: 1984 by George Orwell (1949)>


# Comment: The `Book.objects.create(...)` call creates and saves the instance to the database and returns the created `Book` object.