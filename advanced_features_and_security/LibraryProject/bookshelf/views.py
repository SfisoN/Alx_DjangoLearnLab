# LibraryProject/bookshelf/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from django.http import HttpResponseForbidden
from django import forms

from .models import Book

# Simple ModelForm for Book create/edit
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "pub_date", "summary"]

# List view — requires can_view permission
@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# Detail view — requires can_view permission
@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "bookshelf/book_detail.html", {"book": book})

# Create view — requires can_create permission
@login_required
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("bookshelf:book_list"))
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form, "action": "Create"})

# Edit view — requires can_edit permission
@login_required
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(reverse("bookshelf:book_detail", args=[book.pk]))
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/book_form.html", {"form": form, "action": "Edit", "book": book})

# Delete view — requires can_delete permission
@login_required
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect(reverse("bookshelf:book_list"))
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
