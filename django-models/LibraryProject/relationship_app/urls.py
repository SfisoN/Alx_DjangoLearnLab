from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from . import admin_view, librarian_view, member_view

app_name = "relationship_app"

urlpatterns = [
    # existing app views
    path("books/text/", views.list_books_text, name="list_books_text"),
    path("books/", views.list_books, name="list_books"),
    path("libraries/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # authentication URLs — use built-in class names and function literally
    path("register/", views.register, name="register"),  # ✅ views.register
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),  # ✅ LoginView.as_view(template_name=
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),  # ✅ LogoutView.as_view(template_name=

    path("admin-view/", admin_view.admin_view, name="admin_view"),
    path("librarian-view/", librarian_view.librarian_view, name="librarian_view"),
    path("member-view/", member_view.member_view, name="member_view"),

    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/<int:pk>/", views.edit_book, name="edit_book"),
    path("delete_book/<int:pk>/", views.delete_book, name="delete_book"),
]
