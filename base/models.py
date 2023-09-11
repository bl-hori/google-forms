from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    email = models.EmailField(unique=True)