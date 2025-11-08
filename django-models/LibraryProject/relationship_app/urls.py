from django.urls import path
from . import views
from .views import list_books

app_name = "relationship_app"

urlpatterns = [
    # Function-based views
    path("books/text/", views.list_books_text, name="list_books_text"),  # plain text
    path("books/", views.list_books, name="list_books"),                # HTML template

    # Class-based view for Library detail (use pk)
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls", namespace="relationship_app")),
]
