from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')
    list_filter = ('published_year', 'author')
    search_fields = ('title', 'author')
    ordering = ('-published_year', 'title')
    list_editable = ('author', 'published_year')
    list_per_page = 25
