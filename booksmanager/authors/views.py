from rest_framework import viewsets

from booksmanager.authors.models import Author
from booksmanager.authors.serializers import AuthorSerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
