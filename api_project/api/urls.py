from django.urls import path, include
from rest_framework import DefaultRouter
from .views import BookList, BookViewSet



router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books-list/', BookList.as_view(())),
]