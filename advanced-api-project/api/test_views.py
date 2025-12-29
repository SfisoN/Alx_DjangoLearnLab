from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from api.models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering,
    and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data before each test runs.
        """
        # Create a user for authenticated requests
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create an author
        self.author = Author.objects.create(name="George Orwell")

        # Create books
        self.book1 = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Animal Farm",
            publication_year=1945,
            author=self.author
        )

        # API endpoints
        self.list_url = reverse('book-list')

    # -----------------------------
    # READ TESTS (Public Access)
    # -----------------------------

    def test_list_books(self):
        """
        Ensure unauthenticated users can list books.
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Ensure unauthenticated users can retrieve a single book.
        """
        detail_url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    # -----------------------------
    # CREATE TESTS (Auth Required)
    # -----------------------------

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create books.
        """
        create_url = reverse('book-create')
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create books.
        """
        self.client.login(username='testuser', password='testpassword')

        create_url = reverse('book-create')
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }

        response = self.client.post(create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -----------------------------
    # UPDATE TESTS
    # -----------------------------

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.login(username='testuser', password='testpassword')

        update_url = reverse('book-update', args=[self.book1.id])
        data = {"publication_year": 1950}

        response = self.client.patch(update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.publication_year, 1950)

    # -----------------------------
    # DELETE TESTS
    # -----------------------------

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')

        delete_url = reverse('book-delete', args=[self.book1.id])
        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # FILTER / SEARCH / ORDER TESTS
    # -----------------------------

    def test_filter_books_by_publication_year(self):
        """
        Ensure filtering by publication year works.
        """
        response = self.client.get(
            self.list_url,
            {'publication_year__gte': 1949}
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "1984")

    def test_search_books_by_title(self):
        """
        Ensure search functionality works.
        """
        response = self.client.get(
            self.list_url,
            {'search': 'Animal'}
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Animal Farm")

    def test_order_books_by_publication_year_desc(self):
        """
        Ensure ordering works correctly.
        """
        response = self.client.get(
            self.list_url,
            {'ordering': '-publication_year'}
        )

        self.assertEqual(response.data[0]['title'], "1984")
