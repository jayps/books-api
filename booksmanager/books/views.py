from django.shortcuts import render
from rest_framework import viewsets

from booksmanager.books.models import Book
from booksmanager.books.serializers import BookSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
