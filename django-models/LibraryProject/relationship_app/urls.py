from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

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
]
