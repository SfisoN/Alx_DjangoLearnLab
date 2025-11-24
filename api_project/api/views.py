from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    uthentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAdminOrReadOnly,)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)