import datetime
import re

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)


class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)


class Patron(User):
    def search_doc(self, string):
        d1 = self.search_doc_author(string)
        d2 = self.search_doc_title(string)
        d3 = self.search_doc_keywords(string)
        d4 = d1 | d2 | d3
        return d4.distinct()

    def search_doc_author(self, name):
        documents = self.user_card.library.documents.filter(authors__name__contains=name).distinct()
        return documents

    def search_doc_title(self, name):
        documents = self.user_card.library.documents.filter(title__contains=name).distinct()
        return documents

    def search_doc_keywords(self, string):
        words = re.split('[ ,.+;:]+', string)
        documents = self.user_card.library.documents.filter(keywords__word__in=words).distinct()
        return documents

    def check_out_doc(self, document):
        for copy in self.user_card.copies.all():
            if copy.document == document:
                return False
        for copy in document.copies.all():
            if not copy.is_checked_out:
                copy.is_checked_out = True
                self.user_card.copies.add(copy)
                copy.booking_date = datetime.date.today()
                self.user_card.save()
                copy.save()
                return True
        return False

    def return_doc(self, document):
        for copy in self.user_card.copies.all():
            if copy.document == document:
                copy.is_checked_out = False
                self.user_card.copies.exclude(copy)
                self.user_card.save()
                copy.save()
                return True
        return False
        pass

    def has_overdue(self):  # bool
        pass


class Student(Patron):
    pass


class Faculty(Patron):
    pass


class Librarian(User):
    def manage_patron(self):
        pass

    def check_overdue_copy(self):
        pass

    def add_doc(self):
        pass

    def delete_doc(self):
        pass

    def modify_doc(self):
        pass