from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

from .models import Library

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



def register(request):
    """
    Displays and processes a UserCreationForm. Logs the user in after successful registration.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # optional: immediately log the user in
            auth_login(request, user)
            # redirect to LOGIN_REDIRECT_URL or any page
            return redirect(reverse_lazy('relationship_app:list_books'))
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# --- Login / Logout using built-in class-based views ---
class AppLoginView(LoginView):
    template_name = "relationship_app/login.html"
    redirect_authenticated_user = True  # if already logged in, redirect

class AppLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"


def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.role == 'Member'


# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")




# Add Book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})



# Edit Book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})



# Delete Book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})