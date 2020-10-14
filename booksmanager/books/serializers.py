from rest_framework import serializers

from booksmanager.authors.models import Author
from booksmanager.books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'isbn_code',
            'author',
            'author_name',
        )
