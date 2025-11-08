from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from .models import Book, Library, Librarian

# Create your views here.

def list_books_text(request):
    """
    Function-based view that returns a simple plain-text list of book titles
    and their authors (one per line). URL: /books/text/
    """
    books = Book.objects.all()
    lines = [f"{b.title} — {b.author.name}" for b in books]
    # join with newlines and return as plain text
    body = "\n".join(lines) if lines else "No books found."
    return HttpResponse(body, content_type="text/plain; charset=utf-8")


def list_books(request):
    """
    Function-based view that renders the list_books.html template with all books.
    URL: /books/
    """
    books = Book.objects.select_related('author').all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    """
    Class-based DetailView to display a Library and all its books.
    Model: Library
    Template expected: relationship_app/library_detail.html
    URL: /libraries/<int:pk>/  (or use slug if you change it)
    """
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

def get_queryset(self):
     # prefetch books and their authors to avoid N+1 queries
    return Library.objects.prefetch_related('books__author').all()