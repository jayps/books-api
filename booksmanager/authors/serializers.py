from rest_framework import serializers

from booksmanager.authors.models import Author
from booksmanager.books.serializers import BookSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
