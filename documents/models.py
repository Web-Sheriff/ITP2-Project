from django.db import models

# Create your models here.
from django.db import models

from users.models import Patron


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)


class Keyword(models.Model):
    word = models.CharField(max_length=255)


class Document(models.Model):
    title = models.CharField(max_length=250)
    authors = models.ManyToManyField(Author, related_name='documents')
    price_value = models.IntegerField(max_length=100)
    keywords = models.ManyToManyField(Keyword, related_name='documents')  # i do not know

    class Meta:
        managed = False


class Copy(models.Model):
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING)
    hash_number = models.IntegerField(max_length=100)
    owner = models.ForeignKey(Patron, on_delete=models.DO_NOTHING)
    is_checked_out = models.BooleanField(max_length=10)


class JournalArticles(Document):
    pass


class Book(Document):
    edition = models.IntegerField(max_length=100)
    pass


class AudioVideo(Document):
	pass