from django.urls import path, include
from rest_framework import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet



router = DefaultRouter()
router.register(r'books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('books-list/', BookList.as_view(())),
    path('', include(router.urls)),            # /api/books/ etc.
    path('books-list/', BookList.as_view()),   # optional ListAPIView endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]