import uuid

from django.db import models

from booksmanager.authors.models import Author


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField(blank=False, null=False)
    isbn_code = models.CharField(blank=False, null=False, max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def author_name(self):
        return self.author.name
