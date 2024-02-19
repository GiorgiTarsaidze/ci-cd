from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    def test_book_creation(self):
        book = Book.objects.create(title="Book ", author="Giorgi")

        self.assertEqual(str(book), "Book 1")


# Create your tests here.
