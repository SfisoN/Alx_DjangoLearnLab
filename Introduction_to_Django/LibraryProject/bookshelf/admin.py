from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('publication_year', 'author')
    search_fields = ('title', 'author')
    ordering = ('publication_year', 'title')
    list_editable = ('author', 'publication_year')
    list_per_page = 25
