from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField()
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=255)
