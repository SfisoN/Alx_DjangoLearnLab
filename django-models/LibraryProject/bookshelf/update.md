## Command (run inside `python manage.py shell`):
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()


# To verify:
book = Book.objects.get(pk=book.pk)
print(book.id, book.title, book.author, book.publication_year)


## Expected output (example):
# 1 Nineteen Eighty-Four George Orwell 1949


# Comment: The title was updated and saved to the database.