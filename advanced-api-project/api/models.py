from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the author's full name")

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Enter the book title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="Select the author of the book")
    publication_year = models.DateField(help_text="Enter the date the book was published")

    def __str__(self):
        return self.title