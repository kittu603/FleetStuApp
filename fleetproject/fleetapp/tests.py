from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

# Create your tests here.
from .models import Book

client = Client()


class TestAPI(TestCase):

    def test_book_create(self):
        url = reverse('book-create')
        data = {
            "library": "test library",
            "isbn_num": "80000",
            "genre": "SAmple",
            "description": "FOOOO"
        }

        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
