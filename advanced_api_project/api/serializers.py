from rest_framework import serializers
from .models import Author, Book
from datetime import date


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']



class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = date.today().year
        if value.year > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
