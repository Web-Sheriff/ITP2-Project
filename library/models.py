from django.db import models

# Create your models here.
from users.models import User


class Library(models.Model):
    def calculate_items(self):
        pass

    def is_due(self):
        pass

    def overdue_fines(self):
        pass


class UserCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='user_card')
    library_card_number = models.CharField(max_length=100)
    library = models.ForeignKey(Library, on_delete=models.DO_NOTHING, related_name='user_cards')


class Login(models.Model):
	username = models.EmailField()
	password = models.CharField(max_length=128)

