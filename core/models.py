from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=255, null=True)
