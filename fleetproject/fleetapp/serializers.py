from rest_framework import serializers

from .models import Book, LibraryBooks


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class LibraryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = "__all__"
